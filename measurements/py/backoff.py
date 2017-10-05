import numpy as np
import myplot as myplot
import os

print("Hello from backoff.py!")

class backoff:
    def __init__(self, **kwargs):
        #self.__dict__.update(kwargs)
        self.data_source_path   =   kwargs.get("data_source_path","/home/alex/0_ba/git/measurements/data")
        self.backoff_data_files =   kwargs.get("backoff_data_files", ["sender_backoff_times_cs", "sender_backoff_times_ack"])
        self.plot_path          =   kwargs.get("plot_path","/home/alex/0_ba/git/measurements/plots")
        self.plot_type          =   kwargs.get("plot_type","all")
        self.measurement        =   kwargs.get("measurement",[])
        self.repetitions        =   kwargs.get("repetitions",5)
        self.show_plot          =   kwargs.get("show_plot","False")
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
        #for debugging purposes
        #print(str(self.__dict__))
        #print(self.repetitions)

    # ------------------------------ Calculations ---------------------------------#
    def calc(self):
        print("Taking a look at the following measurements: "+str(self.measurement))
        # The stuff we want to plot later
        self.backoff_cs_sum = np.zeros(shape=(len(self.measurement),self.repetitions))
        self.backoff_ack_sum = np.zeros(shape=(len(self.measurement),self.repetitions))
        self.backoff_joint_sum = np.zeros(shape=(len(self.measurement),self.repetitions))

        for index,single_measurement in enumerate(self.measurement):
            print("index(measurement): "+str(index))
            for i in range(self.repetitions):
                path                = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                backoff_cs_path     = path+self.backoff_data_files[0]+"_"+str(self.links[index])+".txt"
                backoff_ack_path    = path+self.backoff_data_files[1]+"_"+str(self.links[index])+".txt"
                backoff_cs_times,backoff_ack_times = [],[]

                #print(str(i+1))
                #print("backoff_cs_path:"+backoff_cs_path)

                if os.path.isfile(backoff_cs_path):
                    with open(backoff_cs_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            backoff_cs_times += [float(line)]
                            #print("backoff: "+line)
                    backoff_cs_times += [0]
                else:
                    print(  "File "+backoff_cs_path+" not found. \
                            Assuming not reached in GR.")
                    self.backoff_cs_sum[index,i] = 0

                if os.path.isfile(backoff_ack_path):
                    with open(backoff_ack_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            backoff_ack_times += [float(line)]
                            #print("backoff: "+line)
                    backoff_ack_times += [0]
                else:
                    print(  "File "+backoff_ack_path+" not found. \
                            Assuming not reached in GR.")
                    self.backoff_ack_sum[index,i] = 0

                # print("backoff cs:"+str(sum(backoff_cs_times)))
                # print("backoff ack:"+str(sum(backoff_ack_times)))
                # print("backoff joint:"+str(sum(backoff_cs_times)+sum(backoff_ack_times)))

                sum_backoff_cs_times = sum(backoff_cs_times)
                sum_backoff_ack_times = sum(backoff_ack_times)
                self.backoff_cs_sum[index,i] = sum_backoff_cs_times
                self.backoff_ack_sum[index,i] = sum_backoff_ack_times
                self.backoff_joint_sum[index,i] = sum_backoff_cs_times+sum_backoff_ack_times
                # print(self.backoff_cs_sum)
                # print(self.backoff_ack_sum)
                # print(self.backoff_joint_sum)

    #------------------------------------------------------------------------------#

    def plot(self):

        self.calc()
        print("***self.backoff***")
        #print (self.backoff_sum)

        if "all" in self.plot_type:
            # Removed line, cause it is bugged atm.
            self.plot_type  =   ["pdf","cdf","boxplot","bar"]

        if self.create_plots == True or self.create_plots["backoff"] == True:
            myplot.myplot(data=self.backoff_cs_sum,
                    plottype=self.plot_type,
                    title="Backoff (Channel Busy) Sum",
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
                    legend_coordinates=self.legend_coordinates["backoff"],
                    eval_mode=self.eval_mode,
                    xlims=[0,self.timer])

            myplot.myplot(data=self.backoff_ack_sum,
                    plottype=self.plot_type,
                    title="Backoff (Acks) Sum",
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
                    legend_coordinates=self.legend_coordinates["backoff"],
                    eval_mode=self.eval_mode,
                    xlims=[0,self.timer])

            myplot.myplot(data=self.backoff_joint_sum,
                    plottype=self.plot_type,
                    title="Backoff (Joint) Sum",
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
                    legend_coordinates=self.legend_coordinates["backoff"],
                    eval_mode=self.eval_mode,
                    xlims=[0,self.timer])
