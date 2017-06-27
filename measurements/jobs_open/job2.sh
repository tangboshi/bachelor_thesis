TIMER=1
export MEASUREMENT_REPETITIONS=3
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
