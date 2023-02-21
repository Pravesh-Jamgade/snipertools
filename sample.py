from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
from statistics import mean
import math
import matplotlib.ticker as ticker
import os
import sys

filePath = None
if filePath == None:
	filePath = sys.argv[1]

df = pd.read_csv(filePath)
df.head()

df=df.sample(n=2,replace=False,random_state=1)
splits=filePath.split('/')
name=splits[len(splits)-1]
name="spl-"+name
print(name)
df.to_csv(name)
