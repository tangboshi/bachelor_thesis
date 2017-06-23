#!/bin/bash

#********************************* Options ************************************
## Path and remote options
#Remote options
REMOTE_MEASUREMENT=0
REMOTE_IP=134.130.223.135
REMOTE_FLAGS=YC4
REMOTE_USER_NAME=inets
REMOTE_TO_MOUNT_PATH=/home/inets
REMOTE_MEASUREMENT_MOUNT_POINT=/home/alex/mnt/$REMOTE_IP

# Other paths
THIS_PATH=$( cd $(dirname $0) ; pwd -P )

if [ $REMOTE_MEASUREMENT -eq 1 ]; then
  LOCATE_BASE_PATH=$REMOTE_MEASUREMENT_MOUNT_POINT/source/gr-inets/examples/Tests
else
  LOCATE_BASE_PATH=$THIS_PATH
fi

JOBS_OPEN_PATH=$THIS_PATH/jobs_open
JOBS_DONE_PATH=$THIS_PATH/jobs_done
PLOT_PY_PATH=$THIS_PATH/py
export PLOT_DIRECTORY_PATH=$THIS_PATH/plots
export DATA_SOURCE_PATH=$THIS_PATH/data

if [ $REMOTE_MEASUREMENT -eq 1 ]; then
  MEASUREMENT_SCRIPT_PATH=$LOCATE_BASE_PATH
  export RAW_DATA_SOURCE_PATH=$REMOTE_MEASUREMENT_MOUNT_POINT/source/gr-inets/results
else
  MEASUREMENT_SCRIPT_PATH=$LOCATE_BASE_PATH/py/fake_measurements
  export RAW_DATA_SOURCE_PATH=$MEASUREMENT_SCRIPT_PATH/measurement_raw
    #export RAW_DATA_SOURCE_PATH=/home/inets/source/gr-inets/results
fi

## Premature death checks
CHECK_IF_PREMATURELY_ABORTED=0
PLOT_IF_PREMATURELY_ABORTED=0
## Python Version
PLOT_PYTHON_VERSION=3
MEASUREMENT_PYTHON_VERSION=2
OS=ARCH

case $OS in
  "ARCH")
    if    [ $MEASUREMENT_PYTHON_VERSION -eq 2 ]; then MEASURE_PY=python2;
    elif  [ $MEASUREMENT_PYTHON_VERSION -eq 3 ]; then MEASUERE_PY=python; fi
    if    [ $PLOT_PYTHON_VERSION -eq 2 ]; then PLOT_PY=python2;
    elif  [ $PLOT_PYTHON_VERSION -eq 3 ]; then PLOT_PY=python; fi
  ;;

  "UBUNTU")
    if    [ $MEASUREMENT_PYTHON_VERSION -eq 2 ]; then MEASUERE_PY=python;
    elif  [ $MEASUREMENT_PYTHON_VERSION -eq 3 ]; then MEASUERE_PY=python3; fi
    if    [ $PLOT_PYTHON_VERSION -eq 2 ]; then PLOT_PY=python;
    elif  [ $PLOT_PYTHON_VERSION -eq 3 ]; then PLOT_PY=python3; fi
  ;;
esac

#********************* Important Measurement Variables ************************
## Series options (!MOST IMPORTANT VARIABLES HERE)
TIMER=1
export MEASUREMENT_REPETITIONS=5
MEASUREMENT_SCRIPTS=( measure.py )
#MEASUREMENT_SCRIPTS=( two_way_handshake_Rx.py  two_way_handshake_Tx.py )
MEASUREMENT_OUTPUT_FILES=( t1DQ.txt t1CS.txt t2RXe.txt t2e.txt )
export MEASUREMENT_OUTPUT_FILES=${MEASUREMENT_OUTPUT_FILES[*]}
PLOT_SCRIPTS=( cdf.py )
## Plot options
PLOT_ENABLED=1
export PLOT_SAVE_ENABLED=1
# The name of the saved files
export PLOT_NAMES_TRUNK=throughput
#******************************************************************************
#    SET THIS TO 0 IF YOU WANT TO CARRY OUT MULTIPLE MEASUREMENTS IN A ROW!   *
#******************************************************************************
export SHOW_PLOT_AFTER_MEASUREMENT=0
## Specific plot parameters
# Required to have the correct values for some calculations (absolute values)
export PACKET_SIZE=1000 #bytes
#******************************************************************************

