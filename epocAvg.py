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


def byKeyAvg(key, df):
	df = df.groupby(key)
	col='missratio'
	keyvalues=[]
	avg=[]
	for name, group in df:
		gm=mean(group.loc[:,col])
		keyvalues.append(name)
		avg.append(gm)

	kdf=pd.DataFrame(columns=[key,'avg'])

	kdf[key]=keyvalues
	kdf['avg']=avg

	kdf.to_csv(os.path.join(folderPath,"customLog_3_"+key+".log"))

folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

fileName = 'customLog_3.log'
filePath = os.path.join(folderPath, fileName)

df = pd.read_csv(filePath)
df.head()

df = df.groupby('core')

for name,group in df:
	#group by epoc only
	byKeyAvg('epoc',group)

	#group by cache only
	byKeyAvg('cache',group)

epocList=[]
cacheList=[]
meanList=[]
#core
for core, group1 in df:
	df_epoc = group1.groupby('epoc')
	#epoc
	for epoc, group2 in df_epoc:
		df_cache = group2.groupby('cache')
		#cache
		for cache, group3 in df_cache:
			epocList.append(epoc)
			cacheList.append(cache)
			meanList.append(mean(group3.loc[:,'missratio']))

tdf=pd.DataFrame(columns=['epoc','cache','avg_missratio'])
tdf['epoc']=epocList
tdf['cache']=cacheList
tdf['avg_missratio']=meanList

tdf.to_csv(os.path.join(folderPath,"customLog_3_byEpocbyCache"+".log"))

		





