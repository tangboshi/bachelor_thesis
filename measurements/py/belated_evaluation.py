import numpy as np
import myplot

import rtt
import throughput as tp
import channel_occupation
import backoff
import sniffer

# custom legend_coordinates
# [0] = rtt
# [1] = packet loss
# [2] = retransmissions / frame
# [3] = throughput

# fake data parameter set
# measurement                     = [x+1 for x in range(2)]
# links                           = [1,2]
# repetitions                     = 8
# data_source_path                = "/home/alex/Schreibtisch/fake/data"
# plot_path                       = "/home/alex/Schreibtisch/fake/plots"
# plot_type                       = ["cdf", "boxplot"]
# throughput_data_files           = ["sender_data_sent.txt","sender_ack_received.txt"]
# rtt_data_files                  = "sender_data_sent.txt,sender_ack_received.txt"
# retxs_data_files                = ["sender_retransmissions"]
# rtt_mode                        = "rtt"
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
# measurement             =   [345,346,347]
# links used in the measurement
# links                   =   [1,2,3]
############ plotting preparation ############
# # RB HIGH SINGLE
# measurement     =       [13,10,11]
# links           =       [1,2,3]
# boxplot_xticks  = [
#                         "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 1 @ 450MHz",
#                         "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 2 @ 420MHz",
#                         "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 3 @ 480MHz"
#                 ]
# # NO BACKOFF SINGLE
# measurement     =       [3,14,5]
# links           =       [1,2,3]
# boxplot_xticks  = [
#                         "SIFS=15ms,DIFS=3ms,BO=0ms\nLink 1 @ 450MHz",
#                         "SIFS=15ms,DIFS=3ms,BO=0ms\nLink 2 @ 420MHz",
#                         "SIFS=15ms,DIFS=3ms,BO=0ms\nLink 3 @ 480MHz"
#                 ]
# # NO WAIT SINGLE
# measurement     =       [6,12,8]
# links           =       [1,2,3]
# boxplot_xticks  = [
#                         "SIFS=0ms,DIFS=0ms,BO=0ms\nLink 1 @ 450MHz",
#                         "SIFS=0ms,DIFS=0ms,BO=0ms\nLink 2 @ 420MHz",
#                         "SIFS=0ms,DIFS=0ms,BO=0_ ams\nLink 3 @ 480MHz"
#                 ]
#ALOHA SINGLE
# measurement     =       [208,209,210]
# links           =       [1,2,3]
# boxplot_xticks  = [
#                     "ALOHA\nLink 1 @ 450MHz",
#                     "ALOHA\nLink 2 @ 420MHz",
#                     "ALOHA\nLink 3 @ 480MHz"
#                 ]
# # RB LOW SINGLE
# measurement     =       [345,346,347]
# links           =       [1,2,3]
# boxplot_xticks  = [
#                         "SIFS=5ms,DIFS=1ms,BO=2ms\nLink 1 @ 450MHz",
#                         "SIFS=5ms,DIFS=1ms,BO=2ms\nLink 2 @ 420MHz",
#                         "SIFS=5ms,DIFS=1ms,BO=2ms\nLink 3 @ 480MHz"
#                  ]
#ALOHA + RB LOW
# measurement     =       [349,348]
# links           =       [1,2]
# boxplot_xticks  = [
#                     "ALOHA\nLink 1 @ 450MHz",
#                     "SIFS=5ms,DIFS=1ms,BO=2ms\nLink 2 @ 450MHz"
#                 ]
# # ALOHA + RB HIGH
# measurement     =       [416,415]
# links           =       [1,2]
# boxplot_xticks  = [
#                      "ALOHA\nLink 1 @ 450MHz",
#                      "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 1 @ 450MHz"
#                  ]
# # # ALOHA + NO BACKOFF
# measurement     =       #[352,351]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "ALOHA\nLink 1 @ 450MHz",
#                     "SIFS=5ms,DIFS=1ms,BO=0ms\nLink 1 @ 450MHz"
#                 ]
# # RB LOW DUAL
# measurement     =       [344,343]
# links           =       [1,2]
# boxplot_xticks  = [
#                         "SIFS=5ms,DIFS=1ms,BO=2ms\nLink 1 @ 450MHz",
#                         "SIFS=5ms,DIFS=1ms,BO=2ms\nLink 2 @ 450MHz"
#                 ]
#RB HIGH DUAL
# measurement     =       [341,342]
# links           =       [1,2]
# boxplot_xticks  = [
#                         "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 1 @ 450MHz",
#                         "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 2 @ 450MHz"
#                  ]
# # NO BACKOFF DUAL
# measurement     =       [?,?]
# links           =       [1,2]
# boxplot_xticks  = [
#                         "SIFS=15ms,DIFS=3ms,BO=0ms\nLink 1 @ 450MHz",
#                         "SIFS=15ms,DIFS=3ms,BO=0ms\nLink 2 @ 450MHz"
#                 ]
# # ALOHA DUAL
# measurement     =       [355,354]
# links           =       [1,2]
# boxplot_xticks  = [
#                     "ALOHA\nLink 1 @ 450MHz",
#                     "ALOHA\nLink 2 @ 450MHz"
#                 ]
############ ~~~~~~~~~~~~~~~~~~~  ############

# measurement     =       [630,631]
# links           =       [1,2]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=5ms\nSIFS=1ms\nBO=2ms\nLink 1 @ 450MHz",
#                     "CSMA\nDIFS=5ms\nSIFS=1ms\nBO=2ms\nLink 2 @ 450MHz"
#                 ]

