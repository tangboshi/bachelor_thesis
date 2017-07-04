# Measurement 29
# protocol: csma two way handshake
# Measured entity: throughput
# SIFS = 1ms
# DIFS = 5ms
# BACKOFF = 2ms
# nodes = 2

TIMER=4
export MEASUREMENT_REPETITIONS=3
MEASUREMENT_SCRIPTS=( csma_80211_II_1.py csma_80211_I.py )
PLOT_SCRIPTS=( throughput.py rtt.py )
#################################################
# first specify sender and then receiver output #
#################################################
export RTT_DATA_FILES="sender_times.txt,sender_ack_received_times"
export PLOT_TYPE="pdf,cdf"
export SHOW_PLOT_AFTER_MEASUREMENT=1
