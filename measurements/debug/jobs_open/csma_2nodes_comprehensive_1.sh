# Measurement 29
# protocol: csma two way handshake
# Measured entity: throughput
# SIFS = 1ms
# DIFS = 5ms
# BACKOFF = 2ms
# nodes = 2

TIMER=4
export MEASUREMENT_REPETITIONS=1
MEASUREMENT_SCRIPTS=( csma_80211_I.py csma_80211_II_1.py )
PLOT_SCRIPTS=( throughput.py rtt.py )
#################################################
# first specify sender and then receiver output #
#################################################
export MEASUREMENT_OUTPUT_FILES="sender_times.txt,receiver_times"
export PLOT_TYPE="pdf,cdf"
export SHOW_PLOT_AFTER_MEASUREMENT=1
