#!/bin/bash

source measurement.conf
echo "remote_measurement is set to "$remote_measurement"."

function setup_remote_connection
{
  reset
  # echo "setting up remote connection..."
  # if ( mount | grep $remote_measurement_mount_point  )
  # then
  #   echo "the mount point is in use, confirm unmount with your password."
  #   sudo umount $remote_measurement_mount_point
  # fi
  # echo "please enter the server password to mount the target directory."
  # mkdir -p $remote_measurement_mount_point
  #sshfs $remote_user@$remote_ip:$remote_to_mount_path $remote_measurement_mount_point
  #ssh -$remote_flags $remote_user@$remote_ip "$(typeset -f); main"
  sshpass -p "inets" ssh -$remote_flags $remote_user@$remote_ip "bash -s" < remote_measurement.sh
}

function prepare_measurement
{
    reset
    measurement_counter=0
    ## let's make sure all the directories exist
    printf "\nchecking if paths exists...\n"

    #let's first make absolutely sure the raw data source path exists
    if [ ! -d $raw_data_source_path ];
      then
        mkdir -p $raw_data_source_path
        echo $raw_data_source_path" created."
    fi

    if [ -d $plot_directory_path ];
      then
        echo $plot_directory_path" already existed!"
        cd $plot_directory_path
        # create measurement directory
        while [ -d $measurement_counter ]; do
            measurement_counter=$(($measurement_counter+1))
        done
        export measurement_counter;
    fi

    if [ -d $log_path ];
      then
        echo $log_path" already existed!"
      else
        mkdir -p $log_path
        echo $log_path" directory created."
    fi

    mkdir -p $plot_directory_path/$measurement_counter
    echo $plot_directory_path/$measurement_counter" directory created."

    mkdir -p $data_source_path/$measurement_counter
    echo $data_source_path/$measurement_counter" directory created."

    mkdir -p $jobs_open_path
    mkdir -p $jobs_done_path

    ## let's check if measurement script is defined
    # if $measurement_scripts undefined:
    # go through directory and list all python files
    if [ -z ${measurement_scripts+x} ];
      then
        echo  "no measurement scripts set,
              going through files inside of $locate_base_path."
        echo "please add a the full path of one of the files to \$scritps."
        #locate -r "$locate_base_path" | grep "\.py$"
        echo "terminated. ding dong"
        exit -1
    fi

    printf "\n"
}

function measure
{
  local prematurely_aborted=0

  for ((x = 1 ; x <= $measurement_repetitions ; x += 1)); do

    # get pid to later kill it
    for i in "${measurement_scripts[@]}"
    do
      python $measurement_script_path/$i &
      #measurement_scripts_pid+=($!)
    done

    for ((y = $timer ; y > 0 ; y -= 1)); do
      echo "measurement $x/$measurement_repetitions complete in $y second(s)."
      if [ $check_if_prematurely_aborted -eq 1 ];
        then
          if ps -p ${measurement_scripts_pid[*]};
            then
              :
            else
              prematurely_aborted=1
              echo  "scripts were killed prematurely.
                    measurement may be incomplete."
              break
          fi
      fi
      sleep 1
    done

    # kill scripts if running
    #sleep 1
    #if {ps -p ${measurement_scripts_pid[*]}} &>/dev/null;
    #  then
    #    kill ${measurement_scripts_pid[*]}
    #fi
    kill $(jobs -p)

    # save this measurement's data to special folder
    mkdir -p $data_source_path/$measurement_counter/$x
    echo  "measurement $x raw data directory created $data_source_path/$measurement_counter/$x/."
    mv -v $raw_data_source_path/* $data_source_path/$measurement_counter/$x/
    echo  "measurement $x raw data moved to $data_source_path/$measurement_counter/$x/."
    printf "\n"

    # will only ever be true if $check_if_prematurely_aborted is set to 1
    if [ $prematurely_aborted -eq 1 ];
      then
        if [ $plot_if_prematurely_aborted -eq 0 ];
          then
            echo "plotting if measurement prematurely aborted set to false."
            echo "terminated."
            exit -1
        fi
    fi

  done

  #exit remote connection
  if [ $remote_measurement -eq 1 ]; then
    exit
  fi
}

function plot
{
  ## plot the results
  echo "now processing results..."

  # call the plotting scripts as data
  #echo "starting to generate plots..."
  echo "plotting python should be: "$plot_py" ("$os")."

  for i in ${plot_scripts[@]}; do
    bash -c "$plot_py $plot_py_path/$i"
  done

  printf "\n"
  echo "+--------------------------------------------------------------+"
  echo "| plotting completed. until the next measurement session then! |"
  echo "+--------------------------------------------------------------+"
}

function cleanup
{
    ##cleaning up the mess you created!
    #kill all child proceesses
    echo "staring cleanup..."
    echo "killing all lingering child processes..."
    killall -9 -g $0
    cd $this_path
    exit
}
trap cleanup sighup sigint sigkill;
trap "cd $this_path" exit;

function main
{
  # clear up console
  #reset
  # check if jobs_open directory is empty
  if [ ! "$(ls -a $jobs_open_path)" ]; then
    echo "there seem to be no open jobs. measuring with default parameters."
    prepare_measurement
    #take measurements
    measure | tee -a $log_path/default_$measurement_counter.log
    # create plot if desired
    if [ $plot_enabled -eq 1 ]; then
      plot | tee -a $log_path/default_$measurement_counter.log; fi
  else
    prepare_measurement
    echo "open jobs detected! let's get to work..."
    jobs=$jobs_open_path/*
    for job in $jobs; do
      source $job;
      log=$log_path/$job_name"_"$measurement_counter.log
      job_name=$(echo $job | rev | cut -d"/" -f1 | rev )
      #echo $job_name
      $(cat $job) | tee -a $log
      $(cat measurement.conf) | tee -a $log
      measure | tee -a $log
      if [ $plot_enabled -eq 1 ]; then
        plot | tee -a $log
      fi
      if [ $move_after_job_done -eq 1 ]; then
        cp $job $plot_directory_path/$measurement_counter/
        mv $job $jobs_done_path/
      fi
      export measurement_counter=$((measurement_counter++))
    done
  fi

}

if [ $debug_mode -eq 1 ]; then
  printf "\n"
  echo "+-----------------------------------------------------------+"
  echo "| debug mode is active, results are saved in the debug dirs |"
  echo "+-----------------------------------------------------------+"
fi

if [ $remote_measurement -eq 1 ]; then
  # call to main included here
    setup_remote_connection
  else
    main
fi
