from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
fig, ax = plt.subplots(1, figsize=(20,10))
alias = 'tc'
colors = ['red', '#008000', '#0000FF', '#FF00FF']#red,green,blue,magneta(purple shade)
fileName=['/mnt/B/sniper/test/gapbs/customLog_4.log']

def process(ind,file):
    df = pd.read_csv('' + file)
    df.head()

    fields = []
    labels = []

    for col in df:
        if col=='epoc':
            continue
        fields.append(col)   
        labels.append(col)

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(50))#800
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(5))#3
    plt.grid(True, which='major', axis='y')
    plt.xticks(rotation=90)
    plt.bar(df['epoc'], df['fs'],linewidth=2)
    plt.bar(df['epoc'], df['ts'], linewidth=2)
    plt.bar(df['epoc'], df['fns'], linewidth=2)
    plt.bar(df['epoc'], df['tns'],bottom=df['fs'], linewidth=3)

    ax.set_axisbelow(True)
    ax.xaxis.grid(color='gray', linestyle='dashed')

    # title, legend, labels
    plt.legend(labels)
    plt.xlabel('epoc')
    plt.ylabel('count')

    plt.savefig(file+'-'+ alias +'.png')


threads=[]
for ind,file in enumerate(fileName):
    process(ind,file)


