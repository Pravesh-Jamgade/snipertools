from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics


import sys
path='/mnt/B/sniper/test/gapbs/customLog_11.log'
if path == '':
    path = sys.argv[1]
df = pd.read_csv(path)
df.head()

#remove unnamed last col because of extra , at end 
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df=df[df.columns.drop('pc')]
print(df)

#groupby epoc into list
t=df.pivot_table(columns=['epoc'],aggfunc='size').to_list()
l1d=df.groupby('epoc')['l1d'].apply(list)
l2=df.groupby('epoc')['l2'].apply(list)
l3=df.groupby('epoc')['l3'].apply(list)
epoc=df['epoc'].unique()
newd={'epoc':epoc,'l1d':l1d.values, 'l2':l2.values, 'l3':l3.values}
newdf=pd.DataFrame(data=newd)
print(newdf)

#for each list of epoc, find mean or gmean
newl1=[]
newl2=[]
newl3=[]
for e in l1d.values:
	newl1.append(statistics.mean(e))
for e in l2.values:
	newl2.append(statistics.mean(e))
for e in l3.values:
	newl3.append(statistics.mean(e))

tmpd={'epoc':epoc, 'l1d':newl1, 'l2':newl2, 'l3':newl3}
tmpdf=pd.DataFrame(data=tmpd)
print(tmpdf)

plt.plot(tmpdf['l1d'], label='l1d', color='blue')  # Plot some data on the (implicit) axes.
plt.plot(tmpdf['l2'], label='l2', color='red')  # etc.
plt.plot(tmpdf['l3'], label='l3', color='green')
plt.xlabel('epoc')
plt.ylabel('missmatch/missmatch + match')
plt.title("LP Missmatch")
plt.legend()
plt.savefig('timeseries'+'.png')