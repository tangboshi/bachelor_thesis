import matplotlib.pyplot as plt
import numpy as np
import os
import math

'''
    Prints single plot with self.data
'''
class myplot:
    def __init__(   self, plottype, data, bins="",
                    title="", xlabel="", ylabel="",
                    show=False, savepath=False, **kwargs
                ):

        print("Hello from myplot_belated.py!")

        self.data               = np.asarray(data).transpose()
        self.bins               = bins
        self.plottype           = plottype
        self.xlabel             = xlabel
        self.ylabel             = ylabel
        # Let's have reasonable figure dimensions
        self.fig, self.ax       = plt.subplots(figsize=(10,8))
        self.kwargs             = kwargs
        self.grid               = kwargs.get("grid", False)
        self.legend             = kwargs.get("legend", [])
        self.xticks             = kwargs.get("xticks", [])
        self.legend_loc         = kwargs.get("legend_loc", "best")
        self.annotations_below  = kwargs.get("annotations_below", [])
        self.annotations_other  = kwargs.get("annotations_other", [])

        #print(self.legend_loc)

        plottypes = {
            "cdf2":     lambda: self.cdf2(),
            "line":     lambda: self.line(),
            "cdf":      lambda: self.cdf(),
            "pdf":      lambda: self.pdf(),
            "boxplot":  lambda: self.boxplot(),
            "debug":    lambda: self.debug()
        }

        titles = {
            "cdf2":     "CDF2",
            "line":     "Line Chart",
            "cdf":      "CDF",
            "pdf":      "PDF",
            "boxplot":  "Boxplot",
            "debug":    "Debug"
        }

        no_sci_label = ["boxplot"]

        # length of plottype is always 1, structure chosen for possible
        # future developments!
        for aplot in plottype:
            #print("single plot in plottype array is:"+str(aplot))
            self.title = title+" "+titles[aplot]
            if aplot not in no_sci_label:
                plt.ticklabel_format(style='sci', scilimits=(0,0))
            # Make plot
            plottypes[aplot]()
            # Optionally create grid
            self.ax.xaxis.grid(self.grid)
            self.ax.yaxis.grid(self.grid)
            #Create legend
            #This will create a warning if you plot boxplots that you can
            #safely ignore (boxplots cannot be labeled).
            #As a workaround the xticks are labeled
            if len(self.data) == len(self.legend):
                self.ax.legend(fancybox=True,loc=self.legend_loc)
            else:
                print ( "len(self.data) = "
                        + str(len(self.data))
                        + " and len(self.legend) = "
                        + str(len(self.legend))
                        +" don't match!")
            # Add anotations:
            for annotation in self.annotations_other:
                self.ax.annotate(annotate)
            # Save and show plot
            if(savepath):
                print(savepath)
                self.save(savepath, aplot)
            if(show):
                self.show()

            self.fig.clear()

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
                        label=self.legend)
        self.setLabels( xlabel=self.xlabel,
                        ylabel="cumulative density",
                        title=self.title)
        print(self.patches)

    def cdf2(self):
        self.n, self.bins, self.patches = self.ax.hist(x=self.data,
                        bins=self.bins,
                        normed=1,
                        histtype='bar',
                        stacked=True,
                        cumulative=True,
                        label=self.legend)
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
                        label=self.legend)
        self.setLabels( xlabel=self.xlabel,
                        ylabel="probability density",
                        title=self.title)

        cm = plt.cm.get_cmap('jet')
        for index, patch in enumerate(self.patches):
            plt.setp(patch, 'facecolor', cm(float(index/len(self.patches))))

    def boxplot(self):
        self.plot = plt.boxplot(self.data,
                                #notch=True,
                                patch_artist=True)

        colors = ['ivory','honeydew','mistyrose','lightskyblue','plum']
        color_repetitions = math.ceil(len(self.data)/len(colors))
        colors = color_repetitions * colors

        for patch, color in zip(self.plot['boxes'], colors):
            patch.set_facecolor(color)

        self.setLabels( xlabel="measurement",
                        ylabel=self.ylabel,
                        title=self.title)

        # Only modify xticks if self.data has as many data sets as self.xticks
        # has labels. Else print warning.
        if len(self.data) == len(self.xticks):
            plt.xticks([x+1 for x in range(len(self.xticks))],self.xticks)
        else:
            print ( "len(self.data) = "
                    + str(len(self.data))
                    + " and len(self.xticks) = "
                    + str(len(self.xticks))
                    +" don't match!")

        #Diagnostic
        #print(self.plot)
        #print("Whiskers: "+self.plot["whiskers"])

    def setLabels(self, xlabel="", ylabel="", title=""):
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)

    def save(self, savepath, plot_type):
        savename = self.title
        savename = savename.lower()
        savename = savename.replace(" ", "_")
        self.fig.savefig(savepath+plot_type+"/"+savename+".png")
        self.fig.savefig(savepath+plot_type+"/"+savename+".pdf")

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
