#!/bin/bash

#********************************* Options ************************************
## Path options
THIS_PATH=$( cd $(dirname $0) ; pwd -P )
  # Fall back to absolute path if the construct above fails
  # THIS_PATH="/home/alex/0_data/2017_Coding_Experiments/bash"
  # THIS_PATH="/home/inets/source/gr-inets/measurement"
LOCATE_BASE_PATH=$THIS_PATH
PLOT_PY_PATH=$THIS_PATH/py
export PLOT_DIRECTORY_PATH=$THIS_PATH/plots
#MEASUREMENT_SCRIPT_PATH=/home/inets/source/gr-inets/examples/Tests
  #For testing purpose use this path
  MEASUREMENT_SCRIPT_PATH=$PLOT_PY_PATH/fake_measurements
DATA_SOURCE_PATH=$THIS_PATH/data
#RAW_DATA_SOURCE_PATH=$THIS_PATH/../results
  #RAW_DATA_SOURCE_PATH=/home/inets/source/gr-inets/results
  #export is needed to let fake_measurements.py know where to output data
  export RAW_DATA_SOURCE_PATH=$MEASUREMENT_SCRIPT_PATH/measurement_raw
# Premature death checks
CHECK_IF_PREMATURELY_ABORTED=0
PLOT_IF_PREMATURELY_ABORTED=0
#********************* Important Measurement Variables ************************
## Series options (!MOST IMPORTANT VARIABLES HERE)
TIMER=2
MEASUREMENT_REPETITIONS=5
MEASUREMENT_SCRIPTS=( measure.py )
PLOT_SCRIPTS=( cdf.py )

## Plot options
PLOT_ENABLED=1
export PLOT_SAVE_ENABLED=1
export PLOT_TYPE=cdf
# The name of the saved files
export PLOT_NAMES_TRUNK=throughput
## Specific plot parameters
# Required to have the correct values for some calculations (absolute values)
export PACKET_SIZE=1000
#******************************************************************************

function prepare_measurement
{
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

    for ((y = $TIMER ; y > 0 ; y -= 1)); do
      echo "Measurement $x/$MEASUREMENT_REPETITIONS completed in $y seconds."
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
    printf "\n"
    sleep 1
    if ps -p ${MEASUREMENT_SCRIPTS_PID[*]};
      then
        kill ${MEASUREMENT_SCRIPTS_PID[*]}
    fi

    # Save this measurement's data to special folder
    mkdir -p $DATA_SOURCE_PATH/$MEASUREMENT_REPETITIONS
    mv $RAW_DATA_SOURCE_PATH/* $DATA_SOURCE_PATH/$MEASUREMENT_REPETITIONS/

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
}

function plot
{
  ## Plot the results
  printf "\nNow processing results..."

  # Call the plotting scripts as data
  echo "Starting to generate plots..."
  for $j in ${PLOT_SCRIPTS[@]}; do
    bash -c "python ${$PLOT_PY_PATH/$j} &"
  done
  sleep 1

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
}
trap cleanup EXIT SIGHUP SIGINT SIGKILL;

function main
{
  # Prepare Measurement
  prepare_measurement

  #Take measurements
  measure

  # Create plot if desired
  if [ $PLOT_ENABLED -eq 1 ]; then plot; fi
}

main
