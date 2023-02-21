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
		
'''
separate by cache name, sample
'''
def separate(filePath, fileName, fileNo, folderPath):
	df = pd.read_csv(filePath)
	df.head()
	if sample:
		df=df.sample(n=len(df)//4,replace=True,random_state=1)
	df=df.sort_values('epoc')
	df=df.groupby(" name")
	for name, group in df:
		group.to_csv(name+'_log_'+fileNo+'.log')

'''
for customLog_1.log, per pc miss ratio over entire run, separate by cache
'''
def separate2(filePath, fileName, fileNo, folderPath):
	df = pd.read_csv(filePath)
	df.head()
	df=df.groupby("cache")
	for name, group in df:
		group.to_csv(name+'_log_'+fileNo+'.log')

sample = False
folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

files = ['1']
for i in range(len(files)):
	fileName = 'customLog_' + str(files[i]) + '.log'
	filePath = os.path.join(folderPath, fileName)
	print("fileName:", fileName, '\n', "filePath:", filePath)
	separate2(filePath, fileName, files[i], folderPath)
	filePath=""




