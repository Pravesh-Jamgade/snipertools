from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from scipy.stats import gmean
import statistics
import sys
import os
import random
out=[]

tmp = 0xffffffff
for i in range(5):
    a = random.randint(0,5)
    a = tmp - a;
    op = random.randint(0,1) 
    val = random.randint(250,255)

    addr = str(a)
    oper = str(op)
    value = str(val)

    inp = oper+","+addr+","+value
    print(inp)

    