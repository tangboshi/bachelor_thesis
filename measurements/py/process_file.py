#from variables import *
import numpy as np
import lines

# import subprocess
# import os
# source = os.path.dirname(__file__)
# parent = os.path.join(source, '../')
# script_path = os.path.join(parent, 'measurement.conf')
#
# subprocess.run([script_path], stdout=subprocess.PIPE)
#



print("Hello from process_file.py");

'''
Note that this script only generates a single data point each time it is called.
Thus self.files represents an array of files (paths) that is required to
calculate a SINGLE data point.
'''

class process_file:
    def __init__(self, files, mode):
        self.files = files

        modes = {
            "througput":    lambda: self.throughput(),
            "rtt":          lambda: self.rtt()
        }

        return modes[mode]()

    def throughput(self):
        lines = linecount(self.files[0])
        return lines*packet_size

    def rtt(self):
        data = []
        data_sent_times = []
        ack_received_times = []
        rtt_single_measurement = []

        # Calculate RTT for each packet
        with open(self.files[0]) as f:
            for line in f:
                line = line.strip('\n')
                line = line.replace(' ', '.')
                data_sent_times += [float(line)]
                print("data_sent: "+line)

        with open(self.files[1]) as f:
            for line in f:
                line = line.strip('\n')
                line = line.replace(' ', '.')
                ack_received_times += [float(line)]
                print("ack_received: "+line)

        # If I wanted I could now plot packet loss as well...
        packet_loss_abs = float(len(data_sent_times) - len(ack_received_times))
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
        rtt_single_mean =   float(sum(rtt_single_measurement))/ \
                            len(rtt_single_measurement)
        # rtt_single_mean seems to be calculated correctly,
        # but source data is odd.
        # print("\nThe resulting mean RTT of this single measurement is:")
        # print(rtt_single_mean)
        # print("\n")

        return rtt_single_mean
