import matplotlib.pyplot as plt
import numpy as np

# ALOHA vs. CSMA vs. reservation-based
a                           = 0.04
Gmax                        = 7
G                           = np.arange(0,Gmax,0.01)
S_pure_ALOHA                = G*np.exp(-2*G)
S_slotted_ALOHA             = G*np.exp(-G)
S_non_pers_CSMA             = G*np.exp(-a*G)/(G*(1+2*a)+np.exp(-a*G))
S_slotted_non_pers_CSMA     = a*G*np.exp(-a*G)/(1-np.exp(-a*G)+a)
S_1_pers_CSMA               = G*(1+G+a*G*(1+G+(a/2*G)))*np.exp(-G*(1+2*a))/(G*(1+2*a)-(1-np.exp(-a*G))+(1+a*G)*np.exp(-G*(1+a)))
S_slotted_1_pers_CSMA       = G*np.exp(-G*(1+a))*(1+a-np.exp(-a*G))/((1+a)*(1-np.exp(-a*G))+a*np.exp(-G*(1+a)))
S_reservation_based         = 0.5*(1*(1-np.sign(1-G))+G*(1-np.sign(G-1)))

S_non_pers_CSMA_no_delay    = G/(G+1)
S_1_pers_CSMA_no_delay      = G*(1+G)*np.exp(-G)/(G+np.exp(-G))

fig, ax = plt.subplots(figsize=(10,6))
plt.plot(G,S_pure_ALOHA,label="pure ALOHA")
plt.plot(G,S_slotted_ALOHA,label="slotted ALOHA",linestyle="dashed")
plt.plot(G,S_non_pers_CSMA_no_delay,label="unslotted non-persistent CSMA, a=0",linestyle="dashdot")
plt.plot(G,S_non_pers_CSMA,label="unslotted non-persistent CSMA, a=0.04",linestyle="dotted")
plt.plot(G,S_slotted_non_pers_CSMA,label="slotted non-persistent CSMA, a=0.04")
plt.plot(G,S_1_pers_CSMA_no_delay,label="unslotted 1-persistent CSMA, a=0",linestyle="dashed")
plt.plot(G,S_1_pers_CSMA,label="unslotted 1-persistent CSMA, a=0.04",linestyle="dashdot")
plt.plot(G,S_slotted_1_pers_CSMA,label="slotted 1-persistent CSMA, a=0.04")
plt.plot(G,S_reservation_based,label="reservation-based",linestyle="dashed",color="black")

ax.xaxis.grid(True, linestyle="dashdot")
ax.yaxis.grid(True, linestyle="dashdot")
ax.set_xlabel("offered load G")
ax.set_ylabel("normalized throughput S")
ax.set_xlim(xmin=0,xmax=xmax)
ax.set_ylim(ymin=0,ymax=1.1)
ax.set_xticks(np.arange(0,xmax,0.5))
ax.set_yticks(np.arange(0,1.1,0.1))
plt.legend(loc=4,bbox_to_anchor=(1,0.1))
plt.tight_layout()
plt.show()
