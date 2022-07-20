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

def helper(level):
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1000))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))
    plt.grid(True, which='major', axis='y')
    plt.xticks(rotation=90)
    plt.title("skip per epoc")
    plt.xlabel('epoc')
    plt.ylabel('mean of skip count per epoc')
    plt.legend()
    plt.savefig(alias+'PerEpoc-'+level+'.png')

def plotlevel(level,c):
    plt.plot(newdf['epoc'], newdf[level], label=level, color=c)
    helper(level)
    plt.clf()

import sys
path=''#'/mnt/B/sniper/test/gapbs/customLog_9.log'
alias=''#'noskip'
if path == '':
    path = sys.argv[1]
    alias = sys.argv[2]
else:
    print("test is on")

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

plotlevel('l1d','r')
plotlevel('l2', 'g')
plotlevel('l3', 'b')

plt.plot(newdf['epoc'], newdf['l1d'], 'r', label='l1d')
plt.plot(newdf['epoc'], newdf['l2'], 'g', label='l2')
plt.plot(newdf['epoc'], newdf['l3'], 'b', label='l3')
helper('')
