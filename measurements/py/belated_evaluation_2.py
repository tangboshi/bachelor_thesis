import numpy as np
import myplot

import rtt_3 as rtt

### Parameters, change these to fit your needs

#measurement        = [x for x in range(5)] + [12] + [x for x in range (14,17)]
measurement         = [x+1 for x in range(2)]
repetitions         = 8
data_source_path    = "/home/alex/Schreibtisch/data"
plot_path           = "/home/alex/Schreibtisch/plots"
plot_type           = ["pdf","cdf"]

eval_dict = {
    "measurement":          measurement,
    "repetitions":          repetitions,
    "data_source_path":     data_source_path,
    "plot_path":            plot_path,
    "plot_type":            plot_type,
}

# print (repetitions)
# print (repetitions[0])
# for item in repetitions:
#     print (item)

rtt.rtt(**eval_dict).plot()
