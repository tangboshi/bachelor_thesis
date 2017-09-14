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

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('red', 'yellow', 'green'))
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (30, 9),
              facecolors=('red', 'yellow', 'green'))
ax.set_ylim(5, 75)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25, 35, 45, 55])
ax.set_yticklabels(['Bill', 'Jim', 'Hank', 'Luke', 'Mojo'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
