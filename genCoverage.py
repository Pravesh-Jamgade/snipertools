from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

import sys
import os
path=''
if path == '':
    path = sys.argv[1]
else:
    pass

df = pd.read_csv(path)
df.head()

columns = ['epoc','total','lp','accuracy']

df['A']=(df['lp']/df['total'])*100
df['B']=(df['accuracy']/df['lp'])*100

# print(df)

tdf = df.sample(n=50,replace=False,random_state=1)

fileName=os.path.splitext(path)[0]
folderPath=os.path.dirname(path)
dst=os.path.join(folderPath,fileName)
print(dst)
tdf.to_csv(dst+'-sampled.log')

epoc = tdf['epoc'].tolist()
cov = tdf['A'].tolist()
acc = tdf['B'].tolist()

x = np.arange(len(cov))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, tdf['A'], width, label='coverage')
rects2 = ax.bar(x+width/2, tdf['B'], width, label='accuracy')

ax.legend()

fig.tight_layout()

plt.xticks(rotation=90)

dst=os.path.join(folderPath,fileName+'-cov+acc.png')
plt.savefig(dst)

