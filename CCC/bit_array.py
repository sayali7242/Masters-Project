import pandas as pd
import numpy as np
import itertools
import sys
import networkx as nx

#This code is used to convert the original data to bit-array representation.  

np.set_printoptions(threshold=sys.maxsize)

df=pd.read_csv('ado_ctrl_5000.csv', sep='\t')

tally = {}
#print(df)

# list_allel = []
# for (idx, row) in df.iterrows(): 
# 	list_list(allel.append({row[3] : 0,) row[4] : 1})


df = df.drop(['snpID', 'dbSNP_ss', 'vendor_SNP_ID', 'ALLELE1_fwd'], axis=1)

#The following code is used to convert the orginial data into pairs of 0 and 1. 
#Un-comment line 31 and comment line 28 and 29 to get the positions of Missing value in the converted data. 

for i in range(len(df)):
	x=np.array(list(''.join(df.iloc[i][1:])), dtype=str)
	y=((x==df.iloc[i][0])+0)
	print(''.join([str(k) for k in y]))

	#print(np.where(x=='N'))

