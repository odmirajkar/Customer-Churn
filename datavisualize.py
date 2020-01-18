"""
This code is responsible to plotting different graphs for data set
using matplotlib
"""

from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

def pie(slices,labels,explode,shadow,autopct,title):
    """
    Function responsible to draw pie chart
    PArams:
    slices:- list of data values to be plot in pie chart
    labels :- list of lables for each data value
    explode :- list of values in percentage, by which each portion should be cut out from origin
    shadow:-boolean to indicate if shadow is needed or not
    autopact :- sting to fisplay percentage value
    titile:- title of the graph
    """
    plt.pie(slices,labels=labels,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,autopct='%1.1f%%')
    plt.title("Percentage of customer churned")
    plt.tight_layout()
    plt.show()


def hist(list_of_dataset, list_of_label,ylabel,xlabel,title,bins=None,alpha=0.25,axvline=None,axvlie_label=None,axvlinewidth=None):
    """
    Function responsible to plot histograms
    Params:
    list_of_dataset=dataset to plot, if multiple dataset are used then multiple dataset will stacked on top of each other
    bins= bins to use, default is default bins selected by matplotlib
    alpha = to control transpernce, default is 0.25
    list_of_label = label of histogram 
    ylabel = y axis label
    xlabel = x axis label
    title = title of graph
    axvline = vertical line to be drawn in histogram
    axvline_lable= lable of vertical line
    axvlinewidth= width of vertical line 

    """
    for ind,df in enumerate(list_of_dataset):
        plt.hist(df,bins=[0,5,10,12,20,25,30,35,40,45,50,60],alpha=0.5, label=list_of_label[ind])

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.tight_layout()
    plt.title(title)
    if axvline:
        plt.axvline(axvline,label=axvlie_label,color='#91ee9a',linewidth=axvlinewidth)
    plt.show()    
    
