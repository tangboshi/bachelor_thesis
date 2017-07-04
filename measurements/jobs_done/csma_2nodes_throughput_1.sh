# Measurement 0
# protocol: csma two way handshake
# Measured entity: throughput [B]
# SIFS = 1ms
# DIFS = 5ms
# BACKOFF = 2ms
# nodes = 2
TIMER=300
export MEASUREMENT_REPETITIONS=5

MEASUREMENT_SCRIPTS=( csma_80211_I.py csma_80211_II_1.py )
MEASUREMENT_OUTPUT_FILES=( t1DQ.txt t1CS.txt t2RXe.txt t2e.txt )
export MEASUREMENT_OUTPUT_FILES=${MEASUREMENT_OUTPUT_FILES[*]}
PLOT_SCRIPTS=( cdf.py )
## Plot options
PLOT_ENABLED=1
export PLOT_SAVE_ENABLED=1
# The name of the saved files
export PLOT_NAMES_TRUNK=throughput