function setup_remote_connection
{
  if ( mount | grep $REMOTE_USER_NAME  )
  then
    echo "The mount point is in use, confirm unmount with your password."
    sudo umount $REMOTE_MEASUREMENT_MOUNT_POINT
  fi
  echo "Please enter the server password to mount the target directory."
  sshfs $REMOTE_USER_NAME@$REMOTE_IP:$REMOTE_TO_MOUNT_PATH $REMOTE_MEASUREMENT_MOUNT_POINT
  ssh -$REMOTE_FLAGS $REMOTE_IP
}

function prepare_measurement
{
    if [ $REMOTE_MEASUREMENT -eq 1 ]; then
      setup_remote_connection
    fi

    MEASUREMENT_COUNTER=0
    ## Let's make sure all the directories exist
    printf "\nChecking if paths exists...\n"

    # Let's first make absolutely sure the raw data source path exists
    #if [ ! -d $RAW_DATA_SOURCE_PATH ];
    #  then
    #    echo $RAW_DATA_SOURCE_PATH" is not a valid path."
    #    echo "Terminated."
    #    exit -1
    #fi

    if [ -d $PLOT_DIRECTORY_PATH ];
      then
        echo $PLOT_DIRECTORY_PATH" already existed!"
        cd $PLOT_DIRECTORY_PATH
        # create measurement directory
        while [ -d $MEASUREMENT_COUNTER ]; do
            MEASUREMENT_COUNTER=$[$MEASUREMENT_COUNTER+1]
        done
        export MEASUREMENT_COUNTER;
    fi

    mkdir -p $PLOT_DIRECTORY_PATH/$MEASUREMENT_COUNTER
    echo $PLOT_DIRECTORY_PATH/$MEASUREMENT_COUNTER" directory created."

    mkdir -p $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER
    echo $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER" directory created."

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
      MEASUREMENT_SCRIPTS_PID+=($!)
    done

    # Counteract ssh and GR lag
    if [ $REMOTE_MEASUREMENT -eq 1 ]; then
      sleep 2
    fi

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
    if {ps -p ${MEASUREMENT_SCRIPTS_PID[*]}} &>/dev/null;
      then
        kill ${MEASUREMENT_SCRIPTS_PID[*]}
    fi

    # Save this measurement's data to special folder
    mkdir -p $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER/$x
    echo  "Measurement $x raw data directory created $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER/$x/."
    mv $RAW_DATA_SOURCE_PATH/* $DATA_SOURCE_PATH/$MEASUREMENT_COUNTER/$x/
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
  echo "Starting to generate plots..."
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
  # Prepare Measurement
  prepare_measurement

  # Check if jobs_open directory is empty
  if [ ! "$(ls -A $JOBS_OPEN_PATH)" ]; then
    echo "There seem to be no open jobs. Measuring with default parameters."
    #Take measurements
    measure
    # Create plot if desired
    if [ $PLOT_ENABLED -eq 1 ]; then plot; fi
  else
    echo "Open jobs detected! Let's get to work..."
    JOBS=$JOBS_OPEN_PATH/*
    for job in $JOBS; do
      source $job;
      measure
      if [ $PLOT_ENABLED -eq 1 ]; then plot; fi
      mv $job $JOBS_DONE_PATH/
      MEASUREMENT_COUNTER=$MEASUREMENT_COUNTER+1
    done
  fi

}

main
