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

fig, ax = plt.subplots(1, figsize=(20,10))
'''
'''
def byEpocByCacheAvg(folderPath, df):
	
	tdf = df.groupby('epoc')

	mdf = {'epoc':[], 'l1':[], 'l2':[], 'l3':[]}

	for name, epocgrp in tdf:
		epoc=epocgrp['epoc'].tolist()
		avg=epocgrp['avg_missratio'].tolist()
		cash=epocgrp['cache'].tolist()
		mdf['epoc'].append(epoc[0])
		mdf['l1'].append(avg[0])
		mdf['l2'].append(avg[1])
		mdf['l3'].append(avg[2])

	udf=pd.DataFrame(data=mdf)

	for col in udf:
		if col == 'epoc':
			continue
		plt.plot(udf['epoc'], udf[col], label=col)
	plt.legend(loc='best')
	filePath=os.path.join(folderPath, 'abc.png')
	plt.savefig(filePath)
	plt.clf()


'''
log1
'''
def byEntireRun(folderPath, df):
	tdf=df.groupby('cache')
	for name,epocgrp in tdf:
		plt.plot(epocgrp['epoc'], epocgrp['skipthreshold'], label=name)

	plt.legend(loc='best')
	filePath=os.path.join(folderPath, 'xyz.png')
	plt.savefig(filePath)
	plt.clf()


# def xxx(folderPath, df):
# 	fig, ax = plt.subplots(1,1)
# 	plt.figure(figsize=(20,10))
# 	ax.fmt_ydata = 1.0

# 	plt.plot(newdf['epoc'], newdf['skip'], label="skip")
# 	# plt.plot(newdf['epoc'], newdf['noskip'], label="noskip")

# 	plt.gca().xaxis.set_major_locator(plt.MultipleLocator(50))

# 	#y ticks on interval
# 	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))

# 	# reference line with y ticks
# 	# plot grids only on y axis on major locations
# 	plt.grid(True, which='major', axis='y')

# 	# plt.xticks(newdf['epoc'], labels=newdf['epoc'])
# 	plt.xticks(rotation=90)
# 	plt.title("skip per epoc")
# 	plt.legend()
# 	plt.savefig('skipPerEpoc'+'.png')