import pandas as pd
import numpy as np
import itertools
import sys
import networkx as nx


np.set_printoptions(threshold=sys.maxsize)

df=pd.read_csv('ado_ctrl_5000.csv', sep='\t')

tally = {}
#print(df)

# list_allel = []
# for (idx, row) in df.iterrows(): 
# 	list_list(allel.append({row[3] : 0,) row[4] : 1})


df = df.drop(['snpID', 'dbSNP_ss', 'vendor_SNP_ID', 'ALLELE1_fwd'], axis=1)

for i in range(len(df)):
	x=np.array(list(''.join(df.iloc[i][1:])), dtype=str)
	#y=((x==df.iloc[i][0])+0)
	#print(''.join([str(k) for k in y]))

	print(np.where(x=='N'))

