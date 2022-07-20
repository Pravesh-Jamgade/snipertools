from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import math
import matplotlib.ticker as ticker

def newlist(newl, fromList):
    for e in fromList.values:
        newl.append(statistics.mean(e) * len(e))

def plotlevel(level):

    plt.plot(newdf['epoc'], newdf[level], label=level)

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(50))

    #y ticks on interval
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))

    # reference line with y ticks
    # plot grids only on y axis on major locations
    plt.grid(True, which='major', axis='y')

    plt.xticks(rotation=90)
    plt.title("noskip per epoc")
    plt.legend()
    plt.savefig('notskipPerEpoc-'+level+'.png')
    plt.clf()

import sys
path='/mnt/B/sniper/test/gapbs/customLog_9.log'
if path == '':
    path = sys.argv[1]

df = pd.read_csv(path)
df.head()

l1d=df.groupby('epoc')['l1d'].apply(list)
l2=df.groupby('epoc')['l2'].apply(list)
l3=df.groupby('epoc')['l3'].apply(list)

epoc=df['epoc'].unique()

new1=[]
newlist(new1,l1d)

new2=[]
newlist(new2,l2)

new3=[]
newlist(new3,l3)

newd={'epoc':epoc,'l1d':new1, 'l2':new2, 'l3':new3}
newdf=pd.DataFrame(data=newd)

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))
ax.fmt_ydata = 1.0

plotlevel('l1d')
plotlevel('l2')
plotlevel('l3')
