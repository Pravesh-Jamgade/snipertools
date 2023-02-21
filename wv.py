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

cols = ['inter', 'intra']

def process(df):

	size_ana = []
	tdf = df.groupby('size')
	for name, group in tdf:
		inter=mean(group.loc[:,'inter'])
		intra=mean(group.loc[:,'intra'])
		temp = 'size,{},{},{}'.format(name, inter, intra)
		size_ana.append(temp)
		print(temp)
	print('\n')

	replacement_ana = []
	tdf = df.groupby('replacement')
	for name, group in tdf:
		inter=mean(group.loc[:,'inter'])
		intra=mean(group.loc[:,'intra'])
		temp = 'replacement,{},{},{}'.format(name, inter, intra)
		print(temp)
		replacement_ana.append(temp)
	print('\n')

	trace_ana = []
	tdf = df.groupby('trace')
	for name, group in tdf:
		inter=mean(group.loc[:,'inter'])
		intra=mean(group.loc[:,'intra'])
		temp = 'trace,{},{},{}'.format(name, inter, intra)
		print(temp)
		trace_ana.append(temp)

	


filePath = None
if filePath == None:
	filePath = sys.argv[1]

fileName = filePath.split('/')[-1]
print("filepath="+filePath)
df = pd.read_csv(filePath)
df.head()
process(df)