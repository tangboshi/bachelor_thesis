import numpy as np
import myplot
import os

print("Hello from rtt.py!")

## Get all required information from OS
try:
    from variables import (
        data_source_path,
        rtt_data_files,
        rtt_mode,
        plot_path,
        plot_type,
        measurement,
        repetitions,
        show_plot,
        max_retxs,
        retxs_data_files
    )
except ImportError:
    print("Probably not all data were imported correctly!")

# ------------------------------ Calculations ---------------------------------#
# Create a repetitions X 1 matrix aka row vector with measurement data
data_sent_times = []
ack_received_times = []
rtt_single_measurement = []
rtt = np.zeros(shape=(repetitions))
retxs = []
total_retxs = 0
tx_fails = 0

for i in range(1,repetitions+1):
    path                = data_source_path+'/'+str(i)+'/'
    data_sent_path      = path+rtt_data_files["data_sent"]
    ack_received_path   = path+rtt_data_files["ack_received"]
    retxs_path          = path+retxs_data_files["retxs"]

    if os.path.isfile(data_sent_path):
        with open(data_sent_path) as f:
            for line in f:
                line = line.strip('\n')
                secs, usecs = line.split(" ",1)
                missing_zeros = 6 - len(usecs)
                usecs = ("0" * missing_zeros) + usecs
                line = ".".join([secs, usecs])
                data_sent_times += [float(line)]
                print("data_sent: "+line)
    else:
        print(  "File "+data_sent_path+" not found. \
                Assuming not reached in GR.")

    if os.path.isfile(ack_received_path):
        with open(ack_received_path) as f:
            for line in f:
                line = line.strip('\n')
                secs, usecs = line.split(" ",1)
                missing_zeros = 6 - len(usecs)
                usecs = ("0" * missing_zeros) + usecs
                line = ".".join([secs, usecs])
                ack_received_times += [float(line)]
                print("ack_received: "+line)

    else:
        print(  "File "+ack_received_path+" not found. \
                Assuming not reached in GR.")

    if os.path.isfile(retxs_path):
        with open(retxs_path) as f:
            for line in f:
                line.strip("\n")
                line = [int(item) for item in line.split()]
                retxs += [item for item in line]
                print("retx: "+retxs)

    else:
        print(  "File "+retxs_path+" not found. \
                Assuming not reached in GR. Creating data for you...")
        for index in range(ack_received_times):
            retxs += [0]


    # Calculate RTT for each packet
    if rtt_mode == "rtt":
        for idx, counter in enumerate(retxs):
            # This check must be added to catch the case where the last data
            # frame isnt followed up by an ACK (max retries)
            if len(ack_received_times) > idx:
                total_retxs += counter
                if counter > 0:
                    if counter == max_retxs:
                        txs_fails += 1
                else:
                    res = ack_received_times[idx] - data[idx+counter+total_retxs]
                    rtt_single_measurement += [round(res,5)]
            else:
                print(  "Last data frame wasnt acked (max tries). \
                        Termintating calculation here.")

    else:#rtt_mode == delay
        for idx, counter in enumerate(retxs):
            if len(ack_received_times) > idx:
                total_retxs += counter
                if counter < max_retxs:
                    res = ack_received_times[idx] - data[idx+counter+total_retxs]
                    rtt_single_measurement += [round(res,5)]
                else:
                    # Probably not needed, but hey if we can get it for free...
                    txs_fails += 1
            else:
                print(  "Last data frame wasnt acked (max tries). \
                        Termintating calculation here.")


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
    retxs = []
    total_retxs = 0
    tx_fails = 0

    ### Packet loss ###
    packet_loss_abs = float( len(data_sent_times) - len(ack_received_times) )
    packet_loss_rel = float( packet_loss_abs / len(data_sent_times) )
    packet_loss_percent = str((round(packet_loss_rel*100, 2)))+"%"
    print("abs. packet loss: "+str(packet_loss_abs))
    print("packet loss in %: "+packet_loss_percent)

print(rtt)
#------------------------------------------------------------------------------#

for index, plot in enumerate(plot_type):

    xlabels = {
        "cdf": "rtt",
        "pdf": "rtt",
        "boxplot": "",
        "bar": "",
        "line": ""
    }

    ylabels = {
        "pdf": "",
        "cdf": "",
        "boxplot": "rtt",
        "bar":  "rtt",
        "line": "rtt"
    }

    titles = {
        "pdf":  "PDF",
        "cdf":  "CDF",
        "boxplot": "boxplot",
        "bar":  "bar chart",
        "line": "line chart"
    }

    myplot.myplot(data=rtt,
            bins=np.arange(
                min(rtt)-0.002,
                max(rtt)+0.002,
                #0.07/1000),
                (max(rtt)-min(rtt))/100),
            plottype=plot,
            title="RTT "+titles[plot],
            xlabel=xlabels[plot],
            ylabel=ylabels[plot],
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)
