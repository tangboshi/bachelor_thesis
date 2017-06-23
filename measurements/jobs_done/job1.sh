echo "Hello from job1.sh"

export TIMER=2
export MEASUREMENT_REPETITIONS=9
export MEASUREMENT_SCRIPTS=( measure.py )
export MEASUREMENT_OUTPUT_FILES=( t1DQ.txt t1CS.txt t2RXe.txt t2e.txt )
export MEASUREMENT_OUTPUT_FILES=${MEASUREMENT_OUTPUT_FILES[*]}
export PLOT_SCRIPTS=( cdf.py )
export PLOT_ENABLED=1
export PLOT_SAVE_ENABLED=1
export PLOT_NAMES_TRUNK=other_trunk