measurement     =       [619,620,720,724]
links           =       [1,2,1,2]
boxplot_xticks  = [
                    "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 1 @ 450MHz",
                    "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 2 @ 450MHz",
                    "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 1 @ 450MHz\n Baseline",
                    "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 2 @ 450MHz\n Baseline",
                ]

# measurement     =       [638,639]
# links           =       [1,2]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=9ms\nSIFS=1ms\nBO=2ms\nLink 1 @ 450MHz",
#                     "CSMA\nDIFS=9ms\nSIFS=1ms\nBO=2ms\nLink 2 @ 450MHz"
#                 ]

# measurement     =       [644,643]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=9ms\nSIFS=1ms\nBO=2ms\nLink 1 @ 450MHz",
#                     "ALOHA saturated\nLink 2 @ 450MHz"
#                 ]

# measurement     =       [648,647]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=9ms\nSIFS=1ms\nBO=2ms\nLink 1 @ 450MHz",
#                     "ALOHA unsaturated\nLink 2 @ 450MHz"
#                 ]

# measurement     =       [667,666]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 1 @ 450MHz",
#                     "ALOHA unsaturated\nLink 2 @ 450MHz"
#                 ]

# measurement     =       [661,660]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA unsaturated\nDIFS=9ms\nSIFS=1ms\nBO=2ms\nLink 1 @ 450MHz",
#                     "ALOHA unsaturated\nLink 2 @ 450MHz"
#                 ]

# measurement     =       [665,664]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA unsaturated\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 1 @ 450MHz",
#                     "ALOHA unsaturated\nLink 2 @ 450MHz"
#                 ]

# measurement     =       [632,633]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 1 @ 450MHz",
#                     "CSMA\nDIFS=5ms\nSIFS=1ms\nBO=2ms\nLink 2 @ 450MHz"
#                 ]

# measurement     =       [634,635]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 1 @ 450MHz",
#                     "CSMA\nDIFS=7.5ms\nSIFS=1ms\nBO=2ms\nLink 2 @ 450MHz"
#                 ]
#
# measurement     =       [637,636]
# links           =       [2,1]
# boxplot_xticks  = [
#                     "CSMA\nDIFS=15ms\nSIFS=3ms\nBO=6ms\nLink 1 @ 450MHz",
#                     "CSMA\nDIFS=9ms\nSIFS=1ms\nBO=2ms\nLink 2 @ 450MHz"
#                 ]
#From "Bash"
repetitions             =   5
data_source_path        =   "/home/alex/Schreibtisch/teebs/measurements/debug/data"
plot_path               =   "/home/alex/Schreibtisch/teebs/measurements/belated/plots"
plot_type               =   ["cdf", "boxplot"]
throughput_data_files   =   ["receiver_data_received","sender_ack_received"]
diagnosis_files         =   ["receiver_data_received","receiver_ack_sent"]
#changed the following 2 from string to list
rtt_data_files          =   ["sender_bfr_dq","sender_ack_received","receiver_ack_sent"]
co_data_files           =   ["sender_bfr_dq","receiver_ack_sent","sender_ack_received"]
sniffer_data_files      =   ["sniffer"]
retxs_data_files        =   ["sender_retransmissions"]
show_plot               =   False
rtt_mode                =   "frame_delay"
receiver_mode           =   "single"
timer                   =   100

#From Python
plot_pdf                =   False
#boxplot_xticks          =   [ "measurement "+str(index) for index in measurement ]
legend_labels           =   [ tick.replace("\n", ", ") for tick in boxplot_xticks ]

custom_legend_coordinates   = {
                                "rtt":                 [0.24,0.85,"upper left"],
                                "packet_loss":         [1,0,"lower right"],
                                "retxs":               [1,0,"lower right"],
                                "throughput":          [1,0,"lower right"],
                                "diagnosis_sender":    [1,0,"lower right"],
                                "diagnosis_receiver":  [1,0,"lower right"],
                                "backoff":             [1,0,"lower right"],
                                "channel_occupation":  [1,0,"lower right"],
                                "sniffer":             [1,0,"lower right"]
                            }

create_plots                = {
                                "rtt":                  True,
                                "packet_loss":          False,
                                "retxs":                False,
                                "throughput":           False,
                                "diagnostic":           False,
                                "backoff":              False,
                                "channel_occupation":   False,
                                "sniffer":              False
                            }

# create_plots                = {
#                                 "rtt":                  True,
#                                 "packet_loss":          False,
#                                 "retxs":                False,
#                                 "throughput":           True,
#                                 "diagnostic":           False,
#                                 "backoff":              True,
#                                 "channel_occupation":   True,
#                                 "sniffer":              True
#                             }

channel_occupation_mode     =   {
                                    "occupation_mode":  ["overview", "zoom"],
                                    "zoom":             [5,7],
                                    "zoom_mode":        "interval",
                                    "zoom_interval":    2
                                }

#FIXME: link obsolete, remove
sniffer_settings            =   {
                                    "sniffer_mode":             ["smoothed"],
                                    "link":                     1,
                                    "zoom":                     [0.0,timer*repetitions],
                                    "zoom_mode":                "interval",
                                    "zoom_interval":            2,
                                    "smoothing_difference":     0.0001,
                                    "smoothing_derivative":     0.01,
                                    "smoothing_range":          [0.0010,0.0013]
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
    "plot_pdf":                 plot_pdf,
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

    if create_plots["backoff"] == True:
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
