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
        with open(data_file) as f:
            for line in f:
                line.strip("\n")
                 = line.split(" ")

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

    titles = {
        "pdf":  "PDF",
        "cdf":  "CDF"
    }

    myplot.myplot(  data=rtt,
            bins=np.arange(
                min(rtt)-0.002,
                max(rtt)+0.002,
                (max(rtt)-min(rtt))/25,
            plottype=plot,
            title="retransmissions (data)"+titles[plot],
            xlabel=xlabels[plot],
            ylabel=ylabels[plot],
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)

    myplot.myplot(  data=rtt,
            bins=np.arange(
                min(rtt)-0.002,
                max(rtt)+0.002,
                0.07/1000),
            plottype=plot,
            title="retransmissions (acks)"+titles[plot],
            xlabel=xlabels[plot],
            ylabel=ylabels[plot],
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)
