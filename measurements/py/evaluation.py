import numpy as np
import myplot
import os

import rtt_belated as rtt
import throughput_belated as tp


measurement             =   [int(os.environ["measurement_counter"])]
links                   =   [int(os.environ["link"])]
repetitions             =   os.environ["repetitions"]
data_source_path        =   os.environ["data_source_path"]+"/"+measurement[0]
plot_path               =   os.environ["plot_directory_path"]
plot_type               =   ["cdf", "boxplot"]
throughput_data_files   =   os.environ["throughput_data_files"]
rtt_data_files          =   os.environ["rtt_data_files"]
retxs_data_files        =   os.environ["retxs_data_files"]
show_plot               =   os.environ["show_plot"]
rtt_mode                =   os.environ["rtt_mode"]

boxplot_xticks      = [ "measurement "+str(idx+1) for idx in range(repetitions)]

legend_labels               = [ tick.replace("\n", ", ") for tick in boxplot_xticks]

custom_legend_coordinates   = {
                                "rtt":          [1,0,"lower right"],
                                "packet_loss":  [1,0,"lower right"],
                                "retxs":        [1,0,"lower right"],
                                "throughput":   [1,0,"lower right"]
                            }

create_plots                = {
                                "rtt":          True,
                                "packet_loss":  True,
                                "retxs":        True,
                                "throughput":   True
                            }

#Unimplemented, use later
annotations_below   = []
annotations_other   = []

for index,a_plot_type in enumerate(plot_type):
    if plot_type[index] == "cdf":
        grid                = True
    else:
        grid                = True

    eval_dict = {
        "measurement":              measurement,
        "repetitions":              repetitions,
        "data_source_path":         data_source_path,
        "plot_path":                plot_path,
        "plot_type":                [plot_type[index]],
        "grid":                     grid,
        "xticks":                   boxplot_xticks,
        "legend":                   legend_labels,
        "annotations_below":        annotations_below,
        "annotations_other":        annotations_other,
        "throughput_data_files":    throughput_data_files,
        "retxs_data_files":         retxs_data_files,
        "rtt_data_files":           rtt_data_files,
        "show_plot":                show_plot,
        "legend_coordinates":       custom_legend_coordinates,
        "create_plots":             create_plots,
        "links":                    links,
        "rtt_mode":                 rtt_mode
    }

    rtt.rtt(**eval_dict).plot()
    tp.tp(**eval_dict).plot()

print("Done.")
