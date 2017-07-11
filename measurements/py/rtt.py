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
data_sent_times = []
ack_received_times = []
rtt_single_measurement = []
rtt = np.zeros(shape=(repetitions))

for i in range(1,repetitions+1):
    path                = data_source_path+'/'+str(i)+'/'
    data_sent_path      = path+rtt_data_files["data_sent"]
    ack_received_path   = path+rtt_data_files["ack_received"]

    # Calculate RTT for each packet
    with open(data_sent_path) as f:
        for line in f:
            line = line.strip('\n')
            secs, usecs = line.split(" ",1)
            missing_zeros = 6 - len(usecs)
            usecs = ("0" * missing_zeros) + usecs
            line = ".".join([secs, usecs])
            data_sent_times += [float(line)]
            print("data_sent: "+line)

    with open(ack_received_path) as f:
        for line in f:
            line = line.strip('\n')
            secs, usecs = line.split(" ",1)
            missing_zeros = 6 - len(usecs)
            usecs = ("0" * missing_zeros) + usecs
            line = ".".join([secs, usecs])
            ack_received_times += [float(line)]
            print("ack_received: "+line)

    # If I wanted I could now plot packet loss as well...
    packet_loss_abs = float( len(data_sent_times) - len(ack_received_times) )
    packet_loss_rel = float( packet_loss_abs / len(data_sent_times) )
    packet_loss_percent = str((round(packet_loss_rel*100, 2)))+"%"
    print("packet loss in %: "+packet_loss_percent)

    for index, ack_time in enumerate(ack_received_times):
        res = ack_time - data_sent_times[index]
        rtt_single_measurement += [round(res,5)]

    print("\nThe resulting RTTs of this single measurement are:")
    print(rtt_single_measurement)
    print("\n")

    # Now calculate mean RTT for this measurement
    # print(str(float(sum(rtt_single_measurement))))
    # print(str(len(rtt_single_measurement)))
    rtt_single_mean =   float(sum(rtt_single_measurement))/len(rtt_single_measurement)
    # rtt_single_mean seems to be calculated correctly, but source data is odd.
    print("\nThe resulting mean RTT of this single measurement is:")
    print(rtt_single_mean)
    print("\n")

    rtt[i-1] = rtt_single_mean

    # Prepare next iteration
    rtt_single_measurement = []
    ack_received_times = []
    data_sent_times = []

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
            bins=np.arange(
                min(data),
                max(data),
                2),
            plottype=plot,
            title="RTT "+titles[plot],
            xlabel=xlabels[plot],
            ylabel=ylabels[plot],
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)
