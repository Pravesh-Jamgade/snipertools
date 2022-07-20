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
either run all apps  'python3 runAllApps.py $(folderPath) $(cores)'
or run single run app 'python3 runAllApps.py $(folderPath) $(cores) $(kernel)'

then, combine results for app
'''

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))
ax.fmt_ydata = 1.0

numCores = 0

x_axis = np.arange(int(numCores))
def plotGroup(name,df,appFolder):
	plt.plot(df['cache'], df['dead'])
	plt.plot(df['cache'], df['evicts'])
	plt.plot(df['cache'], df['inserts'])

'''
execute snipersim, move result to app dir
'''
def runAll(apps):
	for app in apps:
		appFolder = os.path.join(folderPath, app+'dir')

		cmd = 'make clean -C {}'.format(folderPath)
		print(cmd)
		os.system(cmd)

		cmd = 'mkdir {}'.format(appFolder)
		print(cmd)
		if os.path.exists(appFolder):
			rmcmd = 'rm -rf {}'.format(appFolder)
			os.system(rmcmd)
		os.system(cmd)

		cmd = 'make TARGET={} -C{}'.format(app, folderPath)
		print(cmd, os.getcwd())
		os.system(cmd)

		cmd = 'mv {}/cust* {}/'.format(folderPath,appFolder)
		print(cmd)
		os.system(cmd)

def mergeByApp(appFolder, app):
	mdf = pd.DataFrame()
	'''
	read file one by one by core basis and merge into our dataframe
	'''
	for i in range(numCores):
		fileName = 'customLog_c'+str(i)+'.log'
		filePath = os.path.join(appFolder, fileName)
		fileExists = os.path.exists(filePath)
		if not fileExists:
			print('file:',filePath,' ..not ok')
			continue
		print('file:',filePath,' ..ok')
		df = pd.read_csv(filePath)
		df.head()
		mdf=pd.concat([mdf,df],ignore_index=True)

	'''
	from shared appending to our dataframe
	'''
	fileName = None
	fileName = 'customLog_'+'shared.log'
	filePath = os.path.join(appFolder, fileName)
	fileExists = os.path.exists(filePath)
	if fileExists:
		print('file:',filePath, ' ..ok')
		df = pd.read_csv(filePath)
		mdf=pd.concat([mdf,df], ignore_index=True)
	else:
		print('file:',filePath, ' ..not ok')

	''' groupby cache and calculate mean ''' 
	# mdf=mdf.groupby('cache').mean()
	savePath = os.path.join(folderPath, app+'log.csv')
	mdf.to_csv(savePath)

	#sorted_df = mdf.sort_values(by=['core'], ascending=True)
	coredf = mdf.groupby('core')
	
	for name, grp in coredf:
		plotGroup(str(name), grp, appFolder)

	plt.savefig(os.path.join(appFolder,app+'.png'))
	plt.clf()

apps=['pr','bfs','cc','bc','sssp','tc']
perLevel=['L1-D', 'L2', 'L3']

folderPath = sys.argv[1]
numCores = int(sys.argv[2])

'''batch/single app check'''
check = len(sys.argv)>3
kernel=None
if check:
	kernel=sys.argv[3]

'''
run single or batch of apps
'''
if kernel == None:
	runAll(apps)
else:
	for app in apps:
		appFolder = os.path.join(folderPath, app+'dir')

		if os.path.exists(appFolder):
			rmcmd = 'rm -rf {}'.format(appFolder)
			os.system(rmcmd)
			print(rmcmd)

	apps=[]
	apps.append(kernel)
	runAll(apps)

'''
merge results by app
'''
for app in apps:
	appFolder = os.path.join(folderPath, app+'dir')
	if os.path.exists(appFolder):
		mergeByApp(appFolder, app)




