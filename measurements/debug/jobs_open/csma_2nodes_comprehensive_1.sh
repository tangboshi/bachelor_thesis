# Measurement 29
# protocol: csma two way handshake
# Measured entity: throughput
# SIFS = 1ms
# DIFS = 5ms
# BACKOFF = 2ms
# nodes = 2

TIMER=5
export MEASUREMENT_REPETITIONS=3
MEASUREMENT_SCRIPTS=( csma_80211_I.py csma_80211_II.py )
PLOT_SCRIPTS=( retransmissions.py )
#################################################
# first specify sender and then receiver output #
#################################################
export THROUGHPUT_DATA_FILES="receiver_data_received.txt"
export RTT_DATA_FILES="sender_bfr_dq.txt,sender_ack_received.txt"
export RETXS_DATA_FILES="sender_retransmissions.txt,sender_max_retransmissions.txt"
export RETXS2_DATA_FILES="receiver_retransmissions.txt,receiver_max_retransmissions.txt"
export PLOT_TYPE="pdf,cdf,boxplot,bar"
export SHOW_PLOT_AFTER_MEASUREMENT=1
