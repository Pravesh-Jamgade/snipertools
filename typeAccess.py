from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os

'''
LP Type Access (TA) 
'''
fig, ax = plt.subplots(1, figsize=(20,10))

files=['customLog_5']
filePath=None
fileLoc=None

colors = ['red', '#008000', '#0000FF', '#FF00FF']

def helpers(level, tag=''):
	level='l'+str(level)
	plt.xticks(rotation=90)
	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.gca().xaxis.set_major_locator(plt.MultipleLocator(100))
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))
	plt.grid(True, which='major', axis='y')
	plt.savefig(filePath +'TA-'+str(level)+tag+'.png')
	plt.clf()

def indexed(newcol,level):
	off = len(df) * [0]
	for j,col in enumerate(newcol):
		plt.bar(df.index, df[col], bottom=off, color=colors[j], label=columns[j])
		off = off + df[col]
	plt.plot(df.index, df['lp'], marker=".", linestyle="", color="k")
	helpers(level,"ind")

def process(df, newcol, level):
	off = len(df) * [0]
	# for j,col in enumerate(newcol):
	# 	plt.bar(df['epoc'], df[col], bottom=off, color=colors[j], label=columns[j])
	# 	off = off + df[col]
	plt.bar(df.index, df[newcol[0]], label=newcol[0], color=colors[0])
	plt.bar(df.index, df[newcol[1]], label=newcol[1], color=colors[1])
	plt.bar(df.index, df[newcol[2]], label=newcol[2], color=colors[2])
	plt.bar(df.index, df[newcol[3]], bottom=df[newcol[3]],label=newcol[3], color=colors[3])
	# df['lp']=df['lp']-(df[newcol[0]]+df[newcol[1]]+df[newcol[2]]+df[newcol[3]])
	plt.plot(df.index, df['lp'], marker=".", linestyle="", color="k")
	# df.to_csv(filePath+str(level)+'.csv')
	helpers(level)

if filePath == None:
	filePath = sys.argv[1]
	for file in files:
		fp=os.path.join(filePath, file + ".log")
		fileLoc=fp
		print(fp)
	filePath=filePath+'/'

df = pd.read_csv(fileLoc)
df.head()

columns=['fs','ts','fns','tns']
levels=['1','2','3']

for level in levels:
	tmp={'epoc':df['epoc'], 'lp':df['lp']}

	newCol = []
	for col in columns:
		colN=col+str(level)
		tmp[colN]=df[colN]
		newCol.append(colN)
	tmpf = pd.DataFrame(data=tmp)
	print(tmpf)
	process(tmpf, newCol, level)
