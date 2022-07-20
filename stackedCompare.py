from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
fig, ax = plt.subplots(1, figsize=(20,10))

print(" python3 stackedCompare.py /mnt/B/sniper/test/gapbs")

alias = 'tc'
files=['customLog_2', 'customLog_3', 'customLog_4']
filePath=None
fileLoc = []

study=['fs','ts','fns','tns']
colmns = ['l1','l2','l3']

if filePath == None:
	filePath = sys.argv[1]
	for file in files:
		fp=os.path.join(filePath, file + ".log")
		fileLoc.append(fp)
		print(fp)
	print(filePath)
	filePath=filePath+'/'

# status is whether indexing is based on epoc (status=orig) or based on index of rows(0,1,2...) (status='ind')
def helpers(typeComp, status):
	plt.xticks(rotation=90)
	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend(colmns)
	plt.savefig(filePath + 'cmp-' + typeComp + '-' + status + '-' + alias +'.png')
	plt.clf()

def getOrig(df, typeComp):
	df.head()
	off = len(df) * [0]
	for i,col in enumerate(colmns):
		plt.bar(df['epoc'], df[col], 0.4, bottom=off, color=colors[i])
		off = off + df[col]
	helpers(typeComp, 'orig')

colors = ['red', '#008000', '#0000FF', '#FF00FF']

dfs=[]
for path in fileLoc:
	df = pd.read_csv(path)
	df.head()
	dfs.append(df)

for s in study:
	tmpd = {'epoc': dfs[0]['epoc'], 'l1':dfs[0][s], 'l2':dfs[1][s], 'l3':dfs[2][s]}
	tmpdf = pd.DataFrame(data=tmpd)
	getOrig(tmpdf, s)
	# off = len(df) * [0]
	# for i,col in enumerate(colmns):
	# 	plt.bar(tmpdf.index, tmpdf[col], 0.4, bottom=off)
	# 	off = off + tmpdf[col]
	# helpers(s,'ind')
	
	
