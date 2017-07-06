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

import myplot
fancyplot = myplot.myplot(data=data, bins=repetitions, plottype="cdf")
fancyplot.setLabels(xlabel="awesomeness", ylabel="fancyness", title="Fancyplot")
fancyplot.show()

mystring ="abc"
result = mystring.split(",")
print(result)
