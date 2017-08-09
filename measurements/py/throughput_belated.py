import numpy as np
import subprocess
import myplot_belated as myplot
import os.path as pt
import lines

import pdb

print("Hello from throughput_belated.py! Really, it's me!")

class tp:
    def __init__(self,**kwargs):
        print("Tp instance initialized!")
        #self.__dict__.update(kwargs)
        self.data_source_path       =   kwargs.get("data_source_path","/home/alex/0_ba/git/self.measurements/data")
        self.plot_path              =   kwargs.get("plot_path","/home/alex/0_ba/git/self.measurements/plots")
        self.plot_type              =   kwargs.get("plot_type","all")
        self.measurement            =   kwargs.get("measurement",[])
        self.repetitions            =   kwargs.get("repetitions",5)
        self.show_plot              =   kwargs.get("show_plot","False")
        self.throughput_data_files  =   kwargs.get("throughput_data_files", ["sender_data_sent.txt","sender_ack_received.txt"])
        self.packet_size            =   kwargs.get("packet_size", 1000)
        self.timer                  =   kwargs.get("timer",300)
        self.grid                   =   kwargs.get("grid",False)
        self.legend                 =   kwargs.get("legend", [])
        self.xticks                 =   kwargs.get("xticks", [])
        self.legend_loc             =   kwargs.get("legend_loc", "best")
        self.annotations_below      =   kwargs.get("annotations_below", [])
        self.annotations_other      =   kwargs.get("annotations_other", [])
        self.legend_coordinates     =   kwargs.get("legend_coordinates", False)
        self.create_plots           =   kwargs.get("create_plots", True)
        self.links                  =   kwargs.get("links", [1 for x in range(len(self.measurement))])
        #pdb.set_trace()

    def calc(self):
        # ------------------------------ Calculations ---------------------------------#
        # Create a self.repetitions X 1 matrix aka row vector with self.measurement data
        print("I'll create a numpy array!")
        self.data = np.zeros(shape=(len(self.measurement),self.repetitions))
        print("Done.")

        for index,single_measurement in enumerate(self.measurement):
            for i in range(self.repetitions):
                print("I'll open files from iteration "+str(i+1)+" for you!")
                file_path = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                data_file_path = file_path+self.throughput_data_files[0]+"_"+str(self.links[index])+".txt"
                ack_file_path = file_path+self.throughput_data_files[1]+"_"+str(self.links[index])+".txt"
                if pt.isfile(ack_file_path):
                    print("Let's count some ACKS!")
                    ackcount = lines.linecount(ack_file_path)
                else:
                    # no acks found
                    print("ACK file not found at "+ack_file_path+".")
                    ackcount = 0
                    self.data[index,i] = 0
                if pt.isfile(data_file_path):
                    print("Let's count some data!")
                    datacount = lines.linecount(data_file_path)
                    print("ackcount: "+str(ackcount))
                    print("datacount: "+str(datacount))
                    # *8 = bytes -> bits /1000 => 1 --> kilo
                    self.data[index,i] = min(ackcount, datacount)*self.packet_size/self.timer*8/1000
                else:
                    # no data sent off
                    print("Data file not found at "+data_file_path+".")
                    datacount = 0
                    self.data[index,i] = 0

        print(self.data)
        #------------------------------------------------------------------------------#

    def plot(self):
        self.calc()
        all_data = []

        for val in self.data:
            all_data.extend(val)

        #print("all_data:")
        #print(all_data)

        print("Let's plot! ;-)")
        if self.create_plots == True or self.create_plots["throughput"] == True:
            myplot.myplot(  data=self.data,
                bins=np.arange(
                    min(all_data)-float(self.packet_size),
                    max(all_data)+float(self.packet_size),
                    (max(all_data)-min(all_data)+1)/25),
                plottype=self.plot_type,
                title="Throughput",
                xlabel="throughput [kbit/s]",
                ylabel="throughput [kbit/s]",
                savepath=self.plot_path+"/",
                show=self.show_plot,
                grid=self.grid,
                xticks=self.xticks,
                legend=self.legend,
                legend_loc=self.legend_loc,
                annotations_below=self.annotations_below,
                annotations_other=self.annotations_other,
                legend_coordinates=self.legend_coordinates["throughput"])
