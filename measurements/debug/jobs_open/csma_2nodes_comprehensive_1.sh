# measurement 29
# protocol: csma two way handshake
# measured entity: throughput
# sifs = 1ms
# difs = 5ms
# backoff = 2ms
# nodes = 2

timer=15
export measurement_repetitions=2
measurement_scripts=( csma_80211_I.py csma_80211_II.py )
plot_scripts=( throughput.py rtt_2.py  )
#################################################
# first specify sender and then receiver output #
#################################################
export throughput_data_files="receiver_data_received.txt,sender_ack_received.txt"
export rtt_data_files="sender_bfr_dq.txt,sender_ack_received.txt"
export retxs_data_files="sender_retransmissions.txt,sender_max_retransmissions.txt"
export retxs2_data_files="receiver_retransmissions.txt,receiver_max_retransmissions.txt"
export plot_type="pdf,cdf,boxplot,bar,line"
export show_plot_after_measurement=0
