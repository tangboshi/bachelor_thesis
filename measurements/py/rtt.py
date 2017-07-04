import numpy as np
import os

print("Hello from rtt.py!")

## Get all required information from OS
try:
    from variables import (
        data_source_path,
        data_source_files,
        plot_path,
        plot_type,
        measurement,
        repetitions,
        show_plot
    )
except ImportError:
    print("Probably not all data were imported correctly.")

# ------------------------------ Calculations ---------------------------------#
# Create a repetitions X 1 matrix aka row vector with measurement data
data = np.zeros(shape=(repetitions))

for i in range(1,repetitions+1):
    data_sent_path       =   data_source_path+'/'+str(i)+'/'+data_source_files[0]
    ack_received_path    =   data_source_path+'/'+str(i)+'/'+data_source_files[1]

    with open(data_sent_path) as f
        data_sent_raw      =   f.readlines()
    with open(ack_received_path) as f
        ack_received_raw   =   f.readlines()

    data_sent_times     = [x.strip('\n') for x in data_sent_raw]
    ack_received_times  = [x.strip('\n') for x in ack_received_raw]

    rtt[i-1] = ack_received_times[i-1] - data_sent_times[i-1]
print(data)
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

    myplot.myplot(  data=data,
            bins=repetitions,
            plottype=plot,
            title="RTT "+titles[plot],
            xlabel=xlabels[plot],
            ylabel=ylabels[plot],
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)
