import numpy as np
import subprocess
import myplot

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
    linecount = subprocess.run(['wc', '-l', file_path], stdout=subprocess.PIPE)
    linecount = linecount.stdout.decode('utf-8')
    linecount = linecount.partition(" ")[0]
    linecount = int(linecount)
    data[i-1] = linecount*packet_size
print(data)
#------------------------------------------------------------------------------#

for index, plot in enumerate(plot_type):

    xlabels = {
        "cdf": "throughput",
        "pdf": "throughput"
    }

    ylabels = {
        "pdf": "",
        "cdf": ""
    }

    titles = {
        "pdf": "PDF",
        "cdf":  "CDF"
    }

    myplot.myplot(  data=data,
            bins=repetitions,
            plottype=plot,
            title="Throughput "+titles[plot],
            xlabel=xlabels[plot],
            ylabel=ylabels[plot],
            savepath=plot_path+"/"+measurement+"/",
            show=show_plot)
