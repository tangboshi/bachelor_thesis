import os

print("Hello from variables.py!")

## Get all required information from OS

if os.environ.get('MEASUREMENT_COUNTER') is not None:
    measurement         = os.environ["MEASUREMENT_COUNTER"]
else:
    measurement         = -1

if os.environ.get('MEASUREMENT_REPETITIONS') is not None:
    repetitions         = int(os.environ["MEASUREMENT_REPETITIONS"])
else:
    repetitions         = -1

if os.environ.get('DATA_SOURCE_PATH') is not None:
    data_source_path    = os.environ["DATA_SOURCE_PATH"]+"/"+measurement
else:
    data_source_path    = "/home/inets/0_ba/bachelor_thesis/measurements/data"

if os.environ.get('PLOT_DIRECTORY_PATH') is not None:
    plot_path           = os.environ["PLOT_DIRECTORY_PATH"]
else:
    plot_path           = ""

if os.environ.get('PACKET_SIZE') is not None:
    packet_size         = int(os.environ["PACKET_SIZE"])
else:
    packet_size         = 1000

if os.environ.get('SHOW_PLOT_AFTER_MEASUREMENT') is not None:
    show_plot           = int(os.environ["SHOW_PLOT_AFTER_MEASUREMENT"])
else:
    show_plot           = True

if os.environ.get('PLOT_TYPE') is not None:
    plot_type           = os.environ["PLOT_TYPE"].split(",")
else:
    plot_type           = "debug"

if os.environ.get('MAX_RETXS') is not None:
    max_retxs           = os.environ["MAX_RETXS"]
else:
    max_retxs           = 6

#throughput
if os.environ.get('THROUGHPUT_DATA_FILES') is not None:
    throughput_data_files_array = os.environ["THROUGHPUT_DATA_FILES"].split(",")
    throughput_data_files = {
        "receiver_data_received": throughput_data_files_array[0]
    }
else:
    throughput_data_files = {
        "receiver_data_received": "invalid_file.txt"
    }

#RTT
if os.environ.get('RTT_DATA_FILES') is not None:
    rtt_data_files_array  = os.environ["RTT_DATA_FILES"].split(",")
    rtt_data_files = {
        "data_sent":    rtt_data_files_array[0],
        "ack_received": rtt_data_files_array[1]
    }
else:
    rtt_data_files = {
        "data_sent":    "invalid_file.txt",
        "ack_received": "invalid_file_2.txt"
    }

if os.environ.get('RTT_MODE') is not None:
    rtt_mode = os.environ['RTT_MODE']
else:
    #alternative rtt mode is delay, which takes retransmissions into account
    #when calculating rtt, which actually then rather should be called packet
    #delay
    rtt_mode = "rtt"

#retransmissions
#ugly to have two environment variables for this, but w/e
#gotta cover both acks and data, whatcha gonna do?
if os.environ.get('RETXS_DATA_FILES') is not None:
    retxs_data_files_array  = os.environ["RETXS_DATA_FILES"].split(",")
    retxs_data_files = {
        "retxs":       retxs_data_files_array[0],
        "max_retxs":   retxs_data_files_array[1]
    }
else:
    retxs_data_files = {
        "retxs":       "invalid_file.txt",
        "max_retxs":   "invalid_file_2.txt"
    }
if os.environ.get('RETXS2_DATA_FILES') is not None:
    retxs2_data_files_array  = os.environ["RETXS2_DATA_FILES"].split(",")
    retxs2_data_files = {
        "retxs":       retxs2_data_files_array[0],
        "max_retxs":   retxs2_data_files_array[1]
    }
else:
    retxs2_data_files = {
        "retxs":       "invalid_file.txt",
        "max_retxs":   "invalid_file_2.txt"
    }
