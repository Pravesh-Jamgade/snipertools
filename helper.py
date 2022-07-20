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

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))
ax.fmt_ydata = 1.0

'''generate stacked pc1,pc2,pc3 vertical bar graph. It is per epoc pc count'''
def pcPerEpoc(path, name, df, coreFolder):
	columns = ["pc1","pc2","pc3"]
	off = len(df) * [0]
	for j,col in enumerate(columns):
	    plt.bar(df['epoc'], df[col], label=col)
	    off = off + df[col]
	# plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))
	# plt.gca().xaxis.set_major_locator(plt.MultipleLocator(300))
	plt.grid(True, which='major', axis='y')
	plt.xticks(rotation=90)
	plt.title("PC per epoc")
	plt.legend()
	plt.savefig(coreFolder + '/pcPerEpoc-'+str(name)+'.png')
	plt.clf()

'''
generate top pc and total pc per core graph
'''
def topPCperEpoc(path, name, df, coreFolder):
	colmns=['top','total']
	off = len(df) * [0]
	index = np.arange(len(df))
	for j,col in enumerate(colmns):
		plt.bar(df['epoc'], df[col], bottom=off, label=col)
		off = off + df[col]
	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.grid(True, which='major', axis='y')
	# plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))#3
	plt.savefig(coreFolder+'/pccount-'+ str(name) +'.png')
	plt.clf()


'''
generate coverage by lp/total accesses, 
accuracy by how many of lp accurately match
 with results per core graph
'''
def coverageAndAccuracy(path, name, df, coreFolder):
	columns = ['epoc','total','lp','accuracy']
	df['A']=(df['lp']/df['total'])*100
	df['B']=(df['accuracy']/df['lp'])*100
	tdf = df.sample(n=50,replace=True,random_state=1)
	epoc = tdf['epoc'].tolist()
	cov = tdf['A'].tolist()
	acc = tdf['B'].tolist()
	x = np.arange(len(cov))  # the label locations
	width = 0.35  # the width of the bars
	fig, ax = plt.subplots()
	rects1 = ax.bar(x-width/2, tdf['A'], width, label='coverage')
	rects2 = ax.bar(x+width/2, tdf['B'], width, label='accuracy')
	fig.tight_layout()
	plt.xticks(rotation=90)
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(5))
	plt.grid(True, which='major', axis='y')
	dst=os.path.join(coreFolder,'CA-'+str(name)+'.png')
	plt.legend()
	plt.savefig(dst)
	plt.clf()

'''
generate graph for top access with top pc per core
TPA - top pc & accesses
'''
def topAccessAndPCCount(path,name,df,coreFolder):
	df=df.sample(n=100,replace=True,random_state=1)
	plt.bar(df['epoc'],df['toppcaccess'],color='r',label='top_pc_accesses')
	plt.bar(df['epoc'],df['toppccount'],bottom=df['toppccount'],color='y',label='top_pc_count')
	plt.grid(True, which='major', axis='y')
	plt.xticks(rotation=90)
	plt.legend()
	plt.savefig(coreFolder+'/TPA-'+str(name)+'.png')
	plt.clf()


'''
generate stacked graph for type access 
performance per cache level per core
'''
def typeofAccess(path,name,df,coreFolder):
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
		process(tmpf, newCol, level, path, name, coreFolder)


def result(path,name,df,coreFolder):
	columns=['epoc']
	for col in df.columns[1:]:
		columns.append(str(col))

	df.reindex(columns)

	print(df)
	levels=['1','2','3']
	types=['fs','ts','fns','tns']

	allSumPerLevel = []
	for level in levels:
		levelPerType = []
		for t in types:
			key=t+level
			levelPerType.append(df[key].sum())
		allSumPerLevel.append(levelPerType)

	perLevelHitMiss = []
	for index in range(len(allSumPerLevel)):
		levelSpecific = allSumPerLevel[index]
		miss =hit =0
		for jindex in range(len(levelSpecific)):
			if jindex == 0 or jindex == 3:
				hit = hit + levelSpecific[jindex]
			else:
				miss = miss + levelSpecific[jindex]

		perLevelHitMiss.append((miss,hit))


	template = ["fs", "ts", "fns", "tns"]

	for j in range(4):
		for i in range(3):
			template[j] = template[j] + "," + str(allSumPerLevel[i][j])

	tempHM = ["miss","hit"]
	for j in range(3):
		tempHM[0] = tempHM[0] + "," + str(perLevelHitMiss[j][0])
		tempHM[1] = tempHM[1] + "," + str(perLevelHitMiss[j][1])

	template.extend(tempHM)
	output = os.path.join(coreFolder, "result-"+str(name)+".log")
	f = open(output,'w')
	for line in template:
		f.write(line)
		f.write('\n')
	f.close()

'''
helper
'''
def process(df, newcol, level, path, name, coreFolder):
	# print(df.columns, newcol)
	off = len(df) * [0]
	for i,col in enumerate(newcol):
		plt.bar(df['epoc'], df[col], 0.4, label=col)
		# print(df[col])
		off = off + df[col]
	plt.legend()
	plt.savefig(coreFolder +'/T-'+str(level)+'-'+str(name)+'.png')
	plt.clf()


