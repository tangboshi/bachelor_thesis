import os

print("hello from variables.py!")

## get all required information from os

if os.environ.get('measurement_counter') is not None:
    measurement         = os.environ["measurement_counter"]
else:
    measurement         = -1

if os.environ.get('measurement_repetitions') is not None:
    repetitions         = int(os.environ["measurement_repetitions"])
else:
    repetitions         = -1

if os.environ.get('data_source_path') is not None:
    data_source_path    = os.environ["data_source_path"]+"/"+measurement
else:
    data_source_path    = "/home/inets/0_ba/bachelor_thesis/measurements/data"

if os.environ.get('plot_directory_path') is not None:
    plot_path           = os.environ["plot_directory_path"]
else:
    plot_path           = ""

if os.environ.get('packet_size') is not None:
    packet_size         = int(os.environ["packet_size"])
else:
    packet_size         = 1000

if os.environ.get('show_plot_after_measurement') is not None:
    show_plot           = int(os.environ["show_plot_after_measurement"])
else:
    show_plot           = true

if os.environ.get('plot_type') is not None:
    plot_type           = os.environ["plot_type"].split(",")
else:
    plot_type           = "debug"

if os.environ.get('max_retxs') is not None:
    max_retxs           = os.environ["max_retxs"]
else:
    max_retxs           = 6

#throughput
if os.environ.get('throughput_data_files') is not None:
    throughput_data_files_array = os.environ["throughput_data_files"].split(",")
    throughput_data_files = {
        "receiver_data_received": throughput_data_files_array[0],
        "sender_ack_received": throughput_data_files_array[1]
    }
else:
    throughput_data_files = {
        "receiver_data_received": "invalid_file.txt",
        "sender_ack_received": "invalid_file_2.txt"
    }

#rtt
if os.environ.get('rtt_data_files') is not None:
    rtt_data_files_array  = os.environ["rtt_data_files"].split(",")
    rtt_data_files = {
        "data_sent":    rtt_data_files_array[0],
        "ack_received": rtt_data_files_array[1]
    }
else:
    rtt_data_files = {
        "data_sent":    "invalid_file.txt",
        "ack_received": "invalid_file_2.txt"
    }

if os.environ.get('rtt_mode') is not None:
    rtt_mode = os.environ['rtt_mode']
else:
    #alternative rtt mode is delay, which takes retransmissions into account
    #when calculating rtt, which actually then rather should be called packet
    #delay
    rtt_mode = "rtt"

#retransmissions
#ugly to have two environment variables for this, but w/e
#gotta cover both acks and data, whatcha gonna do?
if os.environ.get('retxs_data_files') is not None:
    retxs_data_files_array  = os.environ["retxs_data_files"].split(",")
    retxs_data_files = {
        "retxs":       retxs_data_files_array[0],
        "max_retxs":   retxs_data_files_array[1]
    }
else:
    retxs_data_files = {
        "retxs":       "invalid_file.txt",
        "max_retxs":   "invalid_file_2.txt"
    }
if os.environ.get('retxs2_data_files') is not None:
    retxs2_data_files_array  = os.environ["retxs2_data_files"].split(",")
    retxs2_data_files = {
        "retxs":       retxs2_data_files_array[0],
        "max_retxs":   retxs2_data_files_array[1]
    }
else:
    retxs2_data_files = {
        "retxs":       "invalid_file.txt",
        "max_retxs":   "invalid_file_2.txt"
    }
