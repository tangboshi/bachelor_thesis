
#!/bin/bash

source measurement.conf

function setup_remote_connection
{
  reset
  # echo "Setting up remote connection..."
  # if ( mount | grep $REMOTE_MEASUREMENT_MOUNT_POINT  )
  # then
  #   echo "The mount point is in use, confirm unmount with your password."
  #   sudo umount $REMOTE_MEASUREMENT_MOUNT_POINT
  # fi
  # echo "Please enter the server password to mount the target directory."
  # mkdir -p $REMOTE_MEASUREMENT_MOUNT_POINT
  #sshfs $REMOTE_USER@$REMOTE_IP:$REMOTE_TO_MOUNT_PATH $REMOTE_MEASUREMENT_MOUNT_POINT
  #ssh -$REMOTE_FLAGS $REMOTE_USER@$REMOTE_IP "$(typeset -f); main"
  sshpass -p "inets" ssh -$REMOTE_FLAGS $REMOTE_USER@$REMOTE_IP "bash -s" < remote_measurement.sh
}

function prepare_measurement
{
    reset
    MEASUREMENT_COUNTER=0
    ## Let's make sure all the directories exist
    printf "\nChecking if paths exists...\n"

    #Let's first make absolutely sure the raw data source path exists
    if [ ! -d $RAW_DATA_SOURCE_PATH ];
      then
        mkdir -p $RAW_DATA_SOURCE_PATH
        echo $RAW_DATA_SOURCE_PATH" created."
    fi

    if [ -d $PLOT_DIRECTORY_PATH ];
      then
        echo $PLOT_DIRECTORY_PATH" already existed!"
        cd $PLOT_DIRECTORY_PATH
        # create measurement directory
        while [ -d $MEASUREMENT_COUNTER ]; do
            MEASUREMENT_COUNTER=$(($MEASUREMENT_COUNTER+1))
        done
        export MEASUREMENT_COUNTER;
    fi

    if [ -d $LOG_PATH ];
      then
        echo $LOG_PATH" already existed!"
      else
        mkdir -p $LOG_PATH
        echo $LOG_PATH" directory created."
    fi

    mkdir -p $PLOT_DIRECTORY_PATH/$MEASUREMENT_COUNTER
    echo $PLOT_DIRECTORY_PATH/$MEASUREMENT_COUNTER" directory created."

    mkdir -p $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER
    echo $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER" directory created."

    mkdir -p $JOBS_OPEN_PATH
    mkdir -p $JOBS_DONE_PATH

    ## Let's check if measurement script is defined
    # If $MEASUREMENT_SCRIPTS undefined:
    # Go through directory and list all python files
    if [ -z ${MEASUREMENT_SCRIPTS+x} ];
      then
        echo  "No measurement scripts set,
              going through files inside of $LOCATE_BASE_PATH."
        echo "Please add a the full path of one of the files to \$SCRITPS."
        locate -r "$LOCATE_BASE_PATH" | grep "\.py$"
        echo "Terminated."
        exit -1
    fi

    printf "\n"
}

