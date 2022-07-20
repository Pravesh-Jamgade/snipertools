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
Not in Use
ouput: c$(coreid)_$(kernel).csv 
ex. c0_bfs.csv
'''
folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

resFolder = os.path.join(folderPath, 'rename')
isdir = os.path.isdir(resFolder)
if not isdir:
	os.mkdir(resFolder)

numCores = int(sys.argv[2])
app = str(sys.argv[3])

filePrefix = 'customLog_c'

'''file rename'''
for i in range(numCores):
	fileName = filePrefix+str(i)+'.log'
	filePath = os.path.join(folderPath, fileName)
	fileExists = os.path.exists(filePath)
	if not fileExists:
		continue
	print("fileName:", fileName, '\n', "filePath:", filePath)

	# rename file ex. c1_tc.log
	dstFilePath = os.path.join(resFolder, 'c'+str(i)+'_'+app+'.csv')
	os.rename(filePath, dstFilePath)
