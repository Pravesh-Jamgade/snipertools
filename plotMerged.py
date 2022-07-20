
import sys
import os
import numpy as np
import pandas as pd
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import math
import matplotlib.ticker as ticker
import os
import sys

'''
NOt is Use
'''
fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))
ax.fmt_ydata = 1.0

apps=['pr','bfs','cc','bc','sssp','tc']

cdf = pd.DataFrame()
pdf = pd.DataFrame()

folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

def plotFig(ykey):
	if ykey=='count':
		ylabel='deadblocks count'
	else:
		ylabel='deadblocks % = (deadblocks/total inserted blocks) *100'
	for app in apps:
		fileName = app+'.csv'
		filePath = os.path.join(folderPath, fileName)
		fileExists = os.path.exists(filePath)
		if not fileExists:
			print('status: not found', filePath)
			continue
		df = pd.read_csv(filePath)
		df.head()
		print(df)
		plt.plot(df['cache'], df[ykey], label=app)
		plt.legend()
		plt.xlabel('cache level')
		plt.ylabel()
		plt.savefig( os.path.join(folderPath, 'all-kernel-deadblocks-'+ykey+'.png'))
	plt.clf()

plotFig('count')
plotFig('percentage')

	
	

	




