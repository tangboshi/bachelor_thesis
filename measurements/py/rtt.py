import numpy as np
import myplot
import os

print("Hello from rtt.py!")

## Get all required information from OS
try:
    from variables import (
        data_source_path,
        rtt_data_files,
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
data = np.zeros(shape=(repetitions))
data_sent_times = np.zeros(shape=(repetitions))
ack_received_times = np.zeros(shape=(repetitions))
rtt_single_measurement = []
rtt = np.zeros(shape=(repetitions))
rtt_single_measurement = []

for i in range(1,repetitions+1):
    path                = data_source_path+'/'+str(i)+'/'
    data_sent_path      = path+rtt_data_files["data_sent"]
    ack_received_path   = path+rtt_data_files["ack_received"]

    # Calculate RTT for each packet
    with open(data_sent_path) as f:
        for line in f:
            line = line.strip('\n')
            line = line.replace(' ', '.')
            data_sent_times = np.append(data_sent_times, float(line))
            print("data_sent: "+line)

    with open(ack_received_path) as f:
        for line in f:
            line = line.strip('\n')
            line = line.replace(' ', '.')
            ack_received_times = np.append(ack_received_times, float(line))
            print("ack_received: "+line)

    # If I wanted I could now plot packet loss as well...
    packet_loss_abs = float( len(data_sent_times) - len(ack_received_times) )
    packet_loss_rel = float( packet_loss_abs / len(data_sent_times) )
    packet_loss_percent = str((packet_loss_rel*100))+"%"
    print("packet loss in %: "+packet_loss_percent)

    for index, ack_time in enumerate(ack_received_times):
        res = ack_time - data_sent_times[index]
        rtt_single_measurement = np.append(rtt_single_measurement, res)

    # Now calculate mean RTT for this measurement
    rtt_single_measurement_mean = np.mean(rtt_single_measurement)
    rtt[i-1] = rtt_single_measurement_mean
print(rtt)
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
