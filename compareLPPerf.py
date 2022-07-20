from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

alias=''
fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))

def helper(label):
	#y ticks on interval
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))#3
	plt.gca().xaxis.set_major_locator(plt.MultipleLocator(500))#800
	plt.grid(True, which='major', axis='y', linestyle='-.', label='HelloWorld')
	plt.xlabel('epoc')
	plt.ylabel(label + ' ratio')
	plt.ylim(ymax=1.0,ymin=0.0)
	plt.xticks(rotation=90)
	plt.title("comparing "+label+" ratios for all levels")
	plt.legend()
	plt.savefig('lpPerf-compare-'+label+alias+'.png')

def personalLine(tmpdf, label, mark, tag):
    ax.fmt_ydata = 1.0
    plt.plot(tmpdf['epoc'], tmpdf[label], mark, label=tag)
    helper(label)
    plt.clf()

import sys
paths=[
	'/home/pravesh/Desktop/snipertools/t7/customLog_5.log',
	'/home/pravesh/Desktop/snipertools/t7/customLog_6.log',
	'/home/pravesh/Desktop/snipertools/t7/customLog_7.log'
	]

dfs=[]
for path in paths:
	df = pd.read_csv(path)
	df.head()
	dfs.append(df)

study=['fs','ts','fns','tns']

for s in study:
	tmpd = {'epoc': dfs[0]['epoc'], 'l1':dfs[0][s], 'l2':dfs[1][s], 'l3':dfs[2][s]}
	tmpdf = pd.DataFrame(data=tmpd)

	plt.plot(tmpdf['epoc'], tmpdf['l1'], 'ro',label='l1')
	plt.plot(tmpdf['epoc'], tmpdf['l2'], 'g^',label='l2')
	plt.plot(tmpdf['epoc'], tmpdf['l3'], 'bo',label='l3')
	helper(s)
	plt.clf()

