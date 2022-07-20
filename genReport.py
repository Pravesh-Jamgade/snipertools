from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os

df = pd.read_csv(filePath)#customLog_12.log
df.head()

print(df['fs1'])
levels = ['1','2','3']
types = ['fs','ts','fns','tns']

typeSumByLevel=[]
levelTotalList=[]

for level in levels:
	sumlist=[]
	for t in types:
		t=t+level
		val = df[t].sum()
		sumlist.append(val)

	typeSumByLevel.append(sumlist)

	leveltotal = 0
	for s in sumlist:
		leveltotal = leveltotal + s

	levelTotalList.append(leveltotal)

# for t in types:
# 	line = s+' '
# 	for level in typeSumByLevel:
# 		for s in level:
# 			print()



