from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import math
import matplotlib.ticker as ticker

import sys
# path = sys.argv[1]

import sys
path='/mnt/B/sniper/test/gapbs/customLog_8.log'
if path == '':
    path = sys.argv[1]

df = pd.read_csv(path)
df.head()

df['noskip']=1-df['skip']

skip=df.groupby('epoc')['skip'].apply(list)

noskip=df.groupby('epoc')['noskip'].apply(list)

epoc=df['epoc'].unique()

new1=[]
for e in skip.values:
    new1.append(statistics.mean(e) * len(e))

new2=[]
for e in noskip.values:
    new2.append(statistics.mean(e) * len(e))

newd={'epoc':epoc,'skip':new1, 'noskip':new2}
newdf=pd.DataFrame(data=newd)

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))
ax.fmt_ydata = 1.0

plt.plot(newdf['epoc'], newdf['skip'], label="skip")
# plt.plot(newdf['epoc'], newdf['noskip'], label="noskip")

plt.gca().xaxis.set_major_locator(plt.MultipleLocator(50))

#y ticks on interval
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))

# reference line with y ticks
# plot grids only on y axis on major locations
plt.grid(True, which='major', axis='y')

# plt.xticks(newdf['epoc'], labels=newdf['epoc'])
plt.xticks(rotation=90)
plt.title("skip per epoc")
plt.legend()
plt.savefig('skipPerEpoc'+'.png')