from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import math
import matplotlib.ticker as ticker

import sys
path=''#'/mnt/B/sniper/test/gapbs/customLog_1.log'
if path == '':
    path = sys.argv[1]
    
df = pd.read_csv(path)
df.head()

fig, ax = plt.subplots(1,1)
plt.figure(figsize=(20,10))
ax.fmt_ydata = 1.0

columns = ["pc1","pc2","pc3"]
off = len(df) * [0]
for j,col in enumerate(columns):
    plt.bar(df['epoc'], df[col], bottom=off, label=col)
    off = off + df[col]

#y ticks on interval
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))#3

plt.gca().xaxis.set_major_locator(plt.MultipleLocator(300))#800

# reference line with y ticks
# plot grids only on y axis on major locations
plt.grid(True, which='major', axis='y')

plt.xticks(rotation=90)
plt.title("PC per EPOC")
plt.legend()
plt.savefig(path+'pcPerEpoc'+'.png')
