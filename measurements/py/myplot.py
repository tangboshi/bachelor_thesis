import matplotlib.patches as mpatches
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
                    show=False, savepath=False, data_x=None, **kwargs
                ):

        print("Hello from myplot_belated.py!")

        self.data               = np.asarray(data).transpose()
        self.data_x             = data_x

        print("Title is '"+title+"'.")
        # FIXME: Very hackish, but who cares!
        if  (title == "Retransmissions per Frame"
            or len(data) == 1
            or "bar"  in plottype
            or "hist" in plottype
            or "broken_barh" in plottype):
            print("Keeping original data format instead of transposing.")
            self.data               = data

        self.bins               = bins
        self.plottype           = plottype
        self.xlabel             = xlabel
        self.ylabel             = ylabel
        # Let's have reasonable figure dimensions
        self.fig, self.ax       = plt.subplots(figsize=(9,5))
        self.kwargs             = kwargs
        self.grid               = kwargs.get("grid", False)
        self.legend             = kwargs.get("legend", [])
        self.xticks             = kwargs.get("xticks", [])
        self.legend_loc         = kwargs.get("legend_loc", "best")
        self.annotations_below  = kwargs.get("annotations_below", [])
        self.annotations_other  = kwargs.get("annotations_other", [])
        self.legend_coordinates = kwargs.get("legend_coordinates", False)
        self.timer              = kwargs.get("timer", 300)
        self.repetitions        = kwargs.get("repetitions", 5)
        self.eval_mode          = kwargs.get("eval_mode", "belated")
        self.xlims              = kwargs.get("xlims", False)
        self.ylims              = kwargs.get("ylims", False)
        self.savepath           = savepath,
        self.plot_pdf           = kwargs.get("plot_pdf", False)

        legend_outside_plot     = True
        #print(self.legend_loc)

        plottypes = {
            "hist":         lambda: self.hist(),
            "line":         lambda: self.line(),
            "cdf":          lambda: self.cdf(),
            "pdf":          lambda: self.pdf(),
            "boxplot":      lambda: self.boxplot(),
            "debug":        lambda: self.debug(),
            "bar":          lambda: self.bar(),
            "broken_barh":  lambda: self.broken_barh(),
            "line_xy":      lambda: self.line_xy()
        }

        titles = {
            "cdf":          "CDF",
            "line":         "Line Chart",
            "line_xy":      "Line Chart",
            "hist":         "Histogram",
            "pdf":          "PDF",
            "boxplot":      "Boxplot",
            "debug":        "Debug",
            "bar":          "Bar Chart",
            "broken_barh":  "Gantt Chart"
        }

        # scientific axis scaling exceptions
        #no_sci_label = ["boxplot"]

        # length of plottype is always 1, structure chosen for possible
        # future developments!
        for aplot in plottype:
            #print("single plot in plottype array is:"+str(aplot))
            self.title = title+" "+titles[aplot]
            self.savename = self.title
            self.title = ""
            # scientific axis scaling, deactivated because not liked by supervisors
            # if aplot not in no_sci_label:
            #     plt.ticklabel_format(style='sci', scilimits=(0,0))
            # Make plot
            plottypes[aplot]()
            #set axis limits
            self.ax.set_ylim(ymin=0)
            print("self.ylims is:"+str(self.ylims))
            if self.ylims:
                self.ax.set_ylim(ymin=self.ylims[0], ymax=self.ylims[1])
            if self.xlims != False and not (aplot in ["boxplot", "bar"]):
                self.ax.set_xlim(self.xlims[0], self.xlims[1])
            else:
                self.ax.set_xlim(xmin=0)
            #get rid of unloved margins
            plt.tight_layout()
            # Optionally create grid
            self.ax.xaxis.grid(self.grid, linestyle="dashdot")
            self.ax.yaxis.grid(self.grid, linestyle="dashdot")
            #Create legend
            #This will create a warning if you plot boxplots that you can
            #safely ignore (boxplots cannot be labeled).
            #As a workaround the xticks are labeled
            if not aplot == "boxplot" and not aplot == "broken_barh":
                if len(np.asarray(self.data).transpose()) == len(self.legend):
                    if self.legend_coordinates == False or legend_outside_plot:
                        box = self.ax.get_position()
                        self.ax.set_position([
                            box.x0,
                            box.y0+box.height*0.4,
                            box.width,
                            box.height*0.6
                        ])
                        self.ax.legend(fancybox=True,
                                    loc='upper center',
                                    bbox_to_anchor=(0.5, -0.35))
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

            font = {'family' : 'normal',
                    #'size'   : 12,
                    'weight' : 400
                }

            plt.rc('font', **font)

            # Add anotations:
            self.annotate()
            for annotation in self.annotations_other:
                self.ax.annotate(annotation)
            # Save and show plot
            if(savepath):
                print("***savepath***")
                print(savepath)
                self.save(savepath, aplot)
            if(show):
                self.show()

            #plt.close(self.fig)
            self.fig.clear()
            #print(self.data)

    def bar(self):

        colors = ['steelblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink']
        color_repetitions = math.ceil(len(self.data)/len(colors))
        colors = color_repetitions * colors

        print(self.data)
        for idx,val in enumerate(self.data):
            data_points=len(self.data[idx])
            width=5/data_points
            index=np.arange( data_points )

            self.ax.bar(left=idx*width+width/2,
                height=val,
                color=colors[idx],
                alpha=0.5
             )

            self.setLabels(ylabel=self.ylabel,
                xlabel="measurement",
                title=self.title
            )

        # plt.gca().axes.get_xaxis().set_visible(False)
        #
        # if not self.kwargs.get("number_bars", True) == False:
        #     rects = self.ax.patches
        #     labels = ["%d" % i for i in range(1,len(rects)+1)]
        #
        #     for rect, label in zip(rects, labels):
        #         #height = rect.get_height()
        #         self.ax.text(
        #             rect.get_x() + rect.get_width()/2,
        #             0,
        #             label,
        #             ha='center',
        #             va='bottom')

    def broken_barh(self):
        plot_data = []
        debug_data = []
        for index,item in enumerate(self.data["occupation_starting"]):
            plot_data.append(list(zip(self.data["occupation_starting"][index], self.data["occupation_durations"][index])))

        for index,item in enumerate(self.data["acks_received"]):
            debug_data.append(list(zip(self.data["acks_received"][index], self.data["acks_received_bar_width"][index])))

        print("plot_data:")
        #print(plot_data)
        print("debug_data:")
        #print(debug_data)
        print("data_len:")
        data_len = len(plot_data)
        print(data_len)
        debug_len = len(debug_data)
        print("debug_len:")
        print(debug_len)

        print("data and ack lengths:")
        for index,item in enumerate(plot_data):
            if index % 2 == 0:
                print("data index "+str(index)+":")
            else:
                print("ack index "+str(index)+":")
            print(len(item))

        for index, item in enumerate(debug_data):
            print ("debug data index "+str(index)+":")
            print(len(item))
            #print(item)

        self.ax.set_ylim(10, 5*data_len+20)
        if self.xlims == False:
            self.ax.set_xlim(0, self.timer*self.repetitions)
        self.ax.xaxis.grid(self.grid, linestyle="dashdot")
        self.ax.yaxis.grid(self.grid, linestyle="dashdot")

        # FIXME: Now ACKS are absolutely required, or data_len/2 doesn't make sense!
        self.ax.set_yticks([x*10+15 for x in range(int(data_len/2))])
        self.xticks = [tick.replace(",", ",\n") for tick in self.xticks]
        self.ax.set_yticklabels([self.xticks[index] for index in range(int(data_len/2))])

        self.setLabels(
            xlabel="time[s]",
            title=self.title
        )

        colors = ['blue','red','black']
        transparency=0.7

        patch_a  = mpatches.Patch(color=colors[0], alpha=transparency, label="data sent")
        patch_b  = mpatches.Patch(color=colors[1], alpha=transparency, label='ack sent')
        patch_c  = mpatches.Patch(color=colors[2], alpha=transparency, label="ack received")

        if self.legend_coordinates[2] != "best":
            self.ax.legend( handles=[patch_a,patch_b],#patch_c],
                            fancybox=True,
                            loc=self.legend_coordinates[2],
                            bbox_to_anchor=(self.legend_coordinates[0],
                                            self.legend_coordinates[1]))
        else:
            self.ax.legend( handles=[patch_a,patch_b],#patch_c],
                            fancybox=True,
                            loc="best")

        for index,item in enumerate(plot_data):
            print("Added (data) set with index "+str(index)+" to plot.")
            if index % 2 == 0:
                self.ax.broken_barh(item,((index+1)*5+5,13), facecolors=colors[0], alpha=0.5)
            elif (index-1) % 2 == 0: # well else should be enough here :)
                self.ax.broken_barh(item,((index)*5+5,13), facecolors=colors[1], alpha=0.5)

        # for index,item in enumerate(debug_data):
        #     print("Added (debug) set with index "+str(index)+" to plot.")
        #     if index % 2 == 0:
        #         self.ax.broken_barh(item,((index+1)*5+5,13), facecolors=colors[2], alpha=0.5)
        #     elif (index-1) % 2 == 0:
        #         self.ax.broken_barh(item,((index)*5+5,13), facecolors=colors[2], alpha=0.5)

        plt.tight_layout()

        # if(self.savepath):
        #     print("***savepath***")
        #     print(self.savepath)
        #     self.save(self.savepath, "gantt")

    def line(self):
        from scipy.interpolate import interp1d
        x = np.arange(1, len(self.data)+1, 1)
        y = self.data
        f = interp1d(x,y)
        #plt.plot(x, self.data, 'bo')
        plt.plot(x, f(x), 'k')

        self.setLabels( xlabel="measurement",
                        ylabel=self.ylabel,
                        title=self.title
        )

    def line_xy(self):
        from scipy.interpolate import interp1d
        x = self.data_x
        y = self.data
        f = interp1d(x,y)

        #plt.plot(x, self.data, 'bo')
        plt.plot(x, f(x), 'k')

        self.setLabels( xlabel=self.xlabel,
                        ylabel=self.ylabel,
                        title=self.title
        )

    def hist(self):
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
        linestyles = ["-", "-", ":", ":","-", "--", "-.", ":","-", "--"]
        linewidths = [6,3,6,3,1.2,1.05,1,0.9,0.8,0.75]
        colors = ["blue","orange","blue","orange","blue","orange","blue","orange","blue"]

        if self.eval_mode == "belated":
            cdf_data = np.asarray(self.data).transpose()
        if self.eval_mode == "live":
            cdf_data = np.asarray(self.data).transpose()
            if self.title == "Retransmissions per Frame":
                cdf_data = [cdf_data]
        if len(self.data) == 1:
            print("Hooray, my title is "+self.title+".")
            cdf_data = self.data

        if len(cdf_data) > 1:
            for index,item in enumerate(cdf_data):
                print("index:"+str(index))
                print("___markers____")
                print(markers[index])
                x = np.sort(item)
                y = np.arange(1,len(x)+1) / len(x)
                x = np.insert(x,0,x[0])
                y = np.insert(y,0,0)
                self.plot = plt.step(x,
                    y,
                    marker=markers[index],
                    linestyle=linestyles[index],
                    linewidth=linewidths[index],
                    markevery=range(1,len(x)),
                    label=self.legend[index],
                    color=colors[index])
        else:
            x = np.sort(cdf_data[0])
            y = np.arange(1,len(x)+1) / len(x)
            x = np.insert(x,0,x[0])
            y = np.insert(y,0,0)
            print(x)
            print(y)
            self.plot = plt.step(x,
                    y,
                    marker=markers[0],
                    linestyle=linestyles[0],
                    linewidth=linewidths[0],
                    markevery=range(1,len(x)),
                    label=self.legend[0],
                    color=colors[0])


        self.setLabels( xlabel=self.xlabel,
                        ylabel="cumulative density",
                        title=self.title)
        self.ax.set_ylim(ymax=1)

    def pdf(self):
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
        print(self.data)

        self.plot = plt.boxplot(self.data,
                                #notch=True,
                                patch_artist=True,
                                flierprops=dict(marker='x'))

        colors = ['steelblue', 'peachpuff', 'green', 'red', 'purple', 'brown', 'pink']
        color_repetitions = math.ceil(len(self.data)/len(colors))
        colors = color_repetitions * colors

        for patch, color in zip(self.plot['boxes'], colors):
            patch.set_facecolor(color)

        self.setLabels( xlabel="measurement",
                        ylabel=self.ylabel,
                        title=self.title)

        boxdict = self.ax.boxplot(self.data)
        fliers  = boxdict["fliers"]

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
        #savename = self.title
        savename = self.savename
        savename = savename.lower()
        savename = savename.replace(" ", "_")
        self.fig.savefig(savepath+savename+".png")
        if self.plot_pdf:
            self.fig.savefig(savepath+savename+".pdf")

    def show(self):
        plt.show()

    def annotate(self):
        print("xlim:"+str(self.ax.get_xlim()))
        print("ylim:"+str(self.ax.get_ylim()))
        circle_rad = 18
        # dual ALOHA
        points = [(8.02,0.00062),(8.27,0.00062),(8.52,0.00062),(8.77,0.00062),(9.00,0.00062),(9.24,0.00062),(9.49,0.00062),(9.73,0.00062),(9.97,0.00062)]
        #points = [(8.17,21.7),(8.33,21.7),(8.71,21.7),(8.87,21.7),(9.19,21.7),(9.41,21.7),(9.575,21.7)]
        # dual 1-pers CSMA
        #points = [(8.17,0.00065),(8.33,0.00065),(8.71,0.00066),(8.87,0.00064),(9.19,0.00066),(9.41,0.00066),(9.575,0.00066)]
        #points = [(8.17,21.7),(8.33,21.7),(8.71,21.7),(8.87,21.7),(9.19,21.7),(9.41,21.7),(9.575,21.7)]
        # dual low parameter CSMA/CA
        #points = [(10.46,0.00067),(10.68,0.00041),(11.77,0.00073)]
        #points = [(10.44,21.7),(10.65,21.7),(11.75,21.7)]
        # unsaturated ALOHA + CSMA/CA
        #points = [(8.335,0.00068),(8.365,0.00041),(8.634,0.00041),(8.68,0.00041),(9.69,0.00074)]
        # points = [(8.335,21.7),(8.365,21.7),(8.634,21.7),(8.68,21.7),(9.69,21.7)]
        # unsaturated ALOHA + 1-persistent CSMA
        #points = [(8.86,0.00039),(9.1,0.00039),(9.36,0.00063),(9.57,0.00041),(9.61,0.00059)]
        #points = [(8.86,21.7),(9.1,21.7),(9.36,21.7),(9.57,21.7),(9.61,21.7)]
        for item in points:
            pass
            #print ("Hooray, I'm executed!")
            #self.ax.plot(item[0], item[1], 'o',
                    #ms=circle_rad * 2, mec='r', mfc='none', mew=2)

        # logical channel occupation: xy=(8.85,5)
        # channel energy: xy=(10.85,0.00105)
        #self.ax.annotate('collisions', xy=(8.78,0.00086), color='r',size=18)

        # arrow annotation
        # self.ax.annotate('collision', xy=point, xytext=(60, 60),
        #             textcoords='offset points',
        #             color='r', size='large',
        #             arrowprops=dict(
        #                 arrowstyle='simple,tail_width=0.3,head_width=0.8,head_length=0.8',
        #                 facecolor='r', shrinkB=circle_rad * 1.2)
        #)

    def debug(self):
        print("data: "+str(self.data))
        print("bins: "+str(self.bins))
        print("plottype: "+self.plottype)
