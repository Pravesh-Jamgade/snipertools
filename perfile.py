'''
separate per cache level data
'''
import sys
import os
import numpy as np
import pandas as pd
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import math
import matplotlib.ticker as ticker
import os
import sys

'''
Not in use

python3 perfile.py $(folderPath) $(cores)

It generates dba/ folder, where it stores the plot of DeadBlocks vs epoc 
and %DeadBlock vs epoc per for cache level per core

shared core log file sometimes not processable, because of its large size
In such cases run it separately, by moving other log to backup folder and ran the script again
'''
fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))
ax.fmt_ydata = 1.0

def plotAvgPerSet(name, path, df):
	dist = df['avgDbPerSet'].size
	dist = 1
	plt.plot(df['epoc'], df['avgDbPerSet'], label=name, color='red')
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(dist))
	plt.grid(True, which='major', axis='y')
	plt.ylabel("(DeadBlocks/TotalBlocks) * 100")
	plt.legend()
	plt.savefig(path)
	plt.clf()

def plotDB(name, path, df):
	dist1 = df['dbPerCache'].size
	dist2 = df['dbPerCache'].max()

	dist = min(dist2/50, dist1/50)
	plt.plot(df['epoc'], df['dbPerCache'], label=name, color='blue')
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(dist))
	plt.grid(True, which='major', axis='y')
	plt.ylabel("DeadBlocks")
	plt.legend()
	plt.savefig(path)
	plt.clf()

def getResults(name, group):
	filePath = os.path.join(folderPath,name+'.csv')
	group.to_csv(filePath)

	filePath = os.path.join(resFolder, name+".png")
	plotDB(name, filePath, group)

	filePath = os.path.join(resFolder, name+"-avg-set.png")
	plotAvgPerSet(name, filePath, group)


def separate(filePath, i):
	df = pd.read_csv(filePath)
	df.head()
	tdf=df.groupby('cache')

	for name, group in tdf:
		getResults(name+'-c'+str(i), group)

folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

resFolder = os.path.join(folderPath, 'dba')
isdir = os.path.isdir(resFolder)
if not isdir:
	os.mkdir(resFolder)

numCores = int(sys.argv[2])
filePrefix = 'customLog_c'

for i in range(numCores):
	fileName = filePrefix+str(i)+'.log'
	filePath = os.path.join(folderPath, fileName)
	fileExists = os.path.exists(filePath)
	if not fileExists:
		continue
	print("fileName:", fileName, '\n', "filePath:", filePath)
	separate(filePath, i)

fileName = 'customLog_shared.log'
filePath = os.path.join(folderPath, fileName)
separate(filePath, 'shared')