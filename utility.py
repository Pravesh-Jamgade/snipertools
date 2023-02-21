from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import statistics
import sys
import os

def read_csv(filePath):
	df = pd.read_csv(filePath)
	df.head()
	return df

def read_csv_add_sep(filePath, sep):
	df = pd.read_csv(filePath, sep)
	df.head()
	return df

def to_int(df, col):
	df[col]=df[col].apply(int)
	return df

def to_hex(df, col):
	df[col]=df[col].apply(hex)
	return df

def apply_colnames(df, names):
	df.columns = names
	return df

def to_csv(df, outputFileName):
	df.to_csv(outputFileName)

def to_csv_without_index(df, outputFileName):
	df.to_csv(outputFileName, index=False)

def to_csv_without_header(df, outputFileName):
	df.to_csv(outputFileName, header=False)

def to_csv_with_sep(df, outputFileName, separator=","):
	df.to_csv(outputFileName, sep=separator)

def filter_positive_rows_by_col(df, col):
	df = df[df[col] > 0]
	return df

def get_unique_list_of_col(df, col):
	return df[col].unique()

# return pd series
def get_unique_and_its_freq_of_col(df, col):
	tdf= df[col].value_counts()
	return tdf

def group_by_consecutive_same(df, col):
	tdf=df.groupby((df[col].shift()!=df[col]).cumsum())
	return tdf

def group_by_across_data(df, col):
	tdf=df.groupby(df[col])
	return tdf

def groupby_to_csv(group, path):
	group.sum().to_csv(path)

def col_to_list(df, col):
	return df[col].tolist()