function measure
{
  local PREMATURELY_ABORTED=0

  for ((x = 1 ; x <= $MEASUREMENT_REPETITIONS ; x += 1)); do

    # Get pid to later kill it
    for i in "${MEASUREMENT_SCRIPTS[@]}"
    do
      python $MEASUREMENT_SCRIPT_PATH/$i &
      #MEASUREMENT_SCRIPTS_PID+=($!)
    done

    for ((y = $TIMER ; y > 0 ; y -= 1)); do
      echo "Measurement $x/$MEASUREMENT_REPETITIONS complete in $y second(s)."
      if [ $CHECK_IF_PREMATURELY_ABORTED -eq 1 ];
        then
          if ps -p ${MEASUREMENT_SCRIPTS_PID[*]};
            then
              :
            else
              PREMATURELY_ABORTED=1
              echo  "Scripts were killed prematurely.
                    Measurement may be incomplete."
              break
          fi
      fi
      sleep 1
    done

    # Kill scripts if running
    #sleep 1
    #if {ps -p ${MEASUREMENT_SCRIPTS_PID[*]}} &>/dev/null;
    #  then
    #    kill ${MEASUREMENT_SCRIPTS_PID[*]}
    #fi
    kill $(jobs -p)

    # Save this measurement's data to special folder
    mkdir -p $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER/$x
    echo  "Measurement $x raw data directory created $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER/$x/."
    mv -v $RAW_DATA_SOURCE_PATH/* $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER/$x/
    echo  "Measurement $x raw data moved to $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER/$x/."
    printf "\n"

    # Will only ever be true if $CHECK_IF_PREMATURELY_ABORTED is set to 1
    if [ $PREMATURELY_ABORTED -eq 1 ];
      then
        if [ $PLOT_IF_PREMATURELY_ABORTED -eq 0 ];
          then
            echo "Plotting if measurement prematurely aborted set to false."
            echo "Terminated."
            exit -1
        fi
    fi

  done

  #Exit remote connection
  if [ $REMOTE_MEASUREMENT -eq 1 ]; then
    exit
  fi
}

function plot
{
  ## Plot the results
  echo "Now processing results..."

  # Call the plotting scripts as data
  #echo "Starting to generate plots..."
  echo "Plotting Python should be: "$PLOT_PY" ("$OS")."

  for i in ${PLOT_SCRIPTS[@]}; do
    bash -c "$PLOT_PY $PLOT_PY_PATH/$i"
  done

  printf "\n"
  echo "+--------------------------------------------------------------+"
  echo "| Plotting completed. Until the next measurement session then! |"
  echo "+--------------------------------------------------------------+"
}

function cleanup
{
    ##Cleaning up the mess you created!
    #Kill all child proceesses
    echo "Staring cleanup..."
    echo "Killing all lingering child processes..."
    killall -9 -g $0
    cd $THIS_PATH
    exit
}
trap cleanup SIGHUP SIGINT SIGKILL;
trap "cd $THIS_PATH" EXIT;

function main
{
  # Clear up console
  #reset
  # Check if jobs_open directory is empty
  if [ ! "$(ls -A $JOBS_OPEN_PATH)" ]; then
    echo "There seem to be no open jobs. Measuring with default parameters."
    prepare_measurement
    #Take measurements
    measure | tee -a $LOG_PATH/default_$MEASUREMENT_COUNTER.log
    # Create plot if desired
    if [ $PLOT_ENABLED -eq 1 ]; then
      plot | tee -a $LOG_PATH/default_$MEASUREMENT_COUNTER.log; fi
  else
    prepare_measurement
    echo "Open jobs detected! Let's get to work..."
    JOBS=$JOBS_OPEN_PATH/*
    for job in $JOBS; do
      source $job;
      job_name=$(echo $job | rev | cut -d"/" -f1 | rev )
      #echo $job_name
      measure | tee -a $LOG_PATH/$job_name"_"$MEASUREMENT_COUNTER.log
      if [ $PLOT_ENABLED -eq 1 ]; then
        plot | tee -a $LOG_PATH/$job_name"_"$MEASUREMENT_COUNTER.log;
      fi
      if [ $MOVE_AFTER_JOB_DONE -eq 1 ]; then
        cp $job $PLOT_DIRECTORY_PATH/$MEASUREMENT_COUNTER/
        mv $job $JOBS_DONE_PATH/
      fi
      export MEASUREMENT_COUNTER=$((MEASUREMENT_COUNTER++))
    done
  fi

}

if [ $DEBUG_MODE -eq 1 ]; then
  printf "\n"
  echo "+-----------------------------------------------------------+"
  echo "| Debug mode is active, results are saved in the debug dirs |"
  echo "+-----------------------------------------------------------+"
fi

if [ $REMOTE_MEASUREMENT -eq 1 ]; then
  # Call to main included here
    setup_remote_connection
  else
    main
fi
