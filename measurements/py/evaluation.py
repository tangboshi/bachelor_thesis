import numpy as np
import myplot
import os

import rtt_belated as rtt
import throughput_belated as tp
import channel_occupation as channel_occupation
import backoff
import sniffer


measurement             =   [int(os.environ["measurement_counter"])]
links                   =   [int(os.environ["link"])]
repetitions             =   int(os.environ["measurement_repetitions"])
data_source_path        =   os.environ["data_source_path"]
plot_path               =   os.environ["plot_directory_path"]+"/"+os.environ["measurement_counter"]+"/"
plot_type               =   ["cdf", "boxplot", "bar"]
throughput_data_files   =   os.environ["throughput_data_files"].split(",")
rtt_data_files          =   os.environ["rtt_data_files"].split(",")
co_data_files           =   os.environ["co_data_files"].split(",")
sniffer_data_files      =   os.environ["sniffer_data_files"].split(",")
retxs_data_files        =   os.environ["retxs_data_files"].split(",")
show_plot               =   int(os.environ["show_plot_after_measurement"])
rtt_mode                =   os.environ["rtt_mode"]
max_retxs               =   6
eval_mode               =   "live"
timer                   =   int(os.environ["timer"])

boxplot_xticks              = [ "measurement "+str(index) for index in measurement ]

legend_labels               = [ tick.replace("\n", ", ") for tick in boxplot_xticks]

custom_legend_coordinates   = {
                                "rtt":                 [0.24,0.85,"upper left"],
                                "packet_loss":         [1,0,"lower right"],
                                "retxs":               [1,0,"lower right"],
                                "throughput":          [1,0,"lower right"],
                                "diagnosis_sender":    [1,0,"lower right"],
                                "diagnosis_receiver":  [1,0,"lower right"],
                                "backoff_csfail":      [1,0,"lower right"],
                                "channel_occupation":  [1,0,"lower right"],
                                "sniffer":             [1,0,"lower right"]
                            }

create_plots                = {
                                "rtt":                  True,
                                "packet_loss":          True,
                                "retxs":                False,
                                "throughput":           True,
                                "diagnostic":           True,
                                "backoff_csfail":       True,
                                "channel_occupation":   True,
                                "sniffer":              True
                            }

channel_occupation_mode     =   {
                                    "occupation_mode":  ["overview", "zoom"],
                                    "zoom":             [0,1]
                                }

sniffer_settings            =   {
                                    "link":     2
                                }

#Unimplemented, use later
annotations_below   = []
annotations_other   = []

eval_dict = {
    "measurement":              measurement,
    "repetitions":              repetitions,
    "data_source_path":         data_source_path,
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
    "rtt_mode":                 rtt_mode,
    "channel_occupation_mode":  channel_occupation_mode,
    "co_data_files":            co_data_files,
    "sniffer_data_files":       sniffer_data_files,
    "sniffer_settings":         sniffer_settings,
    "timer":                    timer
}

for index,a_plot_type in enumerate(plot_type):
    if plot_type[index] == "cdf":
        grid                = True
    else:
        grid                = True

    eval_dict["plot_type"]  = [plot_type[index]]
    eval_dict["plot_path"]  = plot_path
    eval_dict["grid"]       = grid

    if create_plots["backoff_csfail"] == True:
        print("_______________________________________________________________")
        print("Creating backoff (cs fail) plot!")
        print("***************************************************************")
        backoff.backoff(**eval_dict).plot()
    # FIXME: diagnostic, packet_loss and retxs plots can only be created if rtt is True.
    if create_plots["rtt"] == True:
        print("_______________________________________________________________")
        print("Creating rtt plot!")
        print("***************************************************************")
        rtt.rtt(**eval_dict).plot()
    if create_plots["throughput"] == True:
        print("_______________________________________________________________")
        print("Creating throughput plot!")
        print("***************************************************************")
        tp.tp(**eval_dict).plot()

# The plots with only one plot type!
if create_plots["channel_occupation"] == True:
    print("_______________________________________________________________")
    print("Creating channel occupation plot!")
    print("***************************************************************")
    channel_occupation.channel_occupation(**eval_dict)
if create_plots["sniffer"] == True:
    print("_______________________________________________________________")
    print("Creating sniffer energy plot!")
    print("***************************************************************")
    sniffer.sniffer(**eval_dict)

print("Done.")
