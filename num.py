'''
separate per core data
'''
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
from statistics import mean
import math
import matplotlib.ticker as ticker
import os
import sys

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(25,15))
ax.fmt_ydata = 1.0

allMsg=[]

def printFunc(msg,val):
	msg=msg+str(val)+'\n'
	allMsg.append(msg)

############################################################################
'''
generate coverage by lp/total accesses, 
accuracy by how many of lp accurately match
 with results per core graph
'''
def coverageAndAccuracy(path, name, df, coreFolder):
	# create columns by levels

	tdf =df #df.sample(n=50,replace=True,random_state=1)

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
	# plt.gca().yaxis.set_major_locator(plt.MultipleLocator(5))
	plt.grid(True, which='major', axis='y')
	plt.xlabel('epoc')
	plt.ylabel('coverage % = (LPT hit/Total Access), accuracy % = (matching prediction & actual/ LPT hit)')
	plt.legend()

	dst=os.path.join(coreFolder,'CA-'+str(name)+'.png')
	
	fig.set_figheight(15)
	fig.set_figwidth(30)

	plt.savefig(dst)
	plt.clf()


#===================================================

color = ['red', 'green', 'blue', 'black']

'''
generate stacked graph for type access 
performance per cache level per core
'''
def LtypeofAccess(path,name,df,coreFolder):
	cols=['fs','ts','fns','tns']
	
	df.plot(x="epoc", y=['fsp','tsp','fnsp','tnsp'], kind="bar",figsize=(30,15))

	plt.xticks(rotation=90)
	# plt.gca().yaxis.set_major_locator(plt.MultipleLocator())
	plt.grid(True, which='major', axis='y')

	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.savefig(coreFolder +'/T-'+str(name)+'.png')
	plt.clf()
	

'''
generate graph of covergae hit-miss percentage
'''
def Lcoverage_hitmiss(path,name,df,coreFolder):
	
	cols=['cmrp', 'chrp','cmpp','chpp']

	df.plot(x="epoc", y=cols, kind="bar",figsize=(30,15))

	fig.tight_layout()
	plt.xticks(rotation=90)
	# plt.gca().yaxis.set_major_locator(plt.MultipleLocator())
	plt.grid(True, which='major', axis='y')

	plt.xlabel('epoc')
	plt.ylabel('hit or miss %')
	plt.legend()

	plt.savefig(coreFolder +'/CHM-'+str(name)+'.png')
	plt.clf()


'''
generate graph of access hit-miss percentage
'''
def Laccess_hitmiss(path,name,df,coreFolder):
	
	cols=['amp','ahp']

	x = np.arange(len(df))  # the label locations

	width = 0.35  # the width of the bars
	fig, ax = plt.subplots()
	rects1 = ax.bar(x-width/2, df['amp'], width, label='miss')
	rects2 = ax.bar(x+width/2, df['ahp'], width, label='hit')

	plt.xlabel('epoc')
	plt.ylabel('hit or miss count')
	plt.legend()

	fig.tight_layout()
	plt.xticks(rotation=90)
	# plt.gca().yaxis.set_major_locator(plt.MultipleLocator())
	plt.grid(True, which='major', axis='y')

	dst=os.path.join(coreFolder,'CA-'+str(name)+'.png')
	
	fig.set_figheight(15)
	fig.set_figwidth(30)

	plt.savefig(coreFolder +'/AHM-'+str(name)+'.png')
	plt.clf()


