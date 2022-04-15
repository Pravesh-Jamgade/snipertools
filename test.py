from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

fig, ax = plt.subplots(1, figsize=(12, 10))
alias = 'tc'
colors = ['#FFC0CB', '#008000', '#0000FF', '#808080', '#FF00FF']#pink,green,blue,gray,magneta(purple shade)
fileName=['customLog_9.log']

def process(ind,file):
    df = pd.read_csv('' + file)
    df.head()

    fields = []
    labels = []

    for col in df:
        if col=='epoc':
            continue
        fields.append(col)   

        if col == 'np':
            labels.append("no-prediction")
            print(col, "no-prediction")
            continue

        if col == 'tsl':
            labels.append("true skip loss")
            print(col, "true skip loss")
            continue

        if col == 'tso':
            labels.append("true skip opportunity")
            print(col, "true skip opportunity")
            continue

        if col == 'fs':
            labels.append("false skip")
            print(col, "false skip")
            continue

        if col == 'h':
            labels.append("hit")
            print(col, "hit")
            continue

        if col == 'm':
            labels.append("miss")
            print(col, "miss")
            continue

        else:
            labels.append(col)
            print(col, col)

    

    left=len(df) * [0]

    for idx, name in enumerate(fields):
        plt.barh(df.index, df[name], left=left, color=colors[idx])
        left=left+df[name]

    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # adjust limits and draw grid lines
    # plt.ylim(-0.5, ax.get_yticks()[-1] + 0.5)
    ax.set_axisbelow(True)
    ax.xaxis.grid(color='gray', linestyle='dashed')

    # title, legend, labels
    plt.legend(labels, bbox_to_anchor=([0.55, 1, 0, 0]), ncol=4, frameon=False)
    plt.xlabel('metric/total')

    plt.savefig(file+'-'+ alias +'.png')


threads=[]
for ind,file in enumerate(fileName):
    process(ind,file)


