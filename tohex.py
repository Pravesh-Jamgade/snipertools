from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os

newname=['A','B']
df = pd.read_csv('/home/pravesh/Desktop/snipertools/c11160M.log', sep=" ")
df.head()

df.columns = newname

df['A']=df['A'].apply(int)
df['A']=df['A'].apply(hex)

df.to_csv('trace.out',index=False, header=False, sep=" ")

