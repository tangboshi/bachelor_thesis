import numpy as np
import myplot
import os

print("Hello from rtt.py!")

class rtt:
    def __init__(self, **kwargs):
        #self.__dict__.update(kwargs)
        self.data_source_path   =   kwargs.get("data_source_path","/home/alex/0_ba/git/measurements/data")
        self.rtt_data_files     =   kwargs.get("rtt_data_files", ["sender_bfr_dq.txt","sender_ack_received.txt"])
        self.rtt_mode           =   kwargs.get("rtt_mode","frame_delay")
        self.plot_path          =   kwargs.get("plot_path","/home/alex/0_ba/git/measurements/plots")
        self.plot_type          =   kwargs.get("plot_type","all")
        self.measurement        =   kwargs.get("measurement",[])
        self.repetitions        =   kwargs.get("repetitions",5)
        self.show_plot          =   kwargs.get("show_plot","False")
        self.max_retxs          =   kwargs.get("max_retxs",6)
        self.retxs_data_files   =   kwargs.get("retxs_data_files",["sender_retransmissions"])
        self.timer              =   kwargs.get("timer",300)
        self.grid               =   kwargs.get("grid",False)
        self.legend             =   kwargs.get("legend", [])
        self.xticks             =   kwargs.get("xticks", [])
        self.legend_loc         =   kwargs.get("legend_loc", "best")
        self.annotations_below  =   kwargs.get("annotations_below", [])
        self.annotations_other  =   kwargs.get("annotations_other", [])
        self.legend_coordinates =   kwargs.get("legend_coordinates", False)
        self.create_plots       =   kwargs.get("create_plots", True)
        self.links              =   kwargs.get("links", [1 for x in range(len(self.measurement))])
        self.eval_mode          =   kwargs.get("eval_mode", "belated")

        print(self.links)
        print ("Calculating "+self.rtt_mode+"...")
        #for debugging purposes
        #print(str(self.__dict__))
        #print(self.repetitions)

    # ------------------------------ Calculations ---------------------------------#
    def calc(self):
        print("Taking a look at the following measurements: "+str(self.measurement))
        # The stuff we want to plot later
        self.rtt = np.zeros(shape=(len(self.measurement),self.repetitions))
        self.packet_loss_percent = []
        self.avg_frame_txs = []
        self.all_retxs = []
        self.retxs_overall = []
        retxs_per_measurement = []
        self.plp_per_measurement = []

        for index,single_measurement in enumerate(self.measurement):
            plp_per_measurement = []
            data_sent_times = []
            ack_received_times = []
            rtt_single_measurement = []
            retxs_per_repetition = []
            total_retxs = 0
            txs_fails = 0


            print("index(measurement): "+str(index))
            print("self.rtt before calc:"+str(self.rtt))

            for i in range(self.repetitions):
                path                = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                data_sent_path      = path+self.rtt_data_files[0]+"_"+str(self.links[index])+".txt"
                ack_received_path   = path+self.rtt_data_files[1]+"_"+str(self.links[index])+".txt"
                retxs_path          = path+self.retxs_data_files[0]+"_"+str(self.links[index])+".txt"

                print(str(i+1))
                print("data_sent_path:"+data_sent_path)
                print("ack_received_path:"+ack_received_path)

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

                if os.path.isfile(ack_received_path):
                    with open(ack_received_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            secs, usecs = line.split(" ",1)
                            missing_zeros = 6 - len(usecs)
                            usecs = ("0" * missing_zeros) + usecs
                            line = ".".join([secs, usecs])
                            ack_received_times += [float(line)]
                            #print("ack_received: "+line)

                else:
                    print(  "File "+ack_received_path+" not found. \
                            Assuming not reached in GR.")

                if os.path.isfile(retxs_path):
                    with open(retxs_path) as f:
                        for line in f:
                            line.strip("\n")
                            line = [int(item) for item in line.split()]
                            retxs_per_repetition += [item for item in line]
                            #print("retx: "+str(line))
                        #print("len:retx: "+str(len(retxs_per_repetition)))


                else:
                    print(  "File "+retxs_path+" not found. \
                            Assuming not reached in GR. Creating data for you...")
                    for index in range(len(ack_received_times)):
                        retxs += [0]


                #frame_delay_condition = self.rtt_mode == "frame_delay" and counter <= self.max_retxs
                #rtt_condition = self.rtt_mode == "rtt" and counter == 0

                data_pos = 0
                for k,ack in enumerate(ack_received_times):
                    for l,data in enumerate(data_sent_times):
                        if data > ack:
                            if self.rtt_mode == "rtt":
                                rtt_single_measurement += [round(ack - data_sent_times[l-1],5)]
                            if self.rtt_mode == "frame_delay":
                                rtt_single_measurement += [round(ack - data_sent_times[data_pos], 5)]
                            data_pos = l
                            break;

                print(rtt_single_measurement)

                #Now calculate mean RTT for this measurement
                print(str(float(sum(rtt_single_measurement))))
                print(str(len(rtt_single_measurement)))
                if len(rtt_single_measurement) > 0:
                    rtt_single_mean =   float(sum(rtt_single_measurement))/len(rtt_single_measurement)
                else:
                    rtt_single_mean =   0
                # rtt_single_mean seems to be calculated correctly, but source data is odd.
                print("\nThe resulting mean RTT of this single measurement is:")
                print(rtt_single_mean)
                print("\n")

                print("self.rtt is:"+str(self.rtt))
                self.rtt[index,i] = rtt_single_mean
                print(str(self.rtt.shape))
                print("index:"+str(index))
                print("i:"+str(i))

                ### Packet loss ###
                packet_loss_abs = float( len(data_sent_times) - len(ack_received_times) )
                if len(data_sent_times) > 0:
                    packet_loss_rel = float( packet_loss_abs / len(data_sent_times) )
                else:
                    packet_loss_rel = 0
                self.packet_loss_percent += [round(packet_loss_rel*100, 2)]
                plp_per_measurement += [round(packet_loss_rel*100, 2)]
                print("abs. packet loss: "+str(packet_loss_abs))
                print("packet loss in %: "+str(self.packet_loss_percent[-1])+"%")
                ### Average retransmissions per frame ###
                ### practically the same  as packet loss
                if not sum(retxs_per_repetition) == 0 and not len(retxs_per_repetition) == 0:
                    self.avg_frame_txs += [sum(retxs_per_repetition) / len(retxs_per_repetition)]

                ## retransmissions
                retxs_per_measurement += retxs_per_repetition

                # Prepare next iteration
                rtt_single_measurement = []
                ack_received_times = []
                data_sent_times = []
                total_retxs = 0
                txs_fails = 0
                print("***len:self.retxs_per_repetition***")
                print(len(retxs_per_repetition))
                retxs_per_repetition = []

            self.retxs_overall.append(retxs_per_measurement)
            self.plp_per_measurement.append(plp_per_measurement)

            print("***len:self.retxs_per_measurement***")
            print(len(retxs_per_measurement))
            retxs_per_measurement = []

            #return data_sent_times,ack_received_times
            #print("self.rtt after calc:"+str(self.rtt))
            #print("****************************************")
            #print("\n\n\n\n")

    #------------------------------------------------------------------------------#

    def plot(self):

        self.calc()
        print("***self.rtt***")
        print (self.rtt)

        if "all" in self.plot_type:
            # Removed line, cause it is bugged atm.
            self.plot_type  =   ["pdf","cdf","boxplot","bar"]

        rtt_vals = []

        for item in self.rtt:
            for val in item:
                rtt_vals += [round(val,5)]


        if self.create_plots == True or self.create_plots["rtt"] == True:
            delay_titles = {
                "rtt": "RTT",
                "frame_delay": "Frame Delay"
            }
            myplot.myplot(data=self.rtt,
                    plottype=self.plot_type,
                    title=delay_titles[self.rtt_mode],
                    xlabel=self.rtt_mode.replace("_", " ")+" [s]",
                    ylabel=self.rtt_mode.replace("_", " ")+" [s]",
                    savepath=self.plot_path+"/",
                    show=self.show_plot,
                    grid=self.grid,
                    xticks=self.xticks,
                    legend=self.legend,
                    legend_loc=self.legend_loc,
                    annotations_below=self.annotations_below,
                    annotations_other=self.annotations_other,
                    legend_coordinates=self.legend_coordinates["rtt"],
                    eval_mode=self.eval_mode)

        if self.create_plots == True or self.create_plots["packet_loss"] == True:
            myplot.myplot(data=self.plp_per_measurement,
                    plottype=self.plot_type,
                    title="Packet Loss",
                    xlabel="packet loss [%]",
                    ylabel="packet loss [%]",
                    savepath=self.plot_path+"/",
                    show=self.show_plot,
                    grid=self.grid,
                    xticks=self.xticks,
                    legend=self.legend,
                    legend_loc=self.legend_loc,
                    annotations_below=self.annotations_below,
                    annotations_other=self.annotations_other,
                    legend_coordinates=self.legend_coordinates["packet_loss"],
                    eval_mode=self.eval_mode)

        if len(self.all_retxs) <= 20:
            number_bars = True
        else:
            number_bars = False

        ### Probably uninteresting
        # myplot.myplot(data=self.all_retxs,
        #         bins=np.arange(
        #             0,
        #             self.max_retxs+1,
        #             0.1),
        #         plottype=self.plot_type,
        #         title="Retransmissions Overall",
        #         xlabel="retransmissions",
        #         ylabel="retransmissions",
        #         savepath=self.plot_path+"/",
        #         show=self.show_plot,
        #         number_bars=number_bars)

        if self.create_plots == True or self.create_plots["retxs"] == True:
            myplot.myplot(data=self.retxs_overall,
                    plottype=self.plot_type,
                    title="Retransmissions per Frame",
                    xlabel="retransmissions/frame",
                    ylabel="retransmissions/frame",
                    savepath=self.plot_path+"/",
                    show=self.show_plot,
                    number_bars=number_bars,
                    grid=self.grid,
                    xticks=self.xticks,
                    legend=self.legend,
                    legend_loc=self.legend_loc,
                    annotations_below=self.annotations_below,
                    annotations_other=self.annotations_other,
                    legend_coordinates=self.legend_coordinates["retxs"],
                    eval_mode=self.eval_mode)
