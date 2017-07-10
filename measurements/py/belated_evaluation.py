import numpy as np
import process_file
import myplot

## Get all required information from OS
try:
    from variables import (
        data_source_path,
        throughput_data_files,
        rtt_data_files,
        plot_path,
        show_plot
    )
except ImportError:
    print("Probably not all data were imported correctly!")
    print(ImportError)

# Modify these variables
measurement = 95
repetitions = 15 # be sure to have the correct value here
data_file_names = ["sender_bfr_dq.txt", "sender_ack_received.txt"]
plot_type = "pdf"
processing_scheme = "rtt"
xlabel = "fancyness"
ylabel= "awesomeness"
title = "super nice"
show_plot = False
savepath = plot_path+"/"+str(measurement)+"/"

# Don't modify these variables
data_source_path += "/"+str(measurement)

#Testing
print(data_source_path)
print(rtt_data_files)

## Trigger data processing
data = []
paths = []
for i in range(1,repetitions+1):
    for filename in data_file_names:
        paths.append(data_source_path+"/"+str(i)+"/"+filename)
    data += process_file.process_file(files=paths, mode=processing_scheme);

## Trigger the plotting
myplot.myplot(  data=data,
                bins=np.arange(
                        min(data),
                        max(data)),
                plottype=plot_type,
                xlabel=xlabel,
                ylabel=ylabel,
                title=title,
                show=show_plot,
                savepath=savepath)
