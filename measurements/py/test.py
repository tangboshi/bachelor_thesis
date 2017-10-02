import matplotlib.pyplot as plt
import numpy as np

# ALOHA's performance
x = np.arange(0,5,0.01)
y = x*np.exp(-2*x)
y2 = x*np.exp(-x)

fig, ax = plt.subplots()
plt.plot(x,y,label="Pure ALOHA")
plt.plot(x,y2,label="Slotted ALOHA")
ax.xaxis.grid(True, linestyle="dashdot")
ax.yaxis.grid(True, linestyle="dashdot")
ax.set_xlabel("G [attempts per packet time]")
ax.set_ylabel("S [throughput per packet time]")
ax.set_yticks(np.arange(0,0.5,0.18))
ax.set_xticks(np.arange(0,5.1,0.5))
plt.legend(loc=1)
plt.tight_layout()
plt.show()
