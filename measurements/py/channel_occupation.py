import numpy as np
import myplot
import os

print ("Hello from channel_occupation.py!")

class channel_occupation:
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
        self.co_data_files              =   kwargs.get("co_data_files", ["sender_bfr_dq.txt","receiver_ack_sent.txt","sender_ack_received"])
        self.receiver_mode              =   kwargs.get("receiver_mode", "single")

        self.calc()
        self.plot()

    def calc(self):
        print("self.measurement")
        print(self.measurement)
        print("self.repetitions")
        print(self.repetitions)

        busy_starting_times = []
        acks_received = []

        if self.receiver_mode == "single":
            link = ""
        else:
            link = "_"+str(self.links[index])

        # FIXME: let's try to avoid this repetition of code from rtt! (until ###)
        for index,single_measurement in enumerate(self.measurement):
            ack_received_times = []
            data_sent_times = []
            ack_sent_times = []

            for i in range(self.repetitions):
                path                = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                data_sent_path      = path+self.co_data_files[0]+"_"+str(self.links[index])+".txt"
                ack_sent_path       = path+self.co_data_files[1]+link+".txt"
                ack_received_path   = path+self.co_data_files[2]+"_"+str(self.links[index])+".txt"

                if os.path.isfile(data_sent_path):
                    with open(data_sent_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            secs, usecs = line.split(" ",1)
                            missing_zeros = 6 - len(usecs)
                            usecs = ("0" * missing_zeros) + usecs
                            line = ".".join([secs, usecs])
                            data_sent_times += [float(line)]
                            #print("data_sent: "+line)
                else:
                    print(  "File "+data_sent_path+" not found. \
                            Assuming not reached in GR.")
                    # Preventing these arrays from being empty to prevent wrong
                    # depiction of results
                    data_sent_times += [0.0]

                if os.path.isfile(ack_sent_path):
                    with open(ack_sent_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            secs, usecs = line.split(" ",1)
                            missing_zeros = 6 - len(usecs)
                            usecs = ("0" * missing_zeros) + usecs
                            line = ".".join([secs, usecs])
                            ack_sent_times += [float(line)]
                            #print("ack_sent: "+line)

                else:
                    print(  "File "+ack_sent_path+" not found. \
                            Assuming not reached in GR.")
                    # Preventing these arrays from being empty to prevent wrong
                    # depiction of results
                    ack_sent_times += [0.0]

                if os.path.isfile(ack_received_path):
                    with open(ack_received_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            secs, usecs = line.split(" ",1)
                            missing_zeros = 6 - len(usecs)
                            usecs = ("0" * missing_zeros) + usecs
                            line = ".".join([secs, usecs])
                            ack_received_times += [float(line)]
                            #print("ack_sent: "+line)

                else:
                    print(  "File "+ack_received_path+" not found. \
                            Assuming not reached in GR.")
                    # Preventing these arrays from being empty to prevent wrong
                    # depiction of results
                    ack_received_times += [0.0]

            busy_starting_times += [data_sent_times]
            busy_starting_times += [ack_sent_times]
            acks_received += [ack_received_times]
            # Prepare next iteration
            ack_sent_times = []
            ack_received_times = []
            data_sent_times = []
        # ###
        print("len(acks_received):")
        print(len(acks_received))
        print("len(busy_starting_times):")
        print(len(busy_starting_times))
        print("ack_received_times:")
        #print(ack_received_times)
        print("data_sent_times:")
        #print(data_sent_times)

        # Get channel occupation data from files
        # busy_starting_times = [
        #                         [5,27,61],
        #                         [16],
        #                         [34,88,97],
        #                         [22,48],
        #                         [16,37,44],
        #                         [27,55]
        #                     ]

        # Normalize the x-axis to start at 0
        # 'cause UNIX-time isnt really a nice human-readable format
        offset_candidates = [item[0] for item in busy_starting_times]

        #hardware_delay = 0
        hardware_delay = 1.09
        offset = min(offset_candidates) - hardware_delay

        # barwidths in seconds
        data_width = 0.04
        ack_width = 0.007
        ack_received_width = 0.004


        for index,process in enumerate(busy_starting_times):
            busy_starting_times[index] = [time-offset for time in process]
        for index,process in enumerate(acks_received):
            pass
            #acks_received[index] = [time - offset - ack_received_width for time in process]

        print("acks_received")
        #print(acks_received)
        # prepare lists for data for graphical representation
        busy_end_times = []
        busy_durations = []

        for index,process in enumerate(busy_starting_times):
            # KISS: process = (data,ack)
            # data channel occupation time is estimated as 0.04s
            # ack channel occupation time is estimated as 0.01s
            if index % 2 == 0:
                process_time = data_width
                #process_time = 10
            else:
                process_time = ack_width
                #process_time = 5
            # Uncomment next two code comments if end of channel occupation
            # is of any interest
            #process     = [time+process_time for time in process]
            occupation  = [process_time for time in range(len(process))]
            #busy_end_times.append(process)
            busy_durations.append(occupation)

        acks_received_bar_width = []
        for index,process in enumerate(acks_received):
            acks_received_bar_width.append([ack_received_width for x in range(len(process))])

        print("acks_received_bar_width:")
        #print(acks_received_bar_width)


        print("busy_starting_times:")
        #print(busy_starting_times)
        print("busy_end_times:")
        #print(busy_end_times)
        print("busy_durations:")
        #print(busy_durations)

        self.occupation_data = {
            "occupation_starting":      busy_starting_times,
            "occupation_durations":     busy_durations,
            "acks_received":            acks_received,
            "acks_received_bar_width":  acks_received_bar_width
        }

        # Let's prepare the zoomed-in data set
        busy_zoomed_starting_times = []
        acks_received_zoomed = []
        starting_times = [] # temporary variable;
        ack_times = [] # temporary variable
        busy_zoomed_durations = []

        print("self.channel_occupation_mode:")
        print(self.channel_occupation_mode)

        if "zoom" in self.channel_occupation_mode["occupation_mode"]:
            for process in busy_starting_times:
                for time in process:
                    if time > self.channel_occupation_mode["zoom"][0]:
                        if time > self.channel_occupation_mode["zoom"][1]:
                            break;
                        else:
                            starting_times.append(time)
                busy_zoomed_starting_times.append(starting_times)
                starting_times = []

            for process in acks_received:
                for time in process:
                    if time > self.channel_occupation_mode["zoom"][0]:
                        if time > self.channel_occupation_mode["zoom"][1]:
                            print("time:"+str(time)+" break")
                            break;
                        else:
                            print("time:"+str(time))
                            ack_times.append(time)
                acks_received_zoomed.append(ack_times)
                ack_times = []

            print("acks_received_zoomed:")
            #print(acks_received_zoomed)

            for index,process in enumerate(busy_zoomed_starting_times):
                if index % 2 == 0:
                    process_time = data_width
                else:
                    process_time = ack_width
                occupation  = [process_time for time in range(len(process))]
                print("len(process):")
                print(len(process))
                busy_zoomed_durations.append(occupation)

            acks_received_zoomed_bar_width = []
            for index,process in enumerate(acks_received_zoomed):
                acks_received_zoomed_bar_width.append([ack_received_width for time in range(len(process))])

            print("busy_zoomed_durations:")
            print(len(busy_zoomed_starting_times))
            print(len(busy_zoomed_durations))

            print("acks zoomed stuff:")
            print(len(acks_received_zoomed))
            print(len(acks_received_zoomed_bar_width))

            self.zoomed_occupation_data = {
                "occupation_starting":      busy_zoomed_starting_times,
                "occupation_durations":     busy_zoomed_durations,
                "acks_received":            acks_received_zoomed,
                "acks_received_bar_width":  acks_received_zoomed_bar_width
            }

    def plot(self):

        print("Let's plot.")
        #print(self.occupation_data)

        #Prefered object-oriented approach
        if  (
                (   self.create_plots == True
                    or self.create_plots["channel_occupation"] == True)
                and
                "overview" in self.channel_occupation_mode["occupation_mode"]
            ):
            myplot.myplot(data=self.occupation_data,
                    plottype=["broken_barh"],
                    title="Channel Occupation",
                    xlabel="time [s]",
                    ylabel="time [s]",
                    savepath=self.plot_path+"/",
                    show=self.show_plot,
                    grid=self.grid,
                    xticks=self.xticks,
                    legend=self.legend,
                    legend_loc=self.legend_loc,
                    annotations_below=self.annotations_below,
                    annotations_other=self.annotations_other,
                    legend_coordinates=self.legend_coordinates["channel_occupation"],
                    eval_mode=self.eval_mode,
                    timer=self.timer,
                    repetitions=self.repetitions)

        if  (
                (   self.create_plots == True
                    or self.create_plots["channel_occupation"] == True)
                and
                "zoom" in self.channel_occupation_mode["occupation_mode"]
            ):
            myplot.myplot(data=self.zoomed_occupation_data,
                    plottype=["broken_barh"],
                    title="Zoomed Channel Occupation",
                    xlabel="time [s]",
                    ylabel="time [s]",
                    savepath=self.plot_path+"/",
                    show=self.show_plot,
                    grid=self.grid,
                    xticks=self.xticks,
                    legend=self.legend,
                    legend_loc=self.legend_loc,
                    annotations_below=self.annotations_below,
                    annotations_other=self.annotations_other,
                    legend_coordinates=self.legend_coordinates["channel_occupation"],
                    eval_mode=self.eval_mode,
                    timer=self.timer,
                    repetitions=self.repetitions,
                    xlims=self.channel_occupation_mode["zoom"])