#======================Stacked======================
'''
stacked
generate stacked graph for type access 
performance per cache level per core
'''
def typeofAccess(path,name,df,coreFolder):
	df=df.sample(n=len(df)//4,replace=True,random_state=1)
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
stacked
generate graph of covergae hit-miss percentage
'''
def coverage_hitmiss(path,name,df,coreFolder):
	df['cmp']=df['cm']#/df['coverage'])*percent
	df['chp']=df['ch']#/df['coverage'])*percent
	df=df.sample(n=len(df)//4,replace=True,random_state=1)
	cols=['cmp','chp']
	off = len(df) * [0]
	for i,col in enumerate(cols):
		plt.bar(df.index, df[col], 5, label=col)
		off = off + df[col]

	plt.xlabel('epoc')
	plt.ylabel('hit or miss count')
	plt.legend()
	plt.savefig(coreFolder +'/CHM-'+str(name)+'.png')
	plt.clf()

'''
stacked
generate graph of access hit-miss percentage
'''
def access_hitmiss(path,name,df,coreFolder):
	df['amp']=df['tm']#/df['totalaccess'])*percent
	df['ahp']=df['th']#/df['totalaccess'])*percent
	df=df.sample(n=len(df)//4,replace=True,random_state=1)
	cols=['amp','ahp']
	off = len(df) * [0]
	for i,col in enumerate(cols):
		plt.bar(df['epoc'], df[col], 5, label=col)
		off = off + df[col]

	plt.xlabel('epoc')
	plt.ylabel('hit or miss count')
	plt.legend()
	plt.savefig(coreFolder +'/AHM-'+str(name)+'.png')
	plt.clf()


####################################################################

def getResults(rootFolder, coreFolder, coreName, tddf):

	leveldf=tddf.groupby("cache")

	for name, df in leveldf:
		if name == 'l1i':
			continue

		df=df.sample(n=50,replace=True,random_state=1)
		df=df.sort_values('epoc')

		df['fsp']=df['fs']#/df['coverage'])*percent
		df['tsp']=df['ts']#/df['coverage'])*percent
		df['fnsp']=df['fns']#/df['coverage'])*percent
		df['tnsp']=df['tns']#/df['coverage'])*percent

		df['amp']=df['tm']#/df['totalaccess'])*percent
		df['ahp']=df['th']#/df['totalaccess'])*percent

		df['cmrp']=df['cmr']#/df['coverage'])*percent
		df['chrp']=df['chr']#/df['coverage'])*percent
		df['cmpp']=df['cmp']#/df['coverage'])*percent
		df['chpp']=df['chp']#/df['coverage'])*percent

		df['A']=df['coverage']#/df['totalaccess'])*percent
		df['B']=df['accuracy']#/df['coverage'])*percent

		group=df
		

		printFunc('***** {} *****'.format(str(name)), "")

		#save cache level data by core
		levelPath=os.path.join(coreFolder, str(coreName)+"_"+name+".log")
		group.to_csv(levelPath)

		#coverage and accuracy
		coverageAndAccuracy(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("LP coverage and accuracy at: {} ...ok".format(name))
		gm=mean(df.loc[:,'A'])
		printFunc('coverage %:', gm)
		gm=mean(df.loc[:,'B'])
		printFunc('accuracy %:', gm)
		
		#type of access
		LtypeofAccess(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("Type of access: {} ...ok".format(name))
		cols=['fs','ts','fns','tns']
		for col in cols:
			col=col+'p'
			gm=mean(df.loc[:,col])
			printFunc(col+" %:", gm)

		#hit miss 
		Lcoverage_hitmiss(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("HitMiss count: {} ...ok".format(name))
		cols = ['cmp','chp']
		for col in cols:
			gm=mean(df.loc[:,col])
			if col =='cmp':
				printFunc('coverage miss %: ', gm)
			else:
				printFunc('coverage hit %: ', gm)

		#hit miss 
		Laccess_hitmiss(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("Access hit-miss count: {} ...ok".format(name))
		cols = ['amp','ahp']
		for col in cols:
			gm=mean(df.loc[:,col])
			if col =='amp':
				printFunc('access miss %: ', gm)
			else:
				printFunc('access hit %: ', gm)
		

'''
separate by core name
'''
def separate(filePath, fileName, folderPath):
	df = pd.read_csv(filePath)
	df.head()

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

		summaryFile = os.path.join(coreFolder, "summary-"+str(name)+".txt")
		f = open(summaryFile, "w")
		for msg in allMsg:
			f.write(msg)

percent=1
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




