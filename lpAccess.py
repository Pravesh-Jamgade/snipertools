from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
fig, ax = plt.subplots(1, figsize=(30,10))

alias = 'tc'
files=['customLog_9', 'customLog_10']
filePath=None
fileLoc = []

def helpers():
	plt.xticks(rotation=90)
	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.grid(True, which='major', axis='y')
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))#3
	plt.savefig(filePath + '-lp-access-' + alias +'.png')
	plt.clf()

if filePath == None:
	filePath = sys.argv[1]
	for file in files:
		fp=os.path.join(filePath, file + ".log")
		fileLoc.append(fp)
		print(fp)
	print(filePath)
	filePath=filePath+'/'

dfs=[]
for file in fileLoc:
	df = pd.read_csv('' + file)
	df.head()
	dfs.append(df)

dfs[0]['match']=dfs[1]['match']
dfs[0]['total']=dfs[0]['total']-dfs[0]['lp']
dfs[0]['lp']=dfs[0]['lp']-dfs[0]['match']

dfs[0].rename(columns={'total':'lp-miss', 'lp':'lp-missmatch', 'match':'lp-match'}, inplace=True)

columns=['lp-miss', 'lp-missmatch', 'lp-match']
colors=['r','k','b']
print(dfs[0])
off = len(df) * [0]
for j,col in enumerate(columns):
	plt.bar(dfs[0].index, dfs[0][col], 1, label=col, color=colors[j], bottom=off)
	off = off + dfs[0][col]

helpers()