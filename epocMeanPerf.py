from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics

fig, ax = plt.subplots(1, figsize=(12, 10))
alias = 'tc'
colors = ['#FFC0CB', '#008000', '#0000FF', '#FF00FF']#pink,green,blue,magneta(purple shade)

def process():
    df = pd.read_csv('/mnt/B/sniper/test/gapbs/customLog_2.log')
    df.head()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # print (df['pc'])
    # df.drop(df['pc'], axis=1)
    # df=df.groupby(df['epoc']).prod()
    # df=np.sqrt(df[:])
    # df = df.set_index(['epoc'])
    df=df[df.columns.drop('pc')]
    print(df)

    # df['l1d']=1-df['l1d']
    # df['l2']=1-df['l2']
    # df['l3']=1-df['l3']
    print(df)
    
    t=df.pivot_table(columns=['epoc'],aggfunc='size').to_list()
    l1d=df.groupby('epoc')['l1d'].apply(list)
    l2=df.groupby('epoc')['l2'].apply(list)
    l3=df.groupby('epoc')['l3'].apply(list)
    epoc=df['epoc'].unique()
    newd={'epoc':epoc,'l1d':l1d.values, 'l2':l2.values, 'l3':l3.values}
    newdf=pd.DataFrame(data=newd)
    print(newdf)

    newl1=[]
    newl2=[]
    newl3=[]
    for e in l1d.values:
    	newl1.append(statistics.mean(e))
    for e in l2.values:
    	newl2.append(statistics.mean(e))
    for e in l3.values:
    	newl3.append(statistics.mean(e))
    
    tmpd={'epoc':epoc, 'l1d':newl1, 'l2':newl2, 'l3':newl3}
    tmpdf=pd.DataFrame(data=tmpd)
    print(tmpdf)

    fields = []
    labels = []

    for col in tmpdf:
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
            if col == 'pc':
                continue
            labels.append(col)
            print(col, col)

    left=len(tmpdf) * [0]

    for idx, name in enumerate(fields):
        plt.barh(tmpdf['epoc'], tmpdf[name], left=left, color=colors[idx])
        left=left+tmpdf[name]

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

    plt.savefig('praves'+ alias +'.png')

process()

