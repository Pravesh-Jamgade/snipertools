from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
from sklearn.cluster import KMeans

from utility import *
from showcase import *


''' cluster across data and find their frequency '''
def pc_frequency():
	path=sys.argv[1]
	df = read_csv(path)
	df.head()

	savePath1=path+'.pc_frequency'
	savePath2=path+'.count_frequency'
	cspath=path+'.cs.png'
	dfpath=path+'.df.png'
	cols = ['cycle','pc','addr','where']
	df=apply_colnames(df, cols)
	df=filter_positive_rows_by_col(df,cols[1])
	
	pc_based =get_unique_and_its_freq_of_col(df, cols[1])
	pc_based_df = pd.DataFrame(pc_based).reset_index()#pc_basedies to dataframe

	# pc based grouping and counting
	pc_based_df.columns = ['pc','count']
	cs = pc_based_df.sample(n=100, random_state = 1)
	to_csv_without_index(pc_based_df, savePath1)
	pc_fre(cs, cspath)
	
	# bins of count
	count_based = get_unique_and_its_freq_of_col(pc_based_df, 'count')
	count_based_df = pd.DataFrame(count_based).reset_index()
	count_based_df.columns = ['bin','count']
	to_csv_without_index(count_based_df, savePath2)
	bin_count_fre(count_based_df, dfpath)

''' cluster across data and find delta between their addresses '''
def cluster_by_pc():
	path=sys.argv[1]
	df = read_csv(path)
	savePath=path+'.delta_cluster_by_pc'
	cols = ['pc', 'addr']
	df=apply_colnames(df, cols)
	df=filter_positive_rows_by_col(df,cols[1])
	gdf=group_by_across_data(df, cols[0])
	df['diff'] = gdf.addr.diff()
	to_csv_without_index(df, savePath)

''' cluster consecutive data and find delta between their addresses '''
def consecutive_cluster_by_pc():
	path=sys.argv[1]
	df = read_csv(path)
	savePath=path+'.delta_cluster_by_consecutive_pc'
	cols = ['pc', 'addr']
	df=apply_colnames(df, cols)
	df=filter_positive_rows_by_col(df,cols[1])
	gdf=group_by_consecutive_same(df, cols[0])
	df['diff'] = gdf.addr.diff()
	to_csv_without_index(df, savePath)

def k_cluster():
	path=sys.argv[1]
	df = read_csv(path)
	df.head()
	df=df.sort_values('count')

	kmeans = KMeans(n_clusters=2, random_state=0)
	df['cluster'] = kmeans.fit_predict(df[['bin', 'count']])
	# get centroids
	centroids = kmeans.cluster_centers_
	cen_x = [i[0] for i in centroids] 
	cen_y = [i[1] for i in centroids]
	df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1]})
	df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1]})
	# define and map colors
	colors = ['#DF2020', '#81DF20', '#2095DF']
	df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})
	plt.scatter(df['bin'], df['count'], c=df['c'], alpha = 0.6, s=10)
	plt.show()

	to_csv_without_index(df, path+".cluster.log")

	# total accesses by each bin
	df['access']=df['count'] * df['bin']
	df=df.groupby('cluster').sum()
	df=df.drop(columns=['bin','cen_x','cen_y'])
	# sum of cluster pc, accesses
	print(df)

pc_frequency()
# cluster_by_pc()
# consecutive_cluster_by_pc()
# k_cluster()