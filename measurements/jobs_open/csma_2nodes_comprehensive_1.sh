# Measurement 29
# protocol: csma two way handshake
# Measured entity: throughput
# SIFS = 1ms
# DIFS = 5ms
# BACKOFF = 2ms
# nodes = 2
TIMER=300
export MEASUREMENT_REPETITIONS=5
#################################################
# first specify sender and then receiver output #
#################################################
MEASUREMENT_OUTPUT_FILES=( sender_times.txt receiver_times.txt )
export MEASUREMENT_OUTPUT_FILES=${MEASUREMENT_OUTPUT_FILES[*]}
MEASUREMENT_SCRIPTS=( csma_80211_I.py csma_80211_II_2.py )
PLOT_SCRIPTS=( cdf_delay.py )

## Plot options
PLOT_ENABLED=1
export PLOT_SAVE_ENABLED=1
# The name of the saved files
export PLOT_NAMES_TRUNK=throughput
