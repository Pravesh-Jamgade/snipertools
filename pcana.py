from general import *
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

folderPath = None
if folderPath == None:
	folderPath = sys.argv[1]

fileName = 'customLog_3_byEpocbyCache.log'
filePath = os.path.join(folderPath, fileName)
df = pd.read_csv(filePath)
df.head()
byEpocByCacheAvg(folderPath, df)

fileName = 'customLog_3.log'
filePath = os.path.join(folderPath, fileName)
df = pd.read_csv(filePath)
df.head()
byEntireRun(folderPath, df)