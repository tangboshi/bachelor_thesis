import numpy as np
import os
from pylab import *
import matplotlib.pyplot as plt
import subprocess

print("Hello from cdf.py!")

## Get all required information from OS
measurement         = os.environ["MEASUREMENT_COUNTER"]
repetitions         = int(os.environ["MEASUREMENT_REPETITIONS"])
data_source_path    = os.environ["DATA_SOURCE_PATH"]+"/"+measurement
plot_path           = os.environ["PLOT_DIRECTORY_PATH"]
trunk               = os.environ["PLOT_NAMES_TRUNK"]
packet_size         = int(os.environ["PACKET_SIZE"])
show_plot           = int(os.environ["SHOW_PLOT_AFTER_MEASUREMENT"])

# Create a repetitions X 1 matrix aka row vector with measurement data
data = np.zeros(shape=(repetitions))

for i in range(1,repetitions+1):
    file_path = data_source_path+'/'+str(i)+'/'+'frames_sent.txt'
    linecount = subprocess.run(['wc', '-l', file_path], stdout=subprocess.PIPE)
    linecount = linecount.stdout.decode('utf-8')
    linecount = linecount.partition(" ")[0]
    linecount = int(linecount)
    data[i-1] = linecount*packet_size
print(data)

#************************************ PDF *************************************
fig, ax = plt.subplots()

n, bins, patches = ax.hist(x=data, bins=repetitions, normed=1, histtype='bar',
                           cumulative=False, label='PDF')
# Save figures to location
#if os.environ["PLOT_SHOW"] == "1":
fig.savefig(plot_path+"/"+measurement+"/"+trunk+"_pdf.png")
fig.savefig(plot_path+"/"+measurement+"/"+trunk+"_pdf.pdf")
if show_plot:
    plt.show()
#******************************************************************************

#************************************ CDF *************************************
fig2, ax2 = plt.subplots()
n, bins, patches = ax2.hist(x=data, bins=repetitions, normed=1, histtype='step',
                           cumulative=True, label='CDF')
# Save figures to location
#if os.environ["PLOT_SHOW"] == "1":
fig2.savefig(plot_path+"/"+measurement+"/"+trunk+"_cdf.png")
fig2.savefig(plot_path+"/"+measurement+"/"+trunk+"_cdf.pdf")
if show_plot:
    plt.show()
#******************************************************************************
