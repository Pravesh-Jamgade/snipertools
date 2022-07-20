
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
'''
generate overall coverage and accuracy
'''
def process(df):
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
	folder = os.path.dirname(filePath)
	output = os.path.join(folder, "result.log")
	f = open(output,'w')
	for line in template:
		f.write(line)
		f.write('\n')
	f.close()
		

filePath=None
if filePath == None:
	filePath = str(sys.argv[1])

df = pd.read_csv(filePath)
df.head()
process(df)
