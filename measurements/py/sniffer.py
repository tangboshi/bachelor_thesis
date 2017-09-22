import numpy as np
import myplot_belated as myplot
import os

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
                sniffer_data_path   = path+self.sniffer_data_files[0]+"_"+str(self.sniffer_settings["link"])+".txt"

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
        print(sniffer_times)
        print("sniffer_energy_levels:")
        print(sniffer_energy_levels)

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

        # Onto cropping the data... let's zoom into a specified area
        tmp, tmp2 = [], []
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

            tmp, tmp2 = [], []
            for index,value in enumerate(sniffer_energy_levels):
                if index+1 < len(sniffer_times):
                    delta_y = sniffer_energy_levels[index+1] - value
                    delta_x = sniffer_times[index+1] - sniffer_times[index]
                    if (delta_y < self.sniffer_settings["smoothing_difference"]
                        or delta_y/delta_x < self.sniffer_settings["smoothing_derivative"] ):
                        tmp.append(value)
                        tmp2.append(sniffer_times[index])
                    else:
                        continue
            sniffer_energy_levels = tmp
            sniffer_times = tmp2

            self.sniffer_smoothed_data = {
                "sniffer_energy_levels":    sniffer_energy_levels,
                "sniffer_times":            sniffer_times
            }

    def plot(self):

        print("Let's plot.")

        if  (self.create_plots == True
            or self.create_plots["sniffer"] == True
            and "physical" in self.sniffer_settings["sniffer_mode"]):
            myplot.myplot(data=self.sniffer_data["sniffer_energy_levels"],
                    data_x=self.sniffer_data["sniffer_times"],
                    plottype=["line_xy"],
                    title="Channel Energy Level",
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
            myplot.myplot(data=self.sniffer_smoothed_data["sniffer_energy_levels"],
                    data_x=self.sniffer_data["sniffer_times"],
                    plottype=["line_xy"],
                    title="Smoothed Channel Energy Level",
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
