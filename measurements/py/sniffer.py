import numpy as np
import myplot
import os

print("Hello from sniffer.py!")

class sniffer:
    def __init__(self, **kwargs):
        self.data_source_path           =   kwargs.get("data_source_path","/home/alex/0_ba/git/measurements/data")
        self.rtt_data_files             =   kwargs.get("rtt_data_files", ["sender_bfr_dq.txt","sender_ack_received.txt"])
        self.plot_path                  =   kwargs.get("plot_path","/home/alex/0_ba/git/measurements/plots")
        self.plot_type                  =   kwargs.get("plot_type","all")
        self.measurement                =   kwargs.get("measurement",[])
        self.repetitions                =   kwargs.get("repetitions",5)
        self.show_plot                  =   kwargs.get("show_plot","False")
        self.max_retxs                  =   kwargs.get("max_retxs",6)
        self.retxs_data_files           =   kwargs.get("retxs_data_files",["sender_retransmissions"])
        self.timer                      =   kwargs.get("timer",300)
        self.grid                       =   kwargs.get("grid",False)
        self.legend                     =   kwargs.get("legend", [])
        self.xticks                     =   kwargs.get("xticks", [])
        self.legend_loc                 =   kwargs.get("legend_loc", "best")
        self.annotations_below          =   kwargs.get("annotations_below", [])
        self.annotations_other          =   kwargs.get("annotations_other", [])
        self.legend_coordinates         =   kwargs.get("legend_coordinates", False)
        self.create_plots               =   kwargs.get("create_plots", True)
        self.links                      =   kwargs.get("links", [1 for x in range(len(self.measurement))])
        self.eval_mode                  =   kwargs.get("eval_mode", "belated")
        self.channel_occupation_mode    =   kwargs.get("channel_occupation_mode", {"occupation_mode": ["overview, zoom"], "zoom": [5,6]})
        self.co_data_files              =   kwargs.get("co_data_files", ["sender_bfr_dq.txt","receiver_ack_sent.txt","sniffer"])
        self.sniffer_data_files         =   kwargs.get("sniffer_data_files", ["sniffer"])
        self.sniffer_settings           =   kwargs.get("sniffer_settings", {"link":2})

        # debugging:
        self.calc()
        self.plot()

    def calc(self):
        print("self.measurement")
        print(self.measurement)
        print("self.repetitions")
        print(self.repetitions)

        sniffer_times           = []
        sniffer_energy_levels  = []


        # FIXME: let's try to avoid this repetition of code from rtt! (until ###)
        for index,single_measurement in enumerate(self.measurement):
            energy_detected_times = []
            energy_levels = []

            for i in range(self.repetitions):
                path                = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                sniffer_data_path   = path+self.sniffer_data_files[0]+".txt"

                if os.path.isfile(sniffer_data_path):
                    with open(sniffer_data_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            secs, usecs, energy = line.split(" ",2)
                            missing_zeros = 6 - len(usecs)
                            usecs = ("0" * missing_zeros) + usecs
                            time = ".".join([secs, usecs])
                            energy_detected_times   += [float(time)]
                            energy_levels          += [float(energy)]
                            #print("data_sent: "+line)
                else:
                    print(  "File "+sniffer_data_path+" not found. \
                            Assuming not reached in GR.")
                    # Preventing these arrays from being empty to prevent wrong
                    # depiction of results
                    sniffer_times           += [0.0]
                    # for debugging purpse choose unreasonable number
                    sniffer_energy_levels   += [-1.0]

            sniffer_times           += energy_detected_times
            sniffer_energy_levels   += energy_levels
        # ###

        print("len(sniffer_times):")
        print(len(sniffer_times))
        print("sniffer_times:")
        #print(sniffer_times)
        print("sniffer_energy_levels:")
        #print(sniffer_energy_levels)

        ## FIXME: post processing
        ## FIXME: fix possible energy chart not covering gantt chart property
        # remove UNIX time offset:
        offset = float(sniffer_times[0])
        sniffer_times = [time-offset for time in sniffer_times]
        # post-processing variables
        # unit: seconds
        # maximum time difference of energies that belong to the same packet
        time_threshold = 0.003

        # Set energy level of two points to zero if they are too far from each other
        for index,item in enumerate(sniffer_times):
            if index+1 < len(sniffer_times):
                if sniffer_times[index+1] - sniffer_times[index] > time_threshold:
                    sniffer_energy_levels[index]    = 0
                    sniffer_energy_levels[index+1]  = 0

        # Onto data cropping...
        # TEMP: determine zoom invterval, if zoom mode is interval
        tmp, tmp2, tmp3, tmp4 = [], [], [], []

        if self.sniffer_settings["zoom_mode"] == "interval":
            zoom_interval = self.sniffer_settings["zoom_interval"]
            interval_lower_bound = self.sniffer_settings["zoom"][0]
            interval_upper_bound = interval_lower_bound+zoom_interval

            for index,time in enumerate(sniffer_times):
                if time >= interval_lower_bound:
                    print("time:"+str(time)+" exceeds lower bound.")
                    if time > interval_upper_bound:
                        print("time:"+str(time)+" exceeds upper bound.")
                        if tmp and tmp2:
                            tmp3.append(tmp)
                            tmp4.append(tmp2)
                        tmp, tmp2 = [], []
                        if interval_upper_bound < self.sniffer_settings["zoom"][1]:
                            interval_lower_bound = interval_upper_bound
                            interval_upper_bound += zoom_interval
                    else:
                        print("time:"+str(time)+" within bounds.")
                        tmp.append(time)
                        tmp2.append(sniffer_energy_levels[index])
            sniffer_times           = tmp3
            sniffer_energy_levels   = tmp4

        else:
            for index,time in enumerate(sniffer_times):
                if time > self.sniffer_settings["zoom"][0]:
                    if time > self.sniffer_settings["zoom"][1]:
                        break;
                    else:
                        tmp.append(time)
                        tmp2.append(sniffer_energy_levels[index])
            sniffer_times=tmp
            sniffer_energy_levels=tmp2

        self.sniffer_data = {
            "sniffer_energy_levels":    sniffer_energy_levels,
            "sniffer_times":            sniffer_times
        }
        print("self.sniffer_data:")
        print(self.sniffer_data)

        # Smoothing algorithm
        if "smoothed" in self.sniffer_settings["sniffer_mode"]:
            tmp, tmp2, tmp3, tmp4, deltas_x, deltas_y = [], [], [], [], [], []
            for interval_index,interval in enumerate(sniffer_energy_levels):
                for index,value in enumerate(interval):
                    if index+1 < len(sniffer_times):
                        delta_y = abs(interval[index+1] - value)
                        delta_x = abs(sniffer_times[interval_index][index+1] - sniffer_times[interval_index][index])
                        deltas_x.append(delta_x)
                        deltas_y.append(delta_y)
                        if (delta_y < self.sniffer_settings["smoothing_difference"]
                            and delta_y/delta_x < self.sniffer_settings["smoothing_derivative"]
                            or value == 0
                            or (value > self.sniffer_settings["smoothing_range"][0] and value < self.sniffer_settings["smoothing_range"][1])):
                            tmp.append(value)
                            tmp2.append(sniffer_times[interval_index][index])
                        else:
                            continue
                tmp3 += [tmp]
                tmp4 += [tmp2]

            #get experimental values from printout of this
            #comment to make the program faster...
            print("difference lower bound:"+str(min([x for x in deltas_y if x != 0])))
            print("difference upper bound:"+str(max(deltas_y)))
            print("derivative lower bound:"+str(min([x for x in deltas_y if x != 0])/max(deltas_x)))
            print("derivative upper bound:"+str(max(deltas_y)/min(deltas_x)))

            sniffer_energy_levels = tmp3
            sniffer_times = tmp4

            print("len(sniffer_energy_levels) (smoothed):")
            print(len(tmp3))
            print("len(sniffer_times) (smoothed):")
            print(len(tmp4))
            print("sniffer_energy_levels (smoothed):")
            print(tmp3)
            print("sniffer_times (smoothed):")
            print(tmp4)

            self.sniffer_smoothed_data = {
                "sniffer_energy_levels":    sniffer_energy_levels,
                "sniffer_times":            sniffer_times
            }

    def plot(self):

        print("Let's plot.")

        if  (self.create_plots == True
            or self.create_plots["sniffer"] == True
            and "physical" in self.sniffer_settings["sniffer_mode"]):
            for index,interval in enumerate(self.sniffer_data["sniffer_times"]):
                myplot.myplot(data=self.sniffer_data["sniffer_energy_levels"][index],
                        data_x=interval,
                        plottype=["line_xy"],
                        title="Channel Energy Level "+str(index),
                        xlabel="time [s]",
                        ylabel="energy [PU]",
                        savepath=self.plot_path+"/",
                        show=self.show_plot,
                        grid=self.grid,
                        xticks=self.xticks,
                        legend=self.legend,
                        legend_loc=self.legend_loc,
                        annotations_below=self.annotations_below,
                        annotations_other=self.annotations_other,
                        legend_coordinates=self.legend_coordinates["sniffer"],
                        eval_mode=self.eval_mode,
                        timer=self.timer,
                        repetitions=self.repetitions,
                        xlims=self.sniffer_settings["zoom"])

        if  (self.create_plots == True
            or self.create_plots["sniffer"] == True
            and "smoothed" in self.sniffer_settings["sniffer_mode"]):
            for index,interval in enumerate(self.sniffer_data["sniffer_times"]):
                myplot.myplot(data=self.sniffer_smoothed_data["sniffer_energy_levels"][index],
                        data_x=interval,
                        plottype=["line_xy"],
                        title="Smoothed Channel Energy Level "+str(index),
                        xlabel="time [s]",
                        ylabel="energy [PU]",
                        savepath=self.plot_path+"/",
                        show=self.show_plot,
                        grid=self.grid,
                        xticks=self.xticks,
                        legend=self.legend,
                        legend_loc=self.legend_loc,
                        annotations_below=self.annotations_below,
                        annotations_other=self.annotations_other,
                        legend_coordinates=self.legend_coordinates["sniffer"],
                        eval_mode=self.eval_mode,
                        timer=self.timer,
                        repetitions=self.repetitions,
                        xlims=self.sniffer_settings["zoom"])
