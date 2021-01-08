import pandas as pd
import numpy as np
import itertools
import sys
import networkx as nx
from itertools import permutations

np.set_printoptions(threshold=sys.maxsize)
f = open('NaNs_gru_5_combined', 'a')

df=pd.read_csv('gru_case_ctrl_combined.csv', sep='\t')

df = df.drop(['snpID', 'dbSNP_ss', 'vendor_SNP_ID', 'ALLELE1_fwd'], axis=1)

for i in range(len(df)):
	x=np.array(list(''.join(df.iloc[i][1:])), dtype=str)
	x=np.random.permutation(x)
	nans=np.where(x=='N')[0]
	j=0
	while j < len(nans):
		if nans[j]%2==0:
			x[nans[j+1]]=x[nans[j]+1]
			x[nans[j]+1]='N'
			j+=2
		else:
			x[nans[j+1]]=x[nans[j]-1]
			x[nans[j]-1]='N'
			j+=2

	y=((x==df.iloc[i][0])+0)
	print(''.join([str(k) for k in y]))
	nans=np.where(x=='N')
	np.savetxt(f, nans, delimiter=",", fmt='%d', newline='\n')
	
	
