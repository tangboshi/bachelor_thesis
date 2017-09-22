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
# # ALOHA + RB LOW
# measurement     =       [349,348]
# links           =       [1,2]
# boxplot_xticks  = [
#                     "ALOHA\nLink 1 @ 450MHz",
#                     "SIFS=5ms,DIFS=1ms,BO=2ms\nLink 1 @ 450MHz"
#                 ]
# # ALOHA + RB HIGH
measurement     =       [416]#,415]
links           =       [1]#,2]
boxplot_xticks  = [
                     "ALOHA\nLink 1 @ 450MHz"#,
                     #"SIFS=15ms,DIFS=3ms,BO=6ms\nLink 1 @ 450MHz"
                 ]
# # ALOHA + NO BACKOFF
# measurement     =       [352,351]
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
# RB HIGH DUAL
# measurement     =       [341,342]
# links           =       [1,2]
# boxplot_xticks  = [
#                         "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 1 @ 450MHz",
#                         "SIFS=15ms,DIFS=3ms,BO=6ms\nLink 2 @ 450MHz"
#                 ]
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
repetitions             =   5
data_source_path        =   "/home/alex/Schreibtisch/real/measurements/debug/data"
plot_path               =   "/home/alex/Schreibtisch/real/measurements/belated/plots"
plot_type               =   ["cdf", "boxplot", "bar"]
throughput_data_files   =   ["sender_data_sent","sender_ack_received"]
diagnosis_files         =   ["receiver_data_received","receiver_ack_sent"]
#changed the following 2 from string to list
rtt_data_files          =   ["sender_bfr_dq","sender_ack_received"]
retxs_data_files        =   ["sender_retransmissions"]
show_plot               =   False
rtt_mode                =   "rtt"

# boxplot_xticks      = [ "SIFS=3ms\nDIFS=15ms\nBO=6ms\nLink 1 @ 450MHz",
#                          "SIFS=3ms\nDIFS=15ms\nBO=6ms\nLink 2 @ 450MHz"
#                       ]

# boxplot_xticks      = [ "ALOHA\nLink 1 @ 450MHz",
#                         "ALOHA\nLink 2 @ 450MHz",
#                         "ALOHA\nLink 3 @ 450MHz"
#                     ]

legend_labels               = [ tick.replace("\n", ", ") for tick in boxplot_xticks]
custom_legend_coordinates   = {
                                "rtt":                 [0.24,0.85,"upper left"],
                                "packet_loss":         [1,0,"lower right"],
                                "retxs":               [1,0,"lower right"],
                                "throughput":          [1,0,"lower right"],
                                "diagnosis_sender":    [1,0,"lower right"],
                                "diagnosis_receiver":  [1,0,"lower right"],
                                "backoff_csfail":      [1,0,"lower right"]
                            }

create_plots                = {
                                "rtt":              True,
                                "packet_loss":      True,
                                "retxs":            False,
                                "throughput":       True,
                                "diagnostic":       True,
                                "backoff_csfail":   False
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
        "plot_path":                plot_path+"/"+plot_type[index],
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

    if create_plots["backoff_csfail"] == True:
        backoff.backoff(**eval_dict).plot()
    rtt.rtt(**eval_dict).plot()
    tp.tp(**eval_dict).plot()

print("Done.")
