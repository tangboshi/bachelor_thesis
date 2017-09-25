import numpy as np
import myplot as myplot
import os

print("Hello from backoff.py!")

class backoff:
    def __init__(self, **kwargs):
        #self.__dict__.update(kwargs)
        self.data_source_path   =   kwargs.get("data_source_path","/home/alex/0_ba/git/measurements/data")
        self.backoff_data_files =   kwargs.get("backoff_data_files", ["sender_cs_backoff_times"])
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

        for index,single_measurement in enumerate(self.measurement):
            print("index(measurement): "+str(index))
            self.backoff_csfail_sum = np.zeros(shape=(len(self.measurement),self.repetitions))

            for i in range(self.repetitions):
                path                    = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                backoff_csfail_path     = path+self.backoff_data_files[0]+"_"+str(self.links[index])+".txt"
                backoff_csfail_times    = []

                print(str(i+1))
                print("backoff_csfail_path:"+backoff_csfail_path)

                if os.path.isfile(backoff_csfail_path):
                    with open(backoff_csfail_path) as f:
                        for line in f:
                            line = line.strip('\n')
                            backoff_csfail_times += [float(line)]
                            #print("backoff: "+line)
                    backoff_csfail_times += [0]
                    self.backoff_csfail_sum[index,i] = sum(backoff_csfail_times)
                else:
                    print(  "File "+backoff_csfail_path+" not found. \
                            Assuming not reached in GR.")
                    self.backoff_csfail_sum[index,i] = 0


    #------------------------------------------------------------------------------#

    def plot(self):

        self.calc()
        print("***self.backoff***")
        print (self.backoff_csfail_sum)

        if "all" in self.plot_type:
            # Removed line, cause it is bugged atm.
            self.plot_type  =   ["pdf","cdf","boxplot","bar"]

        if self.create_plots == True or self.create_plots["backoff_csfail"] == True:
            myplot.myplot(data=self.backoff_csfail_sum,
                    plottype=self.plot_type,
                    title="CS Fail Backoff Sum, (Measurement Time:"+str(self.timer)+u"\u00b1"+"5s)",
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
                    legend_coordinates=self.legend_coordinates["backoff_csfail"],
                    eval_mode=self.eval_mode)
