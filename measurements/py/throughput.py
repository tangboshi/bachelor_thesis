import numpy as np
import subprocess
import myplot
import os.path as pt
import lines

print("Hello from throughput.py!")

# Let's import all data we need
#try:
from variables import (
    data_source_path,
    throughput_data_files,
    packet_size,
    plot_path,
    plot_type,
    measurement,
    repetitions,
    show_plot
)
#except ImportError:
    #print("Probably not all data were imported correctly.")

# ------------------------------ Calculations ---------------------------------#
# Create a repetitions X 1 matrix aka row vector with measurement data
data = np.zeros(shape=(repetitions))

for i in range(1,repetitions+1):
    file_path = data_source_path+'/'+str(i)+'/'
    data_file_path = file_path+throughput_data_files["receiver_data_received"]
    ack_file_path = file_path+throughput_data_files["sender_ack_received"]
    if pt.isfile(ack_file_path):
        ackcount = lines.linecount(ack_file_path)
    else:
        # no acks found
        print("ACK file not found at "+ack_file_path+".")
        ackcount = 0
        data[i-1] = 0
    if pt.isfile(data_file_path):
        datacount = lines.linecount(data_file_path)
        print("ackcount: "+str(ackcount))
        print("datacount: "+str(datacount))
        data[i-1] = min(ackcount, datacount)*packet_size
    else:
        # no data sent off
        print("Data file not found at "+data_file_path+".")
        datacount = 0
        data[i-1] = 0

print(data)
#------------------------------------------------------------------------------#

for index, plot in enumerate(plot_type):

    myplot.myplot(  data=data,
        bins=np.arange(
            min(data)-float(packet_size),
            max(data)+float(packet_size),
            (max(data)-min(data)+1)/25),
            #packet_size/25),
        plottype=plot,
        title="Throughput",
        xlabel="throughput [B]",
        ylabel="throughput [B]",
        savepath=plot_path+"/"+measurement+"/",
        show=show_plot)
