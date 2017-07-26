import numpy as np
import subprocess
import myplot_belated as myplot
import os.path as pt
import lines

print("Hello from throughput_belated.py!")

class tp:
    def __init__(self,**kwargs):
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

    def calc(self):
        # ------------------------------ Calculations ---------------------------------#
        # Create a self.repetitions X 1 matrix aka row vector with self.measurement data
        self.data = np.zeros(shape=(len(self.measurement),self.repetitions))

        for index,single_measurement in enumerate(self.measurement):
            for i in range(self.repetitions):
                file_path = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                data_file_path = file_path+self.throughput_data_files[0]
                ack_file_path = file_path+self.throughput_data_files[1]
                if pt.isfile(ack_file_path):
                    ackcount = lines.linecount(ack_file_path)
                else:
                    # no acks found
                    print("ACK file not found at "+ack_file_path+".")
                    ackcount = 0
                    self.data[index,i] = 0
                if pt.isfile(data_file_path):
                    datacount = lines.linecount(data_file_path)
                    print("ackcount: "+str(ackcount))
                    print("datacount: "+str(datacount))
                    self.data[index,i] = min(ackcount, datacount)*self.packet_size/self.timer
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

        print("all_data:")
        print(all_data)

        myplot.myplot(  data=self.data,
            bins=np.arange(
                min(all_data)-float(self.packet_size),
                max(all_data)+float(self.packet_size),
                (max(all_data)-min(all_data)+1)/25),
            plottype=self.plot_type,
            title="Throughput",
            xlabel="throughput [B/s]",
            ylabel="throughput [B/s]",
            savepath=self.plot_path+"/",
            show=self.show_plot,
            grid=self.grid,
            xticks=self.xticks,
            legend=self.legend,
            legend_loc=self.legend_loc,
            annotations_below=self.annotations_below,
            annotations_other=self.annotations_other)
