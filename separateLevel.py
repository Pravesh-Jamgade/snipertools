from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os

'''
LP Type Access (TA) 
'''
fig, ax = plt.subplots(1, figsize=(20,10))

files=['customLog_12']
filePath=None
fileLoc=None

def process(df, level):
	df.to_csv(filePath+str(level)+'.csv')

if filePath == None:
	filePath = sys.argv[1]
	for file in files:
		fp=os.path.join(filePath, file + ".log")
		fileLoc=fp
		print(fp)
	filePath=filePath+'/'

df = pd.read_csv(fileLoc)
df.head()

columns=['fs','ts','fns','tns']
levels=['1','2','3']

for level in levels:
	tmp={'epoc':df['epoc'], 'lp':df['lp']}

	newCol = []
	for col in columns:
		colN=col+str(level)
		tmp[col]=df[colN]
		newCol.append(colN)
	tmpf = pd.DataFrame(data=tmp)
	process(tmpf, level)
