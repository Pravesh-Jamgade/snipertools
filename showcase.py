from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os
from utility import *


def pc_fre(df, savePath):
	df.plot(x='pc', y='count', kind="bar",figsize=(30,15))
	plt.xticks(rotation=90)
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator())
	plt.grid(True, which='major', axis='y')
	plt.xlabel('pc')
	plt.ylabel('count')
	plt.legend()
	plt.savefig(savePath+'.png')
	plt.clf()

def bin_count_fre(df, savePath):
	df['count'] = np.log10(df['count'])
	df.plot(x='bin', y='count', kind="bar",figsize=(30,15))

	df=df.sort_values('bin')
	# keeping x values as labels instead of as range of x axis scale
	defaul_x_ticks = range(df.shape[0])
	plt.plot(defaul_x_ticks, df['count'])
	plt.xticks(defaul_x_ticks, df['bin'])

	plt.xticks(rotation=90)
	plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
	plt.grid(True, which='major', axis='y')
	plt.xlabel('bin')
	plt.ylabel('count (in log10)')
	plt.legend()
	plt.savefig(savePath+'.png')
	plt.clf()