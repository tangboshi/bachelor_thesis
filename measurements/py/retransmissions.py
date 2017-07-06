import numpy as np
import lines
import os

try:
    from variables import (
        data_source_path,
        retransmission_data_files,
        plot_path,
        plot_type,
        measurement,
        repetitions,
        show_plot
    )
except ImportError:
    print("Probably not all variables were loaded correctly.")

# ------------------------------ Calculations ---------------------------------#
# Create a repetitions X 1 matrix aka row vector with measurement data
data = np.zeros(shape=(repetitions))
data_sent_times = []
ack_received_times = []

# Calculate retransmitted
for i in range(1,repetitions+1):
    path                = data_source_path+'/'+str(i)+'/'
    data_sent_path      = path+retransmissions_data_files["data_sent"]
    data_resent_path    = path+retransmissions_data_files["data_resent"]

    with open(data_sent_path) as f:
        for line in f:
            line = line.strip('\n')
            line = line.replace(' ', '.')
            data_sent_times.append(float(line))

    with open(ack_received_path) as f:
        for line in f:
            line = line.strip('\n')
            line = line.replace(' ', '.')
            ack_received_times.append(float(line))

    rtt[i-1] = ack_received_times[i-1] - data_sent_times[i-1]

# Calculate # of retransmission tries per frame

print(data)
#------------------------------------------------------------------------------#

for index, plot in enumerate(plot_type):

    xlabels = {
        "cdf":      "retransmissions",
        "pdf":      "retransmissions",
        "boxplot":  "retransmissions"
    }

    ylabels = {
        "pdf":      "",
        "cdf":      "",
        "boxplot":  ""
    }

    titles = {
        "pdf":      "PDF",
        "cdf":      "CDF",
        "boxplot":  "Boxplot"
    }

    myplot.myplot(  data=data,
            bins=repetitions,
            plottype=plot,
            title="RTT "+titles[plot],
            xlabel=xlabels[plot],
            ylabel=ylabels[plot],
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)
