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


class Cache:
	def __init__(self, cacheName):
		self.cacheName=cacheName
		self.coverage=0
		self.accuracy=0
		self.fs=self.fns=self.ts=self.tns=0
		self.cm=self.ch=0
		self.am=self.ah=0

class Core:
	def __init__(self, coreId, cacheName):
		self.coreId=coreId
		self.cache=Cache(cacheName)
	def allValues(self):
		return "{},{},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}\n".format(self.coreId,self.cache.cacheName,self.cache.coverage,self.cache.accuracy,self.cache.ch,self.cache.cm, self.cache.ah, self.cache.am, self.cache.fs, self.cache.ts, self.cache.fns, self.cache.tns)

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
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator())
	plt.grid(True, which='major', axis='y')

	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.savefig(coreFolder +'/T-'+str(name)+'.png')
	plt.clf()
	


def Lcoverage_hitmiss_helper(cols, path,name,df,coreFolder):
	df.plot(x="epoc", y=cols, kind="bar",figsize=(30,15))

	fig.tight_layout()
	plt.xticks(rotation=90)
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator())
	plt.grid(True, which='major', axis='y')

	plt.xlabel('epoc')
	plt.ylabel('hit or miss %')
	plt.legend()

	plt.savefig(coreFolder +'/CHM-'+str(name)+'.png')
	plt.clf()

'''
generate graph of covergae hit-miss percentage
'''
def Lcoverage_hitmiss(path,name,df,coreFolder):
	
	cols1=['cmrp', 'cmpp']
	Lcoverage_hitmiss_helper(cols1, path,str(name)+'_miss',df,coreFolder)
	cols2=['chrp', 'chpp']
	Lcoverage_hitmiss_helper(cols2, path,str(name)+'_hit',df,coreFolder)


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
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator())
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
	df['cmp']=(df['cm']/df['coverage'])*percent
	df['chp']=(df['ch']/df['coverage'])*percent
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
	df['amp']=(df['tm']/df['totalaccess'])*percent
	df['ahp']=(df['th']/df['totalaccess'])*percent
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


allResults = []

def getResults(rootFolder, coreFolder, coreName, tddf):

	leveldf=tddf.groupby("cache")

	for name, df in leveldf:
		if name == 'l1i':
			continue

		coreobj = Core(coreName, name)

		print("*** thie is {}".format(coreobj.cache.cacheName))

		df=df.sample(n=100,replace=False,random_state=1)
		df=df.sort_values('epoc')

		df['fsp']=(df['fs']/df['coverage'])*percent
		df['tsp']=(df['ts']/df['coverage'])*percent
		df['fnsp']=(df['fns']/df['coverage'])*percent
		df['tnsp']=(df['tns']/df['coverage'])*percent

		df['amp']=(df['tm']/df['totalaccess'])*percent
		df['ahp']=(df['th']/df['totalaccess'])*percent

		df['cmrp']=(df['cmr']/df['coverage'])*percent
		df['chrp']=(df['chr']/df['coverage'])*percent
		df['cmpp']=(df['cmp']/df['coverage'])*percent
		df['chpp']=(df['chp']/df['coverage'])*percent

		df['A']=(df['coverage']/df['totalaccess'])*percent
		df['B']=(df['accuracy']/df['coverage'])*percent

		group=df
		

		printFunc('***** {} *****'.format(str(name)), "")

		group['total_access'] = group['totalaccess'].sum()
		group['thits'] = group['th'].sum()
		group['tmiss'] = group['tm'].sum()

		group['total_coverage'] = group['coverage'].sum()

		group['chits'] = group['chr'].sum()
		group['cmiss'] = group['cmr'].sum()

		group['phits'] = group['chp'].sum()
		group['pmiss'] = group['cmp'].sum()

		#save cache level data by core
		levelPath=os.path.join(coreFolder, str(coreName)+"_"+name+".log")
		group.to_csv(levelPath)

		#coverage and accuracy
		coverageAndAccuracy(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("LP coverage and accuracy at: {} ...ok".format(name))
		gm=mean(df.loc[:,'A'])
		printFunc('coverage %:', gm)
		coreobj.cache.coverage=gm
		gm=mean(df.loc[:,'B'])
		printFunc('accuracy %:', gm)
		coreobj.cache.accuracy=gm
		
		#type of access
		LtypeofAccess(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("Type of access: {} ...ok".format(name))
		cols=['fs','ts','fns','tns']
		for col in cols:
			tmp=col+'p'
			gm=mean(df.loc[:,tmp])
			printFunc(tmp+" %:", gm)
			if col=='fs':
				coreobj.cache.fs=gm
			if col=='fns':
				coreobj.cache.fns=gm
			if col=='ts':
				coreobj.cache.ts=gm
			if col=='tns':
				coreobj.cache.tns=gm

		#hit miss 
		Lcoverage_hitmiss(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("HitMiss count: {} ...ok".format(name))
		cols = ['cm','ch']
		for col in cols:
			tmp=col+'pp'
			gm=mean(df.loc[:,tmp])
			if tmp =='cmpp':
				printFunc('coverage miss %: ', gm)
				coreobj.cache.cm=gm
			else:
				printFunc('coverage hit %: ', gm)
				coreobj.cache.ch=gm

		#hit miss 
		Laccess_hitmiss(rootFolder, "core"+str(coreName)+"_"+name, group, coreFolder)
		print("Access hit-miss count: {} ...ok".format(name))
		cols = ['am','ah']
		for col in cols:
			tmp=col+'p'
			gm=mean(df.loc[:,tmp])
			if tmp =='amp':
				printFunc('access miss %: ', gm)
				coreobj.cache.am=gm
			else:
				printFunc('access hit %: ', gm)
				coreobj.cache.ah=gm

		allResults.append(coreobj)
		

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
		f.close()

	summaryFile = os.path.join(coreFolder, "summary-excel"+str(name)+".txt")
	f = open(summaryFile, "w")
	f.write("core,cache, coverage, accuracy, coverage hit, coverage miss, access hit, access miss, fs, ts, fns, tns\n");

	for obj in allResults:
		msg = obj.allValues()
		f.write(msg)


percent=100
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




