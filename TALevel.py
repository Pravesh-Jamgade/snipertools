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
print("python3 TALevel.py /mnt/B/sniper/test/gapbs/customLog_9.log 2")

fig, ax = plt.subplots(1, figsize=(20,10))

colors = ['red', '#008000', '#0000FF', '#FF00FF']

# files=['l1']
filePath=None
fileLoc=None
level=None	

def helpers(level, tag=''):
	level='l'+str(level)
	plt.xticks(rotation=90)
	plt.xlabel('epoc')
	plt.ylabel('count')
	plt.legend()
	plt.grid(True, which='major', axis='y')
	plt.savefig('LTA-'+str(level)+tag+'.png')
	plt.clf()

def process(df):
	
	column = ['fs'+level,'ts'+level,'fns'+level,'tns'+level]
	tmp={'epoc':df.index}
	for col in column:
		tmp[col] = df[col]
	tmpf = pd.DataFrame(data=tmp)
	tmpf.head()
	print(tmpf)

	off = len(tmpf) * [0]
	for i,col in enumerate(column):
		plt.bar(tmpf['epoc'], tmpf[col], 0.4, bottom=off, label=col)
		off = off + tmpf[col]

	helpers(level)

if filePath == None:
	filePath = str(sys.argv[1])
	level = str(sys.argv[2])

df = pd.read_csv(filePath)
df.head()
process(df)
