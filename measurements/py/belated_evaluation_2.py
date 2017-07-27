import numpy as np
import myplot

import rtt_belated as rtt
import throughput_belated as tp

# fake data parameter set
# measurement             = [x+1 for x in range(2)]
# repetitions             = 8
# data_source_path        = "/home/alex/Schreibtisch/fake/data"
# plot_path               = "/home/alex/Schreibtisch/fake/plots"
# plot_type               = ["boxplot"]
# throughput_data_files   = ["sender_data_sent.txt","sender_ack_received.txt"]
# rtt_data_files          = "sender_data_sent.txt,sender_ack_received.txt"

# real data parameter set
measurement             = [x for x in range(207,212)] + [218]
repetitions             = 5
data_source_path        = "/home/alex/Schreibtisch/real/measurements/debug/data"
plot_path               = "/home/alex/Schreibtisch/real/measurements/belated/plots"
plot_type               = ["cdf","cdf2","boxplot", "pdf"]
throughput_data_files   = ["sender_data_sent.txt","sender_ack_received.txt"]
rtt_data_files          = "sender_bfr_dq.txt,sender_ack_received.txt"

boxplot_xticks      = [ "SIFS=3ms\nDIFS=15ms\nBO=6ms",
                        "SIFS=3ms\nDIFS=15ms\nBO=0ms",
                        "SIFS=1ms\nDIFS=5ms\nBO=0ms",
                        "SIFS=1ms\nDIFS=5ms\nBO=0-100ms (rng)",
                        "SIFS=1ms\nDIFS=5ms\nBO=50ms",
                        "SIFS=1ms\nDIFS=5ms\nBO=2ms"
                        ]
legend_labels       = [ tick.replace("\n", ", ") for tick in boxplot_xticks]
legend_loc          = "upper left"
show_plot           = False

#Unimplemented, use later
annotations_below   = [ "Comments on this plot:",
                        "Timer: 300s",
                        "Repetitions: 5"]
annotations_other   = []

if "cdf" in plot_type:
    grid                = False
else:
    grid                = True

for index,a_plot_type in enumerate(plot_type):
    eval_dict = {
        "measurement":              measurement,
        "repetitions":              repetitions,
        "data_source_path":         data_source_path,
        "plot_path":                plot_path,
        "plot_type":                [plot_type[index]],
        "grid":                     grid,
        "xticks":                   boxplot_xticks,
        "legend":                   legend_labels,
        "legend_loc":               legend_loc,
        "annotations_below":        annotations_below,
        "annotations_other":        annotations_other,
        "throughput_data_files":    throughput_data_files,
        "rtt_data_files":           rtt_data_files,
        "show_plot":                show_plot
    }

    rtt.rtt(**eval_dict).plot()
    tp.tp(**eval_dict).plot()

print("Done.")
