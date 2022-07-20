from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
fig, ax = plt.subplots(1, figsize=(20,10))

print("python3 stackedVert.py /mnt/B/sniper/test/gapbs")

alias = 'tc'
files=['customLog_2', 'customLog_3', 'customLog_4']
fileLoc = []
filePath=None

fileRepre = ['l1','l2','l3']

if filePath == None:
	filePath = sys.argv[1]
	for file in files:
		fp=os.path.join(filePath, file + ".log")
		fileLoc.append(fp)
		print(fp)
	print(filePath)
	filePath=filePath+'/'

def helpers(i,status):
	plt.xticks(rotation=90)
	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.gca().xaxis.set_major_locator(plt.MultipleLocator(100))
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))
	plt.grid(True, which='major', axis='y')
	plt.savefig(filePath+ fileRepre[i] + '-' + status + '-' + alias +'.png')
	plt.clf()

def getOrig(df):
	off = len(df) * [0]
	index = np.arange(len(df))
	for j,col in enumerate(columns):
		plt.bar(df['epoc'], df[col], bottom=off, color=colors[j], label=col)
		off = off + df[col]
	helpers(i, 'orig')

colors = ['red', '#008000', '#0000FF', '#FF00FF']

dfs=[]
for file in fileLoc:
	df = pd.read_csv('' + file)
	df.head()
	dfs.append(df)

columns = ['fs','ts','fns','tns']
for i,df in enumerate(dfs):
	# off = len(df) * [0]
	# for j,col in enumerate(columns):
	# 	plt.bar(df.index, df[col], 0.4, bottom=off)
	# 	off = off + df[col]
	# helpers(i, "ind")
	getOrig(df)


