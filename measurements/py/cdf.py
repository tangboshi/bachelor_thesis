import numpy as np
import os
from pylab import *
import matplotlib.pyplot as plt

# Create some test data
dx = .01
X  = np.arange(-2,2,dx)
Y  = exp(-X**2)

# Normalize the data to a proper PDF
Y /= (dx*Y).sum()

# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
fig, ax = plt.subplots()
ax.plot(X,Y, 'r', label="troughput pdf")
ax.plot(X,CY,'b--', label="throughput cdf")

legend = ax.legend(loc='upper left', shadow=False)

plt.title("Troughput CDF 300s")
plt.xlabel("throughput")

# Save figures to location
if os.environ["PLOT_SAVE_ENABLED"] == "1":
    path = os.environ["PLOT_DIRECTORY_PATH"]
    measurement = os.environ["MEASUREMENT_COUNTER"]
    trunk = os.environ["PLOT_NAMES_TRUNK"]
    plt.savefig(path+"/"+measurement+"/"+trunk+".png")
    plt.savefig(path+"/"+measurement+"/"+trunk+".pdf")

print(path)
print(measurement)
print(trunk)

#plt.show()
