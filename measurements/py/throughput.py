import numpy as np
import subprocess
import myplot
import os.path as pt

print("Hello from throughput.py!")

# Let's import all data we need
#try:
from variables import (
    data_source_path,
    throughput_data_files,
    packet_size,
    plot_path,
    plot_type,
    measurement,
    repetitions,
    show_plot
)
#except ImportError:
    #print("Probably not all data were imported correctly.")

# ------------------------------ Calculations ---------------------------------#
# Create a repetitions X 1 matrix aka row vector with measurement data
data = np.zeros(shape=(repetitions))

for i in range(1,repetitions+1):
    file_path = data_source_path+'/'+str(i)+'/'
    file_path = file_path+throughput_data_files["receiver_data_received"]
    if pt.isfile(file_path):
        linecount = subprocess.run(['wc', '-l', file_path], stdout=subprocess.PIPE)
        linecount = linecount.stdout.decode('utf-8')
        linecount = linecount.partition(" ")[0]
        linecount = int(linecount)
        data[i-1] = linecount*packet_size
    else:
        # no data put through
        print("Data file not found. Probably zero throughput.")
        data[i-1] = 0
print(data)
#------------------------------------------------------------------------------#

for index, plot in enumerate(plot_type):

    xlabels = {
        "cdf": "throughput",
        "pdf": "throughput",
        "boxplot": "",
        "bar": "",
        "line": ""
    }

    ylabels = {
        "pdf": "",
        "cdf": "",
        "boxplot": "throughput",
        "bar":  "throughput",
        "line": "throughput"
    }

    titles = {
        "pdf": "PDF",
        "cdf":  "CDF",
        "boxplot": "boxplot",
        "bar": "bar chart",
        "line": "line chart"
    }

    myplot.myplot(  data=data,
        bins=np.arange(
            min(data)-float(packet_size),
            max(data)+float(packet_size),
            (max(data)-min(data))/25),
            #packet_size/25),
        plottype=plot,
        title="Throughput "+titles[plot],
        xlabel=xlabels[plot],
        ylabel=ylabels[plot],
        savepath=plot_path+"/"+measurement+"/",
        show=show_plot)
