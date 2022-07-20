'''
separate per core data
'''
import sys
import os
import numpy as np
import pandas as pd
import helper

def getResults(path, name, group, fileName, coreFolder):
	if fileName == 'customLog_1.log':
		print('pc per epoc count @ core:', name)
		helper.pcPerEpoc(path,name,group,coreFolder)
	if fileName == 'customLog_2.log':
		print('top pc per epoc count @ core:', name)
		helper.topPCperEpoc(path,name,group,coreFolder)
	if fileName == 'customLog_3.log':
		print('coverage and accuracy @ core:', name)
		helper.coverageAndAccuracy(path,name,group,coreFolder)
	if fileName == 'customLog_4.log':
		print('top pc and top accesses @ core:', name)
		helper.topAccessAndPCCount(path,name,group,coreFolder)
	if fileName == 'customLog_5.log':
		print('type accesses @ core:', name)
		helper.typeofAccess(path,name,group,coreFolder)
		helper.result(path,name,group,coreFolder)

def separate(filePath, fileName, folderPath):
	newlines = []
	file=open(filePath);
	size_t = 0
	i=0
	for line in file:
		allOf = line.split(',')
		if i==0:
			print(line)
			newlines.append(line)
			size_t=len(allOf)
			i=1
		else:
			if len(allOf)<size_t or len(allOf)>size_t:
				continue
			else:
				newlines.append(line)

	newfile=open(filePath,'w')
	for line in newlines:
		newfile.write(line)
	newfile.close()

	df = pd.read_csv(filePath)
	df.head()

	print(df)

	tdf=df.groupby('core')
	for name, group in tdf:
		coreFolder = os.path.join(folderPath,"core"+str(name))
		isdir = os.path.isdir(coreFolder)
		if not isdir:
			os.mkdir(coreFolder)
		getResults(folderPath, name, group, fileName, coreFolder)

folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

files = ['1', '2', '3', '4', '5']

for i in range(len(files)):
	fileName = 'customLog_' + files[i] + '.log'
	filePath = os.path.join(folderPath, fileName)
	print("fileName:", fileName, '\n', "filePath:", filePath)
	separate(filePath, fileName, folderPath)
	filePath=""
