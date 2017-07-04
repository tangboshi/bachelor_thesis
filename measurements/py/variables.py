import os

print("Hello from variables.py!")
## Get all required information from OS
measurement         = os.environ["MEASUREMENT_COUNTER"]
repetitions         = int(os.environ["MEASUREMENT_REPETITIONS"])
data_source_path    = os.environ["DATA_SOURCE_PATH"]+"/"+measurement
data_source_files   = os.environ["MEASUREMENT_OUTPUT_FILES"].split(",")
plot_path           = os.environ["PLOT_DIRECTORY_PATH"]
packet_size         = int(os.environ["PACKET_SIZE"])
show_plot           = int(os.environ["SHOW_PLOT_AFTER_MEASUREMENT"])
plot_type           = os.environ["PLOT_TYPE"].split(",")
