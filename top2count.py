from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
fig, ax = plt.subplots(1, figsize=(40,30))

files=['customLog_11']
filePath=None
fileLoc=None
if filePath == None:
	filePath = sys.argv[1]
	for file in files:
		fp=os.path.join(filePath, file + ".log")
		fileLoc=fp
		print(fp)
	filePath=filePath+'/'

df = pd.read_csv(fileLoc)
df.head()

plt.bar(df['epoc'],df['toppcaccess'],color='r',label='top_pc_accesses')
plt.bar(df['epoc'],df['toppccount'],bottom=df['toppccount'],color='k',label='top_pc_count')
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(100))
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))
plt.grid(True, which='major', axis='y')
plt.xticks(rotation=90)
plt.savefig(filePath+'top-pc-accesss.png')
