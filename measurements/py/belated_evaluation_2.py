import numpy as np
import myplot

import rtt_belated as rtt
import throughput_belated as tp

# custom legend_coordinates
# [0] = rtt
# [1] = packet loss
# [2] = retransmissions / frame
# [3] = throughput

# fake data parameter set
# measurement             = [x+1 for x in range(2)]
# repetitions             = 8
# data_source_path               = "/home/alex/Schreibtisch/fake/data"
# plot_path                      = "/home/alex/Schreibtisch/fake/plots"
# plot_type                      = ["cdf"]
# throughput_data_files          = ["sender_data_sent.txt","sender_ack_received.txt"]
# rtt_data_files                 = "sender_data_sent.txt,sender_ack_received.txt"
# show_plot                      = False
#
# custom_legend_coordinates      = [[0,1,"upper left"], [0,1,"upper left"], [1,0,"lower right"], [1,0,"lower right"]]
#
# boxplot_xticks      =   [
#                             "fake1",
#                             "fake2"
#                         ]

#real data parameter set
measurement             = [x for x in range(207,212)] + [x for x in range (218,220)]
repetitions             = 5
data_source_path        = "/home/alex/Schreibtisch/real/measurements/debug/data"
plot_path               = "/home/alex/Schreibtisch/real/measurements/belated/plots"
plot_type               = ["cdf", "boxplot"]
throughput_data_files   = ["sender_data_sent.txt","sender_ack_received.txt"]
rtt_data_files          = "sender_bfr_dq.txt,sender_ack_received.txt"
show_plot               = False

boxplot_xticks      = [ "SIFS=3ms\nDIFS=15ms\nBO=6ms",
                        "SIFS=3ms\nDIFS=15ms\nBO=0ms",
                        "SIFS=1ms\nDIFS=5ms\nBO=0ms",
                        "SIFS=1ms\nDIFS=5ms\nBO=0-100ms (rng)",
                        "SIFS=1ms\nDIFS=5ms\nBO=50ms",
                        "SIFS=1ms\nDIFS=5ms\nBO=2ms",
                        "SIFS=0ms\nDIFS=0ms\nBO=0ms"
                        ]

legend_labels               = [ tick.replace("\n", ", ") for tick in boxplot_xticks]
custom_legend_coordinates   = [
                                [0,1,"upper left"], 
                                [0,1,"upper left"],
                                [1,0,"lower right"],
                                [1,0,"lower right"]
                            ]

#Unimplemented, use later
annotations_below   = [ "Comments on this plot:",
                        "Timer: 300s",
                        "Repetitions: 5"]
annotations_other   = []

for index,a_plot_type in enumerate(plot_type):
    if plot_type[index] == "cdf":
        grid                = False
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
        "rtt_data_files":           rtt_data_files,
        "show_plot":                show_plot,
        "legend_coordinates":       custom_legend_coordinates
    }

    rtt.rtt(**eval_dict).plot()
    tp.tp(**eval_dict).plot()

print("Done.")
