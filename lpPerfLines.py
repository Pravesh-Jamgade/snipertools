from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))

def helper(label):
	#y ticks on interval
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))#3
	plt.gca().xaxis.set_major_locator(plt.MultipleLocator(2000))#800
	plt.grid(True, which='major', axis='y')
	plt.xlabel('epoc')
	plt.ylabel('LP Perf')
	plt.ylim(ymax=1.0,ymin=0.0)
	plt.xticks(rotation=90)
	plt.title("using epoc x-1 decision to compare how they are useful in x")
	# ax.legend(loc='upper center', shadow=True, fontsize='x-large')
	plt.legend()
	plt.savefig('lpPerf-dots-'+label+alias+'.png')

def personalLine(label, mark, tag):
    ax.fmt_ydata = 1.0
    plt.plot(tmpdf['epoc'], tmpdf[label], mark, label=tag)
    helper(label)
    plt.clf()

import sys
path=''#'/mnt/B/sniper/test/gapbs/customLog_15.log'
alias=''
if path == '':
    path = sys.argv[1]
    alias=sys.argv[2]
else:
	print("test is on")
df = pd.read_csv(path)
df.head()

#groupby epoc into list
fs=df.groupby('epoc')['fs'].apply(list)
ts=df.groupby('epoc')['ts'].apply(list)
fns=df.groupby('epoc')['fns'].apply(list)
tns=df.groupby('epoc')['tns'].apply(list)
epoc=df['epoc'].unique()

#for each list of epoc, find mean or gmean
newl1=[]
newl2=[]
newl3=[]
newl4=[]
for e in fs.values:
	newl1.append(statistics.mean(e))
for e in ts.values:
	newl2.append(statistics.mean(e))
for e in fns.values:
	newl3.append(statistics.mean(e))
for e in tns.values:
	newl4.append(statistics.mean(e))

tmpd={'epoc':epoc, 'fs':newl1, 'ts':newl2, 'fns':newl3, 'tns':newl4}
tmpdf=pd.DataFrame(data=tmpd)

personalLine('fs', 'b', 'false skip')
personalLine('ts', 'r', 'true skip')
personalLine('fns', 'g', 'false no-skip')
personalLine('tns', 'm', 'true no-skip')

plt.plot(tmpdf['epoc'], tmpdf['fs'], 'b', label='false skip')
plt.plot(tmpdf['epoc'], tmpdf['ts'], 'r', label='true skip')
plt.plot(tmpdf['epoc'], tmpdf['fns'], 'g', label='false no-skip')
plt.plot(tmpdf['epoc'], tmpdf['tns'], 'm', label='true no-skip')
helper('')