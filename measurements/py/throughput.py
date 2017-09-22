import numpy as np
import subprocess
import myplot
import os.path as pt
import lines

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
        self.throughput_data_files  =   kwargs.get("throughput_data_files", ["sender_data_sent","sender_ack_received"])
        self.diagnosis_files        =   kwargs.get("diagnosis_files", ["receiver_data_received","receiver_ack_sent"])
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
        self.eval_mode              =   kwargs.get("eval_mode", "belated")
        self.receiver_mode          =   kwargs.get("receiver_mode", "single")
        #pdb.set_trace()

    def calc(self):
        # ------------------------------ Calculations ---------------------------------#
        # Create a self.repetitions X 1 matrix aka row vector with self.measurement data
        print("I'll create a numpy array!")
        self.data = np.zeros(shape=(len(self.measurement),self.repetitions))
        self.sender_diagnosis = np.zeros(shape=(len(self.measurement),self.repetitions))
        self.receiver_diagnosis = np.zeros(shape=(len(self.measurement),self.repetitions))
        print("Done.")

        if self.receiver_mode == "single":
            link = ""
        else:
            link = "_"+str(self.links[index])

        for index,single_measurement in enumerate(self.measurement):
            for i in range(self.repetitions):
                print("I'll open files from iteration "+str(i+1)+" for you!")
                file_path = self.data_source_path+'/'+str(self.measurement[index])+'/'+str(i+1)+'/'
                data_sent_file_path = file_path+self.throughput_data_files[0]+"_"+str(self.links[index])+".txt"
                ack_received_file_path = file_path+self.throughput_data_files[1]+"_"+str(self.links[index])+".txt"

                data_received_file_path = file_path+self.diagnosis_files[0]+link+".txt"
                ack_sent_file_path = file_path+self.diagnosis_files[1]+link+".txt"

                if pt.isfile(ack_received_file_path):
                    print("Let's count some ACKS!")
                    ackcount = lines.linecount(ack_received_file_path)
                else:
                    # no acks found
                    print("ACK file not found at "+ack_received_file_path+".")
                    ackcount = 0
                    self.data[index,i] = 0
                if pt.isfile(data_sent_file_path):
                    print("Let's count some data!")
                    datacount = lines.linecount(data_sent_file_path)
                    print("ackcount: "+str(ackcount))
                    print("datacount: "+str(datacount))
                    # *8 => bytes --> bits ||| /1000 => 1 --> kilo
                    self.data[index,i] = min(ackcount, datacount)*self.packet_size/self.timer*8/1000
                else:
                    # no data sent off
                    print("Data file not found at "+data_sent_file_path+".")
                    datacount = 0
                    self.data[index,i] = 0

                if pt.isfile(data_received_file_path) and pt.isfile(ack_sent_file_path) and datacount > 0 and ackcount > 0:
                    print("Hoorray, diagnosis files found!")
                    receiver_datacount = lines.linecount(data_received_file_path)
                    receiver_ackcount = lines.linecount(ack_sent_file_path)
                    # the term diagnosis is concerning the sender's or receiver's receiving capability
                    # this assumes that sent-off frames are good frames
                    # *100 => %
                    self.sender_diagnosis[index,i] = 100 - (receiver_ackcount - ackcount)/receiver_ackcount*100
                    self.receiver_diagnosis[index,i] = 100 - (datacount - receiver_datacount)/datacount*100
                else:
                    print("Diagnosis files incomplete or missing :( \
                    (or no sender-side received acks/ receiver-side received data)!")


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
                legend_coordinates=self.legend_coordinates["throughput"],
                eval_mode=self.eval_mode)

        if self.create_plots == True or self.create_plots["diagnostic"] == True:
            myplot.myplot(  data=self.receiver_diagnosis,
                plottype=self.plot_type,
                title="Receiver Receiving Score (Inverse = Data Loss)",
                xlabel="score [%]",
                ylabel="score [%]",
                savepath=self.plot_path+"/",
                show=self.show_plot,
                grid=self.grid,
                xticks=self.xticks,
                legend=self.legend,
                legend_loc=self.legend_loc,
                annotations_below=self.annotations_below,
                annotations_other=self.annotations_other,
                legend_coordinates=self.legend_coordinates["diagnosis_receiver"],
                eval_mode=self.eval_mode)

            myplot.myplot(  data=self.sender_diagnosis,
                plottype=self.plot_type,
                title="Sender Receiving Score (Inverse = ACK Loss)",
                xlabel="score [%]",
                ylabel="score [%]",
                savepath=self.plot_path+"/",
                show=self.show_plot,
                grid=self.grid,
                xticks=self.xticks,
                legend=self.legend,
                legend_loc=self.legend_loc,
                annotations_below=self.annotations_below,
                annotations_other=self.annotations_other,
                legend_coordinates=self.legend_coordinates["diagnosis_sender"],
                eval_mode=self.eval_mode)
