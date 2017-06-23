# This whole file has been created solely for testing purposes
# What it does is creating dummy files in a locatiom that will be moved
# by a shell script

import os
import numpy as np
import time

print("Hello from fake_measurements/measure.py!")

raw_data_source_path    =   os.environ["RAW_DATA_SOURCE_PATH"]
#raw_data_source_path = "/home/alex/0_ba/git/measurements/py/fake_measurements/measurement_raw"
#print("raw_data_source_path evaluated to: "+raw_data_source_path)

#trunk                  =   os.environ["PLOT_NAMES_TRUNK"]

# Create one random number N with exponentially distributed value
# Sounds confusing? This script is actually called $MEASUREMENT_REPETITIONS times
N = np.random.poisson(50000,1)
N = N.astype(np.int64)

## Write N number of lines with current timestamp to file
# Create File
file = open(raw_data_source_path+"/raw.dat", "w")

# For a more realistic output wait exponentially distributed times between writes
for i in range(1,N[0]+1):
    file.write(str(time.time())+"\n")
