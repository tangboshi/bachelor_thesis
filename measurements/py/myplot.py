import matplotlib.pyplot as plt
import numpy as np
import os

class myplot:
    def __init__(   self, plottype, data, bins, title="", xlabel="", ylabel="",
                    show=False, savepath=False
                ):

        print("Hello from myplot.py!")
        print("I will print a "+plottype+" for you now!")
        self.data           = data
        self.bins           = bins
        self.plottype       = plottype
        self.title          = title
        self.xlabel         = xlabel
        self.ylabel         = ylabel
        self.fig, self.ax   = plt.subplots()

        plottypes = {
            "cdf":      lambda: self.cdf(),
            "pdf":      lambda: self.pdf(),
            "boxplot":  lambda: self.boxplot(),
            "debug":    lambda: self.debug()
        }

        plottypes[plottype]()

        self.patches.fill = True;

        if(savepath):
            self.save(savepath)

        if(show):
            self.show()

    def cdf(self):
        self.n, self.bins, self.patches = self.ax.hist(x=self.data,
                        bins=self.bins,
                        normed=1,
                        histtype='step',
                        cumulative=True,
                        label='CDF')
        self.setLabels( xlabel=self.xlabel,
                        ylabel="cumulative density",
                        title=self.title)
        print(self.patches)

    def pdf(self):
        self.n, self.bins, self.patches = self.ax.hist(x=self.data,
                        bins=self.bins,
                        align='left',
                        fill='true',
                        normed=1,
                        cumulative=False,
                        label='CDF')
        self.setLabels( xlabel=self.xlabel,
                        ylabel="probability density",
                        title=self.title)

        cm = plt.cm.get_cmap('jet')
        for index, patch in enumerate(self.patches):
            plt.setp(patch, 'facecolor', cm(float(index/len(self.patches))))

    def boxplot(self):
        print("Boxplot not implemented yet!")

    def setLabels(self, xlabel="", ylabel="", title=""):
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)

    def save(self, savepath):
        self.fig.savefig(savepath+self.title+"_"+self.plottype+".png")
        self.fig.savefig(savepath+self.title+"_"+self.plottype+".pdf")

    def show(self):
        plt.show()

    ''' uncomment if these functions should become a necessity.
    def getFig(self):
        return self.fig

    def getAx(self):
        return self.ax
    '''

    def debug(self):
        print("data: "+str(self.data))
        print("bins: "+str(self.bins))
        print("plottype: "+self.plottype)
