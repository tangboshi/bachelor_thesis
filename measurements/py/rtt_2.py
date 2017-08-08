import numpy as np
import myplot
import os

import pdb

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
all_retxs = []
total_retxs = 0
txs_fails = 0
packet_loss_percent = []
avg_frame_txs = []

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
            print("retx: "+str(retxs))
    else:
        print(  "File "+retxs_path+" not found. \
                Assuming not reached in GR. Creating data for you...")
        for index in range(len(ack_received_times)):
            retxs += [0]

    all_retxs += retxs

    # Let's get rid of the silly out index out of range bug by simply discarding
    # the last frame in our calculations
    # This also fixes wrong packet loss rate.
    # Both bugs are due to the fact that the last ack might not be recevied when the
    # transmission is interrupted due to the timer running out.
    if len(data_sent_times) > len(ack_received_times) + sum(retxs):
        last_frame_retxs = retxs[-1]
        #print(last_frame_retxs+1)
        data_sent_times = data_sent_times[:-(last_frame_retxs+1)]

    # Calculate RTT for each packet
    if rtt_mode == "rtt":
        for idx, counter in enumerate(retxs):
            # This check must be added to catch the case where the last data
            # frame isnt followed up by an ACK (max retries)
            if len(ack_received_times) > idx:
                total_retxs += counter
                if counter > 0:
                    if counter == max_retxs:
                        # Probably not needed, but hey if we can get it for free...
                        txs_fails += 1
                else:
                    res = ack_received_times[idx] - data_sent_times[idx+total_retxs]
                    rtt_single_measurement += [round(res,5)]
            else:
                print(  "Last data frame wasnt acked (max tries). \
                        Termintating calculation here.")

    else:#rtt_mode == delay
        for idx, counter in enumerate(retxs):
            if len(ack_received_times) > idx:
                total_retxs += counter
                if counter < max_retxs:
                    # ! ! !  "HACK"
                    if len(data_sent_times) >= idx+total_retxs-1:
                        res = ack_received_times[idx] - data_sent_times[idx+total_retxs]
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
    if len(rtt_single_measurement) > 0:
        rtt_single_mean =   float(sum(rtt_single_measurement))/len(rtt_single_measurement)
    else:
        rtt_single_mean =   100
    # rtt_single_mean seems to be calculated correctly, but source data is odd.
    print("\nThe resulting mean RTT of this single measurement is:")
    print(rtt_single_mean)
    print("\n")

    rtt[i-1] = rtt_single_mean

    ### Packet loss ###
    packet_loss_abs = float( len(data_sent_times) - len(ack_received_times) )
    packet_loss_rel = float( packet_loss_abs / len(data_sent_times) )
    packet_loss_percent += [round(packet_loss_rel*100, 2)]
    print("abs. packet loss: "+str(packet_loss_abs))
    print("packet loss in %: "+str(packet_loss_percent[-1])+"%")

    ### Average retransmissions per frame ###
    ### practically the same  as packet loss
    if not sum(retxs) == 0 and not len(retxs) == 0:
        avg_frame_txs += [sum(retxs) / len(retxs)]

    # Prepare next iteration
    rtt_single_measurement = []
    ack_received_times = []
    data_sent_times = []
    retxs = []
    total_retxs = 0
    txs_fails = 0

print(rtt)
#------------------------------------------------------------------------------#

for index, plot in enumerate(plot_type):

    myplot.myplot(data=rtt,
            bins=np.arange(
                min(rtt)-0.002,
                max(rtt)+0.002,
                #0.07/1000),
                0.07/100),
            plottype=plot,
            title="RTT",
            xlabel="rtt [s]",
            ylabel="rtt [s]",
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)

    myplot.myplot(data=packet_loss_percent,
            bins=np.arange(
                0,
                100,
                1),
            plottype=plot,
            title="Packet Loss",
            xlabel="packet loss [%]",
            ylabel="packet loss [%]",
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)

    if len(all_retxs) <= 20:
        number_bars = True
    else:
        number_bars = False

    myplot.myplot(data=all_retxs,
            bins=np.arange(
                0,
                max_retxs+1,
                0.1),
            plottype=plot,
            title="Retransmissions",
            xlabel="retransmissions",
            ylabel="retransmissions",
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot,
            number_bars=number_bars)
