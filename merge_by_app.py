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
merge by same app and save by app
'''

'''
from each core collect data and append to our empty dataframe mdf
'''
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



folderPath = sys.argv[1]
numCores = int(sys.argv[2])

'''batch/single app check'''
check = len(sys.argv)>3
kernel=None
if check:
	kernel=sys.argv[3]

perLevel=['L1-D', 'L2', 'L3']

mdf = pd.DataFrame()


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





