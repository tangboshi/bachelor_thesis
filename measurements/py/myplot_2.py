import matplotlib.pyplot as plt
import numpy as np
import os

class myplot:
    def __init__(   self, plottype, data, bins="",
                    title="", xlabel="", ylabel="",
                    show=False, savepath=False, **kwargs
                ):

        print("Hello from myplot.py!")

        self.data           = np.asarray(data).transpose()
        self.bins           = bins
        self.plottype       = plottype
        self.xlabel         = xlabel
        self.ylabel         = ylabel
        self.fig, self.ax   = plt.subplots()
        self.kwargs         = kwargs

        plottypes = {
            "bar":      lambda: self.bar(),
            "line":     lambda: self.line(),
            "cdf":      lambda: self.cdf(),
            "pdf":      lambda: self.pdf(),
            "boxplot":  lambda: self.boxplot(),
            "debug":    lambda: self.debug()
        }

        titles = {
            "bar":      "Bar Chart",
            "line":     "Line Chart",
            "cdf":      "CDF",
            "pdf":      "PDF",
            "boxplot":  "Boxplot",
            "debug":    "Debug"
        }

        self.title  = []
        no_sci_label = ["boxplot"]
        for aplot in plottype:
            #for var in aplot:
            print("single plot in plottype array is:"+str(aplot))
            self.title += [ title+" "+titles[aplot] ]
            if aplot not in no_sci_label:
                plt.ticklabel_format(style='sci', scilimits=(0,0))

        # After variable assignments
        # print("I will print a the following plots for you now!")
        # for aplot in self.plottype:
        #     print(aplot)
        # Before calling plotting function

        for aplot in plottype:
            plottypes[aplot]()



        if(savepath):
            self.save(savepath)

        if(show):
            self.show()

    def bar(self):
        # first rhv is an experimental value, choose what pleases your eye
        data_points=len(self.data)
        width=20/data_points
        index=np.arange( data_points )

        self.ax.bar(left=index + width,
            height=self.data,
            color="#80e5ff"
         )

        self.setLabels(ylabel=self.ylabel,
            xlabel="measurement",
            title=self.title
        )

        plt.gca().axes.get_xaxis().set_visible(False)

        if not self.kwargs.get("number_bars", True) == False:
            rects = self.ax.patches
            labels = ["%d" % i for i in range(1,len(rects)+1)]

            for rect, label in zip(rects, labels):
                #height = rect.get_height()
                self.ax.text(
                    rect.get_x() + rect.get_width()/2,
                    0,
                    label,
                    ha='center',
                    va='bottom')

    def line(self):
        #FIXME
        from scipy.interpolate import interp1d
        x = np.arange(1, len(self.data)+1, 1)
        y = self.data
        f = interp1d(x,y)
        plt.plot(x, self.data, 'bo', x, f(x), 'k')

        self.setLabels( xlabel="measurement",
                        ylabel=self.ylabel,
                        title=self.title
        )

    def cdf(self):
        # if not self.bins:
        #     print("Error: bins undefined.")
        #     return
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
        # if not self.bins:
        #     print("Error: bins undefined.")
        #     return
        self.n, self.bins, self.patches = self.ax.hist(x=self.data,
                        bins=self.bins,
                        align='left',
                        fill='true',
                        normed=1,
                        cumulative=False,
                        label='PDF')
        self.setLabels( xlabel=self.xlabel,
                        ylabel="probability density",
                        title=self.title)

        cm = plt.cm.get_cmap('jet')
        for index, patch in enumerate(self.patches):
            plt.setp(patch, 'facecolor', cm(float(index/len(self.patches))))

    def boxplot(self):
        self.plot = plt.boxplot(self.data)
        self.setLabels( xlabel="measurement",
                        ylabel=self.ylabel,
                        title=self.title)
        #print("Whiskers: "+self.plot["whiskers"])

    def setLabels(self, xlabel="", ylabel="", title=""):
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)

    def save(self, savepath):
        savenames = self.title#+"_"+self.plottype
        savenames = [savename.lower() for savename in savenames]
        savenames = [savename.replace(" ", "_") for savename in savenames]
        for savename in savenames:
            self.fig.savefig(savepath+savename+".png")
            self.fig.savefig(savepath+savename+".pdf")

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
