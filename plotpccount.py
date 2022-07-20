from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

fig, ax = plt.subplots(1, figsize=(20,10))
# plot total pc count vs top pc count
import sys
path=''#'/mnt/B/sniper/test/gapbs/customLog_.log'
alias='tc'
if path == '':
    path = sys.argv[1]
else:
	print("test is on")

df = pd.read_csv(path)
df.head()

colmns=['top','total']

off = len(df) * [0]
index = np.arange(len(df))
for j,col in enumerate(colmns):
    plt.bar(df['epoc'], df[col], bottom=off, label=col)
    off = off + df[col]

plt.xlabel('epoc')
plt.ylabel('count')
plt.legend()
plt.grid(True, which='major', axis='y')
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))#3
plt.savefig(path+'-pccount-'+ alias +'.png')