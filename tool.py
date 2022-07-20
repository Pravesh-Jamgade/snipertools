from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))

def helper():
	plt.grid(True, which='major', axis='y')
	plt.xlabel('set')
	plt.ylabel('count')
	plt.title("plot")
	plt.legend()
	plt.savefig('plot'+'.png')

import sys
path='~/Desktop/snipertools/2core.csv'
df = pd.read_csv(path)
df.head()

print(df)
plt.plot(df['x'], df['y'])
helper()
