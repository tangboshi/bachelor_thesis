#import sys
#print(sys.version)

'''
import random
import numpy as np
import os
import matplotlib.pyplot as plt
'''

'''
mystr = "abc def ghi jkl mno pqr stu vwx yz"
mystr = mystr.split()
print(mystr)
'''

data_1 =    [
                1,2,4,5,6,2,4,7,8,1,2,9,17,2,3,5,6,8,2,6,12,19,16,
                13,8,14,25,1,2,7,5,10,13,17,7,2,
            ]
data_2 =    [
                9,5,12,25,24,6,7,2,0,9,13,17,2,18,5,4,17,19,13,10,4,
                4,2,7,6,19,5,8,8,12,4,0,22,23
            ]

#repetitions = len(data)

'''
fig, ax = plt.subplots()

n, bins, patches = ax.hist(x=data, bins=repetitions, normed=1, histtype='bar',
                           cumulative=False, label='PDF')

ax.set_title("My random title")
ax.set_ylabel("Fancyness")
ax.set_xlabel("Awesomeness")

plt.show()
'''

'''
myDict = {
0: lambda: print("hello"),
1: lambda: print("world"),
2: lambda: print("!"),
"Somerandomword": lambda: print("Take this!")
}

myDict[0]()
myDict[1]()
myDict["Somerandomword"]()
'''

# import myplot
# #fancyplot = myplot.myplot(data=data, bins=repetitions, plottype="pdf")
# fancyplot = myplot.myplot(data=data, plottype="boxplot")
# fancyplot.setLabels(xlabel="awesomeness", ylabel="fancyness", title="Fancyplot")
# fancyplot.show()

#mystring ="abc"
#result = mystring.split(",")
#print(result)

# a = [1,2]
# b = a
# a = []

#a = [1,2]
#b = a
#del a[:]
# print(a)
# print(b)

# a = [0.0025, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025]
# mean = float(sum(a)) / len(a)
# print(mean)

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.random.normal(size=100)
# n, bins, patches = plt.hist(x)
# cm = plt.cm.get_cmap('jet')
# for index, patch in enumerate(patches):
#     plt.setp(patch, 'facecolor', cm(float(index/len(patches))))
#
# plt.show()

# import subprocess
# p = subprocess.run("./test.sh", stdout=subprocess.PIPE)
# for line in p.stdout:
#     print(line)

# import os
#
# if os.environ.get('Foo') is not None:
#     measurement         = os.environ["MEASUREMENT_COUNTER"]
# else:
#     measurement = "abc"
#
# print(measurement)

# import myplot
# fancyplot = myplot.myplot(data=data, bins=repetitions, plottype="pdf")
# fancyplot = myplot.myplot(data=data, plottype="line")
# fancyplot.setLabels(xlabel="awesomeness", ylabel="fancyness", title="Fancyplot")
# fancyplot.show()

# def my_func(**kwargs):
# 	for name, value in kwargs.items():
# 		print( "{0} = {1}".format(name,value) )
#
# # let's cal this function
# my_dict = { "fruits": ["apple","banana"], "vegetables": ["tomato", "cucumber"]}
# my_func(**my_dict)

# import myplot
# import numpy as np
#
# frames  =      100
# data    =      []
# line    =      "1 3 5 2 0 1 2 6 7 8 2"
# line    =      [int(item) for item in line.split()]
# data    +=     [item for item in line]
# #print(data)
#
# myplot.myplot(data=data,
#         bins=np.arange(
#             min(data)-1,
#             max(data)+1),
#         plottype="pdf",
#         title="fancy plot",
#         xlabel="fancyness",
#         ylabel="awesomeness",
#         show=True)

# my_dict = { "A": 1, "B": 5, "C": 7}
#
# print(dict_deref.items())

# import numpy as np
# import statsmodels.api as sm # recommended import according to the docs
# import matplotlib.pyplot as plt
#
# sample = np.random.uniform(0, 1, 50)
# ecdf = sm.distributions.ECDF(sample)
#
# x = np.linspace(min(sample), max(sample))
# y = ecdf(x)
# plt.step(x, y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# arr = [0,1,2,2]
# plt.plot(np.sort(arr), np.linspace(0,1,len(arr), endpoint=False))
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Some fake data:
# data = np.random.randn(1000)
#
# sorted_data = np.sort(data)  # Or data.sort(), if data can be modified
#
# # Cumulative distributions:
# plt.step(np.concatenate([sorted_data, sorted_data[[-1]]]),
#          np.arange(sorted_data.size+1))
# plt.step(np.concatenate([sorted_data[::-1], sorted_data[[0]]]),
#          np.arange(sorted_data.size+1))
#
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# arr = np.zeros(shape=(2,8))
# arr[0,0] = 0
# arr[0,1] = 7
# arr[0,2] = 19
# arr[0,3] = 6
# arr[0,4] = -12
# arr[0,5] = 14
# arr[0,6] = 13
# arr[0,7] = 8
# arr[1,0] = 4
# arr[1,1] = 12
# arr[1,2] = 3
# arr[1,3] = 5
# arr[1,4] = 7
# arr[1,5] = 1
# arr[1,6] = -4
# arr[1,7] = 4
# print(arr)
#
# plt.boxplot(arr)
# plt.show()

