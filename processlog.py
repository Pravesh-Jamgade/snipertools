'''
separate per core data
'''
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
plt.figure(figsize=(25,15))
ax.fmt_ydata = 1.0

############################################################################
'''
generate coverage by lp/total accesses, 
accuracy by how many of lp accurately match
 with results per core graph
'''
def coverageAndAccuracy(path, name, df, coreFolder):
	# create columns by levels

	df['A']=(df['coverage']/df['totalaccess'])*100
	df['B']=(df['accuracy']/df['coverage'])*100

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
	plt.xlabel('epoc')
	plt.ylabel('coverage % = (LPT hit/Total Access), accuracy % = (matching prediction & actual/ LPT hit)')
	plt.legend()

	dst=os.path.join(coreFolder,'CA-'+str(name)+'.png')
	
	fig.set_figheight(15)
	fig.set_figwidth(30)

	plt.savefig(dst)
	plt.clf()


'''
generate stacked graph for type access 
performance per cache level per core
'''
def typeofAccess(path,name,df,coreFolder):
	df=df.sample(n=300,replace=True,random_state=1)
	cols=['fs','ts','fns','tns']
	off = len(df) * [0]
	for i,col in enumerate(cols):
		plt.bar(df.index, df[col], 5, label=col)
		off = off + df[col]

	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.savefig(coreFolder +'/T-'+str(name)+'.png')
	plt.clf()

'''
generate graph of hit/miss
'''
def hitmiss(path,name,df,coreFolder):
	df['miss']=df['fns']+df['ts']
	df['hit']=df['tns']+df['fs']
	df=df.sample(n=300,replace=True,random_state=1)
	cols=['hit','miss']
	off = len(df) * [0]
	for i,col in enumerate(cols):
		plt.bar(df.index, df[col], 5, label=col)
		off = off + df[col]

	plt.xlabel('epoc')
	plt.ylabel('hit or miss count')
	plt.legend()
	plt.savefig(coreFolder +'/HM-'+str(name)+'.png')
	plt.clf()

# '''
# generate graph of hit/miss
# '''
# def hitmiss(path,name,df,coreFolder):
# 	df['miss']=df['fns']+df['ts']
# 	df['hit']=df['tns']+df['fs']
# 	df=df.sample(n=300,replace=True,random_state=1)
# 	cols=['hit','miss']
# 	off = len(df) * [0]
# 	for i,col in enumerate(cols):
# 		plt.bar(df.index, df[col], 5, label=col)
# 		off = off + df[col]

# 	plt.xlabel('epoc')
# 	plt.ylabel('hit or miss count')
# 	plt.legend()
# 	plt.savefig(coreFolder +'/HM-'+str(name)+'.png')
# 	plt.clf()

####################################################################

def getResults(rootFolder, coreFolder, coreName, df):

	leveldf=df.groupby("cache")

	for name, group in leveldf:
		if name == 'l1i':
			continue

		#save cache level data by core
		levelPath=os.path.join(coreFolder, str(coreName)+"_"+name+".log")
		group.to_csv(levelPath)

		#coverage and accuracy
		coverageAndAccuracy(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("LP coverage and accuracy at: {} ...ok".format(name))

		#type of access
		typeofAccess(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("Type of access: {} ...ok".format(name))

		#hit miss 
		hitmiss(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("HitMiss count: {} ...ok".format(name))
	
'''
separate by core name
'''
def separate(filePath, fileName, folderPath):
	# # enable only if data is inconsistent across rows 
	# newlines = []
	# file=open(filePath);
	# size_t = 0
	# i=0
	# for line in file:
	# 	allOf = line.split(',')
	# 	if i==0:
	# 		print(line)
	# 		newlines.append(line)
	# 		size_t=len(allOf)
	# 		i=1
	# 	else:
	# 		if len(allOf)<size_t or len(allOf)>size_t:
	# 			continue
	# 		else:
	# 			newlines.append(line)

	# newfile=open(filePath,'w')
	# for line in newlines:
	# 	newfile.write(line)
	# newfile.close()

	df = pd.read_csv(filePath)
	df.head()

	print(df)

	tdf=df.groupby('core')
	for name, group in tdf:
		coreFolder = os.path.join(folderPath,"core"+str(name))
		isdir = os.path.isdir(coreFolder)
		if not isdir:
			os.mkdir(coreFolder)
		coreFilePath = os.path.join(coreFolder, "core"+str(name))
		group.to_csv(coreFilePath)

		print("core:{}, at:{} ...ok".format(name, coreFolder))
		
		getResults(folderPath, coreFolder, name, group)

folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

files = ['4']

for i in range(len(files)):
	fileName = 'customLog_' + str(files[i]) + '.log'
	filePath = os.path.join(folderPath, fileName)
	print("fileName:", fileName, '\n', "filePath:", filePath)
	separate(filePath, fileName, folderPath)
	filePath=""



