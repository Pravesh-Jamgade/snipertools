from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
fig, ax = plt.subplots(1, figsize=(30,10))
level='level'
alias = 'tc'
colors = ['red', '#008000', '#0000FF', '#FF00FF']
fileName=['/mnt/B/sniper/test/gapbs/customLog_13.log']

df = pd.read_csv('' + fileName[0])
df.head()

colmns = ['fs','ts','fns','tns']
off = len(df) * [0]
index = np.arange(len(df))
for i,col in enumerate(colmns):
	plt.bar(df['epoc'], df[col], bottom=off)
	off = off + df[col]

plt.xticks(rotation=90)
plt.xlabel('epoc')
plt.ylabel('count')
plt.legend(colmns)
plt.savefig(fileName[0]+'-orig-'+ level +'-'+ alias +'.png')


