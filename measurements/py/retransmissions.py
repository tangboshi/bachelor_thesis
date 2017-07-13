import numpy as np
import myplot
import os

print("Hello from retransmissions.py!")

## Get all required information from OS
try:
    from variables import (
        data_source_path,
        retxs_data_files,
        retxs2_data_files,
        plot_path,
        plot_type,
        measurement,
        repetitions,
        show_plot
    )
except ImportError:
    print("Probably not all data were imported correctly!")

# ------------------------------ Calculations ---------------------------------#
# Create a repetitions X 1 matrix aka row vector with measurement data
data = []
data_retxs = []
data_max_retxs = []
ack_retxs = []
ack_max_retxs = []

for i in range(1, repetitions+1):
    path                 = data_source_path+'/'+str(i)+'/'
    data_retxs_path      = path+retxs_data_files["rtxs"]
    data_max_retxs_path  = path+retxs_data_files["max_rtxs"]
    ack_retxs_path       = path+retxs2_data_files["rtxs"]
    ack_max_retxs_path   = path+retxs2_data_files["max_rtxs"]

    file_list = [
        data_retxs_path,
        data_max_retxs_path,
        ack_retxs_path,
        ack_max_retxs_path
    ]

    for index, data_file in enumerate(file_list):
        if os.path.isfile(data_file):
            with open(data_file) as f:
                for line in f:
                    line.strip("\n")
                    data[index] = map(int, line.split(" "))
        else:
            data[index] = [0]

#------------------------------------------------------------------------------#

for index, plot in enumerate(plot_type):

    xlabels = {
        "cdf": "rtt",
        "pdf": "rtt"
    }

    ylabels = {
        "pdf": "",
        "cdf": ""
    }

    titles1 = {
        0: "Data Retransmissions",
        1: "Data Max Retransmissions",
        2: "Ack Retransmissions",
        3: "Ack Max Retransmissions"
    }

    titles2 = {
        "pdf":  "PDF",
        "cdf":  "CDF",
        "boxplot": "boxplot",
        "bar": "bar chart"
    }

    plot_data = [ data[0], data[1], data[2], data[3] ]

    for index, data_set in enumerate(plot_data):
        myplot.myplot(  data=data_set,
                bins=np.arange(
                    min(data_set)-1,
                    max(data_set)+1,
                    (max(data_set)-min(data_set))/25),
                plottype=plot,
                title=titles1[index]+titles2[plot],
                xlabel=xlabels[plot],
                ylabel=ylabels[plot],
                savepath=plot_path+"/"+measurement+"/",
                show=show_plot)
