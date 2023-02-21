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

df = df.groupby('epoc')

for name,group in df:
	byKeyAvg('cache',group)

