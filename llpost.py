
import sys
import os
import numpy as np
import pandas as pd

def process(df):
	print(df)
	
filePath=None
if filePath == None:
	filePath = str(sys.argv[1])

df = pd.read_csv(filePath)
df.head()
process(df)