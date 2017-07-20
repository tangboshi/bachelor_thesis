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

data = [1,2,4,5,6,2,4,7,8,1,2,9,17,
        2,3,5,6,8,2,6,12,19,16,13,8,
        14,25,1,2,7,5,10,13,17,7,2]
repetitions = len(data)

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

import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt

sample = np.random.uniform(0, 1, 50)
ecdf = sm.distributions.ECDF(sample)

x = np.linspace(min(sample), max(sample))
y = ecdf(x)
plt.step(x, y)
plt.show()
