import matplotlib.pyplot as plt
import numpy as np
import os
import math

import pdb

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

        print("Title is '"+title+"'.")
        # Kind of hackish, but who cares!
        if title == "Retransmissions per Frame":
            self.data           = data

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
        self.legend_coordinates = kwargs.get("legend_coordinates", False)

        #print(self.legend_loc)

        plottypes = {
            "hist":     lambda: self.hist(),
            "line":     lambda: self.line(),
            "cdf":      lambda: self.cdf(),
            "pdf":      lambda: self.pdf(),
            "boxplot":  lambda: self.boxplot(),
            "debug":    lambda: self.debug()
        }

        titles = {
            "cdf":      "CDF",
            "line":     "Line Chart",
            "hist":     "Histogram",
            "pdf":      "PDF",
            "boxplot":  "Boxplot",
            "debug":    "Debug"
        }

        # scientific axis scaling exceptions
        #no_sci_label = ["boxplot"]

        # length of plottype is always 1, structure chosen for possible
        # future developments!
        for aplot in plottype:
            #print("single plot in plottype array is:"+str(aplot))
            self.title = title+" "+titles[aplot]
            # scientific axis scaling, deactivated because not liked by supervisors
            # if aplot not in no_sci_label:
            #     plt.ticklabel_format(style='sci', scilimits=(0,0))
            # Make plot
            plottypes[aplot]()
            #set axis limits
            self.ax.set_ylim(ymin=0)
            #get rid of unloved margins
            plt.tight_layout()
            # Optionally create grid
            self.ax.xaxis.grid(self.grid)
            self.ax.yaxis.grid(self.grid)
            #Create legend
            #This will create a warning if you plot boxplots that you can
            #safely ignore (boxplots cannot be labeled).
            #As a workaround the xticks are labeled
            if not aplot == "boxplot":
                if len(np.asarray(self.data).transpose()) == len(self.legend):
                    if self.legend_coordinates == False:
                        box = self.ax.get_position()
                        self.ax.set_position([
                            box.x0,
                            box.y0+box.height*0.3,
                            box.width,
                            box.height*0.7
                        ])
                        self.ax.legend(fancybox=True,
                                    loc='upper center',
                                    bbox_to_anchor=(0.5, -0.15))
                    else:
                        if self.legend_coordinates[2] != "best":
                            self.ax.legend(fancybox=True,
                                        loc=self.legend_coordinates[2],
                                        bbox_to_anchor=(self.legend_coordinates[0],
                                                        self.legend_coordinates[1]))
                        else:
                            self.ax.legend(fancybox=True,loc="best")
                else:
                    print ( "len(self.data) = "
                            + str(len(np.asarray(self.data).transpose()))
                            + " and len(self.legend) = "
                            + str(len(self.legend))
                            +" don't match!")
            # Add anotations:
            for annotation in self.annotations_other:
                self.ax.annotate(annotation)
            # Save and show plot
            if(savepath):
                print("***savepath***")
                print(savepath)
                self.save(savepath, aplot)
            if(show):
                self.show()

            self.fig.clear()
            #print(self.data)

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

    def hist(self):
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

    def cdf(self):
        print("**cdf_data**")
        #print(self.data)
        print(self.legend)
        markers = ["x","v","o","^","8","s","p","+","D","*"]
        #markers = markers[:len(self.data)]
        for index,item in enumerate(np.asarray(self.data).transpose()):
            #print(index)
            print("index:"+str(index))
            print("___markers____")
            print(markers[index])
            item += [0]
            print("***item***")
            print(item)
            x = np.sort(item)
            y = np.arange(1,len(x)+1) / len(x)
            self.plot = plt.plot(x,
                    y,
                    marker=markers[index],
                    label=self.legend[index])
        self.setLabels( xlabel=self.xlabel,
                        ylabel="cumulative density",
                        title=self.title)
        self.ax.set_ylim(ymax=1)

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
        #print("boxplot() reached.")
        print(self.data)

        self.plot = plt.boxplot(self.data,
                                #notch=True,
                                patch_artist=True,
                                flierprops=dict(marker='x'))

        colors = ['steelblue', 'peachpuff', 'green', 'red', 'purple', 'brown', 'pink']
        #colors = ['ivory','honeydew','mistyrose','lightskyblue','plum','#00eacb']
        color_repetitions = math.ceil(len(self.data)/len(colors))
        colors = color_repetitions * colors

        for patch, color in zip(self.plot['boxes'], colors):
            patch.set_facecolor(color)

        self.setLabels( xlabel="measurement",
                        ylabel=self.ylabel,
                        title=self.title)

        #Let's call the number of fliers :)

        boxdict = self.ax.boxplot(self.data)
        fliers  = boxdict["fliers"]

        #print("***self.data***:%")
        #print(self.data)

        for j in range(len(fliers)):
            # the y and x positions of the fliers
            yfliers = boxdict['fliers'][j].get_ydata()
            xfliers = boxdict['fliers'][j].get_xdata()
            # the unique locations of fliers in y
            ufliers = set(yfliers)
            # loop over unique fliers
            for i, uf in enumerate(ufliers):
                # print number of fliers
                self.ax.text(xfliers[i] + 0.05, uf, list(yfliers).count(uf))

        # Only modify xticks if self.data has as many data sets as self.xticks
        # has labels. Else print warning.
        if len(np.asarray(self.data).transpose()) == len(self.xticks):
            #print("Yippie, the condition is true!")
            print(self.xticks)
            plt.xticks([x+1 for x in range(len(self.xticks))],self.xticks)
            #self.ax.set_xticklabels(self.xticks);
        else:
            print ( "len(self.data) = "
                    + str(len(self.data))
                    + " and len(self.xticks) = "
                    + str(len(self.xticks))
                    +" don't match!")

    def setLabels(self, xlabel="", ylabel="", title=""):
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)

    def save(self, savepath, plot_type):
        #pdb.set_trace()
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
