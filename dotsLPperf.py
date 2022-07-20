from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))

import sys
path=''#'/mnt/B/sniper/test/gapbs/customLog_5.log'
alias=''
if path == '':
    path = sys.argv[1]
    alias=sys.argv[2]
else:
	print("test is on")
df = pd.read_csv(path)
df.head()

def helper(label):
	#y ticks on interval
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))#3
	plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1000))#800
	plt.grid(True, which='major', axis='y')
	plt.xlabel('epoc')
	plt.ylabel('LP Perf')
	plt.ylim(ymax=1.0,ymin=0.0)
	plt.title("using epoc x-1 decision to compare how they are useful in x")
	plt.legend()
	plt.savefig('lpPerf-dots-'+label+alias+'.png')

def personalLine(label, mark, tag):
    ax.fmt_ydata = 1.0
    plt.plot(df['epoc'], df[label], mark, label=tag)
    helper(label)
    plt.clf()

df['total']=df['fs']+df['ts']+df['fns']+df['tns']
df['fs']=df['fs']/df['total']
df['ts']=df['ts']/df['total']
df['fns']=df['fns']/df['total']
df['tns']=df['tns']/df['total']

personalLine('fs', 'b.', 'false skip')
personalLine('ts', 'r.', 'true skip')
personalLine('fns', 'g.', 'false no-skip')
personalLine('tns', 'm.', 'true no-skip')

plt.plot(df['epoc'], df['fs'], 'b.', label='false skip')
plt.plot(df['epoc'], df['ts'], 'r.', label='true skip')
plt.plot(df['epoc'], df['fns'], 'g.', label='false no-skip')
plt.plot(df['epoc'], df['tns'], 'm.', label='true no-skip')
helper('')