# import matplotlib.pyplot as plt
#
# plt.subplot(211)
# plt.boxplot([1,2,3], label="test1")
# plt.boxplot([3,2,1], label="test2")
# # Place a legend above this subplot, expanding itself to
# # fully use the given bounding box.
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#            ncol=2, mode="expand", borderaxespad=0.)
#
# plt.subplot(223)
# plt.plot([1,2,3], label="test1")
# plt.plot([3,2,1], label="test2")
# # Place a legend to the right of this smaller subplot.
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#
# plt.show()

#CDF!!
# import numpy as np
# import matplotlib.pyplot as plt
#
# data =  [
#             np.random.choice(100000,3) for x in range(3)
#         ]
#
# for index,item in enumerate(data):
#     x = np.sort(item)
#     y = np.arange(1,len(x)+1) / len(x)
#     plt.plot(x,y,marker='x')
#
# print(data)
# plt.margins(0.02)
# plt.show()

# x1 = np.sort(data_1)
# x2 = np.sort(data_2)
# y1 = np.arange(1, len(x1)+1) / len(x1)
# y2 = np.arange(1, len(x2)+1) / len(x2)
# plt.plot(x1,y1, marker='x', color='r')
# plt.plot(x2,y2, marker='x', color='b')
# plt.margins(0.02)
# plt.show()

# arr1 = [0,2,2]
# arr2 = [5,4,7]
# data = []
# data.append(arr1)
# data.append(arr2)
# print(data)

# import numpy as np
# import matplotlib
# from matplotlib.patches import Circle, Wedge, Polygon
# from matplotlib.collections import PatchCollection
# import matplotlib.pyplot as plt
#
# # Fixing random state for reproducibility
# np.random.seed(1223141536)
#
#
# fig, ax = plt.subplots()
#
# resolution = 50  # the number of vertices
# N = 3
# x = np.random.rand(N)
# y = np.random.rand(N)
# radii = 0.1*np.random.rand(N)
# patches = []
# for x1, y1, r in zip(x, y, radii):
#     circle = Circle((x1, y1), r)
#     patches.append(circle)
#
# x = np.random.rand(N)
# y = np.random.rand(N)
# radii = 0.1*np.random.rand(N)
# theta1 = 360.0*np.random.rand(N)
# theta2 = 360.0*np.random.rand(N)
# for x1, y1, r, t1, t2 in zip(x, y, radii, theta1, theta2):
#     wedge = Wedge((x1, y1), r, t1, t2)
#     patches.append(wedge)
#
# # Some limiting conditions on Wedge
# patches += [
#     Wedge((.3, .7), .1, 0, 360),             # Full circle
#     Wedge((.7, .8), .2, 0, 360, width=0.05),  # Full ring
#     Wedge((.8, .3), .2, 0, 45),              # Full sector
#     Wedge((.8, .3), .2, 45, 90, width=0.10),  # Ring sector
# ]
#
# for i in range(N):
#     polygon = Polygon(np.random.rand(N, 2), True)
#     patches.append(polygon)
#
# colors = 100*np.random.rand(len(patches))
# p = PatchCollection(patches, alpha=0.4)
# p.set_array(np.array(colors))
# ax.add_collection(p)
# fig.colorbar(p, ax=ax)
#
# plt.show()


