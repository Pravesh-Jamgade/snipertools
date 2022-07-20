from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

fig, ax = plt.subplots(1, figsize=(20,10))
import sys

path= None
alias='cov'
if path == None:
    path = sys.argv[1]
else:
	print("test is on")

df = pd.read_csv(path)
df.head()

colmns=['lp','total']

off = len(df) * [0]
index = np.arange(len(df))
for j,col in enumerate(colmns):
    plt.bar(df['epoc'], df[col], bottom=off, label=col)
    off = off + df[col]

plt.xlabel('epoc')
plt.ylabel('accesses')
plt.legend()
plt.grid(True, which='major', axis='y')
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1000))#3
plt.savefig(path+'coverage' +'.png')