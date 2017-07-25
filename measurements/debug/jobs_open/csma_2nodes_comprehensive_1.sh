echo protocol = csma two way handshake
echo sifs = 3ms
echo difs = 15ms
echo backoff = 6ms
echo nodes = 2
echo timer = 300
echo repetions = 5

export timer=300
export measurement_repetitions=5
measurement_scripts=( csma_80211_IV.py csma_80211_V.py )
plot_scripts=( rtt_2.py throughput.py )
#################################################
# first specify sender and then receiver output #
#################################################
export throughput_data_files="receiver_data_received.txt,sender_ack_received.txt"
export rtt_data_files="sender_bfr_dq.txt,sender_ack_received.txt"
export rtt_mode="frame_delay"
export retxs_data_files="sender_retransmissions.txt,sender_max_retransmissions.txt"
export retxs2_data_files="receiver_retransmissions.txt,receiver_max_retransmissions.txt"
export plot_type="pdf,cdf,boxplot,bar,line"
export show_plot_after_measurement=0
