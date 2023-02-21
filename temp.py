from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
from utility import *

path=sys.argv[1]
df = read_csv(path)
cols = ['pc', 'addr']

df=apply_colnames(df, cols)

df=to_int(df, 'addr')

df=df[df['addr']>0]

path = path + '-new'
# to_csv(df,path)
print(df['pc'].value_counts())

tdf=df.groupby( (df['pc'].shift() != df['pc']).cumsum() )

# print(tdf)
# for k,v in tdf:
# 	print(f'[group {k}]')
# 	print(v)

import pandas as pd
technologies   = ({
    'Courses':["Spark","Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python"],
    'Fee' :[22000,25000,25000,23000,24000,26000,25000,25000,22000],
    'Duration':['30days','9days','50days','35days','40days','60days','35days','55days','50days'],
    'Discount':[1000,34,2300,1000,1200,2500,1300,1400,1600]
                })
df = pd.DataFrame(technologies, columns=['Courses','Fee','Duration','Discount'])

tdf=df.groupby(df['Courses'])
df['diff']=tdf.Fee.diff()

print(df)

