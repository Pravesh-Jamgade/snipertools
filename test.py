from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from scipy.stats import gmean
import statistics
import sys
import os


files=['customLog_12']
filePath=None
filLoc=None
if filePath == None:
    filePath = sys.argv[1]
    for file in files:
        fp=os.path.join(filePath, file + ".log")
        fileLoc=fp
        print(fp)
    filePath=filePath+'/'

df = pd.read_csv(fileLoc)
df.head()

columns=['fs','ts','fns','tns']
levels=['1','2','3']

tmp={'epoc':df['epoc'], 'lp':df['lp']}
newCol = []
for col in columns:
    colN=col+str(levels[0])
    tmp[colN]=df[colN]
    newCol.append(colN)
tmpf = pd.DataFrame(data=tmp)
print(tmpf)
tnum = tmpf.to_numpy()
x = tnum[:,1]
y = tnum[:,0]
print(x,y)

dx=x[1:]-x[:-1]

x2 = np.insert(x, np.where(dx>1)[0]+1, -1)
y2 = np.insert(y, np.where(dx>1)[0]+1, -1)

x2 = np.ma.masked_where(x2 == -1, x2)
y2 = np.ma.masked_where(y2 == -1, y2)

df=pd.DataFrame({'x':x2,'y':y2})
df.to_csv(filePath+'lp.csv')
pl.figure()
pl.subplot(121)
pl.plot(y,x,'k.')
pl.subplot(122)
pl.plot(y2,x2, 'k.')
pl.savefig('fig1.png')