# Get channel occupation data from files
# busy_starting_times = [
#                         [5.0,7.0,10.0],
#                         [7.05],
#                     ]
#
# # Normalize the x-axis to start at 0
# # 'cause UNIX-time isnt really a nice human-readable format
# offset_candidates = [item[0] for item in busy_starting_times]
# offset = min(offset_candidates)
#
# for index,process in enumerate(busy_starting_times):
#     busy_starting_times[index] = [time-offset for time in process]
#
# # prepare lists for data for graphical representation
# busy_end_times = []
# busy_durations = []
#
# for index,process in enumerate(busy_starting_times):
#     # KISS: process = (data,ack)
#     # data channel occupation time is estimated as 0.04s
#     # ack channel occupation time is estimated as 0.01s
#     if index % 2 == 0:
#         process_time = 0.04
#     else:
#         process_time = 0.01
#     process     = [time+process_time for time in process]
#     occupation  = [process_time for time in range(len(process))]
#     busy_end_times.append(process)
#     busy_durations.append(occupation)
#
# # Now let's unify the lists for data and acks of the same process
# # Not really necessary if we do something about the coloring of each n sets
# # if len(busy_starting_times) % 2 == 0:
# #     tmp = []
# #     for index in range(int(len(busy_starting_times)/2)):
# #         tmp += busy_starting_times[2*index]+busy_starting_times[2*index+1]
# #     busy_starting_times = tmp
#
# print("busy_starting_times:")
# print(busy_starting_times)
# print("busy_end_times:")
# print(busy_end_times)
# print("busy_durations:")
# print(busy_durations)

# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
# ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='blue')
# ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
#                facecolors=('red', 'yellow', 'green'))
# ax.broken_barh([(10, 50), (100, 20), (130, 10)], (30, 9),
#               facecolors=('red', 'yellow', 'green'))
# ax.set_ylim(5, 75)
# ax.set_xlim(0, 200)
# ax.set_xlabel('seconds since start')
# ax.set_yticks([15, 25, 35, 45, 55])
# ax.set_yticklabels(['Bill', 'Jim', 'Hank', 'Luke', 'Mojo'])
# ax.grid(True)
# ax.annotate('race interrupted', (61, 25),
#             xytext=(0.8, 0.9), textcoords='axes fraction',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             fontsize=16,
#             horizontalalignment='right', verticalalignment='top')
#
# plt.show()

