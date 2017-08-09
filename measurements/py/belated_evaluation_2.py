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
# measurement                     = [x+1 for x in range(2)]
# repetitions                     = 8
# data_source_path                = "/home/alex/Schreibtisch/fake/data"
# plot_path                       = "/home/alex/Schreibtisch/fake/plots"
# plot_type                       = ["cdf", "boxplot"]
# throughput_data_files           = ["sender_data_sent.txt","sender_ack_received.txt"]
# rtt_data_files                  = "sender_data_sent.txt,sender_ack_received.txt"
# show_plot                       = False
#
# boxplot_xticks      =   [
#                             "fake1",
#                             "fake2"
#                         ]

#real data parameter set
#measurement             = [x for x in range(207,212)] + [x for x in range (218,220)]
#baseline one link
# measurement             =  [242,246,244]
measurement             =   [40,41]
#links used in the measurement
links                   =   [1,3]
repetitions             =   5
data_source_path        =   "/home/alex/Schreibtisch/real/measurements/debug/data"
plot_path               =   "/home/alex/Schreibtisch/real/measurements/belated/plots"
plot_type               =   ["cdf", "boxplot"]
throughput_data_files   =   ["sender_data_sent","sender_ack_received"]
rtt_data_files          =   "sender_bfr_dq,sender_ack_received"
retxs_data_files        =   "sender_retransmissions"
show_plot               =   False
rtt_mode                =   "frame_delay"

boxplot_xticks      = [ "SIFS=3ms\nDIFS=15ms\nBO=6ms\nLink 1 @ 450MHz",
                         "SIFS=3ms\nDIFS=15ms\nBO=6ms\nLink 3 @ 450MHz"
                         ]

# boxplot_xticks      = [ "SIFS=0ms\nDIFS=0ms\nBO=0ms\nLink 1 @ 450MHz",
#                         "SIFS=0ms\nDIFS=0ms\nBO=0ms\nLink 2 @ 420MHz",
#                         "SIFS=0ms\nDIFS=0ms\nBO=0ms\nLink 3 @ 480MHz"
#                     ]

# boxplot_xticks      = [ "SIFS=3ms\nDIFS=15ms\nBO=6ms",
#                         "SIFS=1ms\nDIFS=5ms\nBO=2ms",
#                         "SIFS=0ms\nDIFS=0ms\nBO=0ms"
#                     ]

# boxplot_xticks      = [ "SIFS=3ms\nDIFS=15ms\nBO=6ms",
#                         "SIFS=3ms\nDIFS=15ms\nBO=0ms",
#                         "SIFS=1ms\nDIFS=5ms\nBO=0ms",
#                         "SIFS=1ms\nDIFS=5ms\nBO=0-100ms (rng)",
#                         "SIFS=1ms\nDIFS=5ms\nBO=50ms",
#                         "SIFS=1ms\nDIFS=5ms\nBO=2ms",
#                         "SIFS=0ms\nDIFS=0ms\nBO=0ms"
#                         ]

legend_labels               = [ tick.replace("\n", ", ") for tick in boxplot_xticks]
custom_legend_coordinates   = {
                                "rtt":          [0.24,0.85,"upper left"],
                                "packet_loss":  [1,0,"lower right"],
                                "retxs":        [1,0,"lower right"],
                                "throughput":   [1,0,"lower right"]
                            }

create_plots                = {
                                "rtt":          True,
                                "packet_loss":  False,
                                "retxs":        False,
                                "throughput":   False
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