my_testlist = [[0, 0.00143015, 0.00124589, 0.001134, 0.00104629, 0.000956, 0.000864987, 0.000801704, 0.000719069, 0.0006622, 0.000615381, 0.000548566, 0.000522103, 0.000473815, 0.000418841, 0.000366416, 0.000361022, 0.000333638, 0.00028882, 0.000268787, 0.000250697, 0.00023239, 0.000224631, 0.000194247, 0.000193616, 0.000187931, 0.000144869, 0, 0, 0.000982012, 0.000988646, 0.000992034, 0.000983119, 0.000972897, 0.000991635, 0.000976598, 0.00100275, 0.000998634, 0.000987332, 0.000986414, 0.000993297, 0.00097935, 0.000995065, 0.000978223, 0.000990267, 0.000991301, 0.000981298, 0.00097727, 0.000998009, 0.000992253, 0.000977238, 0.000981395, 0.000982245, 0.000970699, 0.000979029, 0.000993398, 0.000997697, 0.000988178, 0.000988917, 0.000983531, 0.00100323, 0.00098661, 0.000983564, 0.000991967, 0.000983046, 0.000981362, 0.000981658, 0.00097905, 0.000988172, 0, 0, 0.000983878, 0.000985398, 0.000998542, 0.000984792, 0.000986212, 0.000991822, 0.0009863, 0.00100142, 0.000988588, 0.000990725, 0.000985302, 0.000995573, 0.000985165, 0.00100193, 0.000981043, 0.000988179, 0.000993687, 0.000984983, 0.000979004, 0.000987822, 0.000999254, 0.000971319, 0.000989114, 0.000982312, 0.000973891, 0.000984032, 0.000993685, 0.000996267, 0.000993469, 0.000986977, 0.000988791, 0.000992697, 0.000991272, 0.000982097, 0.000987568, 0.000991341, 0.000990064, 0.000979424, 0.000988383, 0.000990261, 0, 0, 0.000972424, 0.00098696, 0.000977707, 0.000963906, 0.000969995, 0.000985557, 0.000977844, 0.000984445, 0.000986531, 0.000974129, 0.000974097, 0.000975413, 0.000984167, 0.000974255, 0.000968273, 0.000985538, 0.000966614, 0.000961674, 0.000981985, 0.000993823, 0.000963338, 0.000978742, 0.000968444, 0.000961415, 0.000966592, 0.000978481, 0.000977005, 0.000990854, 0.00096991, 0.00098594, 0.000979289, 0.000979919, 0.000965217, 0.00097771, 0.000982217, 0.000974936, 0.000966176, 0.00096992, 0.000981017, 0.000981892, 0, 0, 0.000971257, 0.000989491, 0.000984596, 0.000966875, 0.000969535, 0.000978468, 0.00097978, 0.000984119, 0.000976666, 0.000974078, 0.000984686, 0.000977512, 0.000982733, 0.000992846, 0.000974278, 0.000988517, 0.00096924, 0.000961394, 0.000984659, 0.000993828, 0.000974487, 0.000978689, 0.000972639, 0.000968159, 0.000969549, 0.000980523, 0.000979577, 0.000986902, 0.000980476, 0.000982905, 0.0009814, 0.000980491, 0.000972363, 0.000982115, 0.000981447, 0.000978256, 0.000970414, 0.000975761, 0.00097758, 0.000979904, 0.000988405, 0.000984839, 0.000995032, 0.000976213, 0.000982471, 0.000979298, 0.000982011, 0.000997241, 0.000988518, 0.000989809, 0.000980548, 0.000990993, 0.000982754, 0.00100377, 0.000986569, 0.000983158, 0.000990723, 0.000979957, 0.000973809, 0.0009977, 0.000996731, 0.000967988, 0.000979437, 0.000981635, 0.000976355, 0.000978029, 0.000989893, 0.000990622, 0.000991208, 0.000984296, 0.000981537, 0.000990583, 0.000987757, 0.000980964, 0.000986264, 0.000991641, 0.000986939, 0.000971716, 0.000980286, 0.000994935, 0.00098594, 0.000990388, 0.000995824, 0.0009967, 0.00098859, 0.000978756, 0.00099401, 0.000982851, 0.00100018, 0.000992205, 0.000990721, 0.00100041, 0.000991844, 0.000987736, 0.00100066, 0.000976937, 0.000991209, 0.000989892, 0.00097567, 0.000979999, 0.00100379, 0.00098797, 0.000979209, 0.000982459, 0.000983797, 0.000974959, 0.000989998, 0.000986329, 0.000998001, 0.00099151, 0.000979204, 0.000991912, 0.00098651, 0.000982836, 0.000980154, 0.000993305, 0.000983235, 0.000980513, 0.000987398, 0.000980207, 0.000989798, 0, 0, 0.000975331, 0.000981124, 0.000989258, 0.0009802, 0.000975205, 0.000976888, 0.000989652, 0.00097748, 0.000988619, 0.000979408, 0.000982114, 0.00098717, 0.000984912, 0.000980978, 0.000994417, 0.000972903, 0.000988701, 0.000976946, 0.000971684, 0.000981513, 0.00099433, 0.000966631, 0.00097262, 0.000975173, 0.000964038, 0.000970921, 0.000984039, 0.000983662, 0.000988412, 0.000975159, 0.000980243, 0.000985791, 0.000979139, 0.000971166, 0.000975739, 0.000985299, 0.000984877, 0.000970629, 0.000966303, 0.000981089, 0.000977745, 0.000975701, 0.000996646, 0.000989134, 0.0009841, 0.000977133, 0.000982764, 0.000984298, 0.000994427, 0.000982278, 0.000985116, 0.000990722, 0.000987218, 0.000982353, 0.000998264, 0.000974449, 0.000980501, 0.000990078, 0.000977065, 0.000978016, 0.00100334, 0.000985633, 0.000971773, 0.000982433, 0.000978415, 0.000969495, 0.00098848, 0.000981941, 0.000987544, 0.000991297, 0.000985636, 0.000987801, 0.000977764, 0.000980746, 0.000973686, 0.000986419, 0.000985947, 0.000976316, 0.000973594, 0.000972107, 0.00098486, 0, 0, 0.000981483, 0.000998637, 0.000990909, 0.000993143, 0.000977427, 0.000999326, 0.000992779, 0.000997611, 0.000990997, 0.000984153, 0.0010012, 0.000991716, 0.000989431, 0.00100272, 0.000983221, 0.000989986, 0.000992079, 0.000990135, 0.000979756, 0.000996995, 0.000990506, 0.000980036, 0.000988443, 0.000987288, 0.000978855, 0.000994881, 0.000988629, 0.00100172, 0.00099347, 0.000988167, 0.000988152, 0.00098982, 0.00098899, 0.000983084, 0.000993419, 0.000991664, 0.000980071, 0.000990103, 0.000988962, 0.000989759, 0, 0, 0.000969884, 0.000987554, 0.000985625, 0.000973845, 0.000957645, 0.000984476, 0.000976068, 0.000983372, 0.000974374, 0.000970033, 0.00098818, 0.000968835, 0.00096849, 0.000986815, 0.000966437, 0.000972298, 0.000974254, 0.000964995, 0.000965374, 0.000987966, 0.000978345, 0.000964181, 0.000980916, 0.000966726, 0.000959068, 0.000981082, 0.000974217, 0.000986405, 0.000985947, 0.00097302, 0.000974602, 0.000983792, 0.000973175, 0.000967937, 0.000987133, 0.00097843, 0.000965005, 0.000965297, 0.000971917, 0.00097376]]

print(len(my_testlist))
