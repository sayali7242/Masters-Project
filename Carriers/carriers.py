import numpy as np
import pandas as pd
import time
import sys
from bitarray import bitarray

ctrl_df = pd.read_csv('binarized_ado_ctrl', header=None, dtype=str)
case_df = pd.read_csv('binarized_ado_case', header=None, dtype=str)

#print(str(ctrl_df[0]))

ctrl_df.columns=['bitarray']
x=np.arange(0,len(ctrl_df.iloc[0][0])/2, dtype=int)

k=0
for i in x:
	ctrl_df[i] = ctrl_df['bitarray'].str[k:k+2]
	k+=2

ctrl_df.drop('bitarray', inplace=True, axis=1)
ctrl_df=ctrl_df.T


case_df.columns=['bitarray']
x=np.arange(0,len(case_df.iloc[0][0])/2, dtype=int)

k=0
for i in x:
	case_df[i] = case_df['bitarray'].str[k:k+2]
	k+=2

case_df.drop('bitarray', inplace=True, axis=1)
case_df=case_df.T

def match(C, AB):
	A=bitarray(''.join([a[0] for a in AB]))
	B=bitarray(''.join([a[1] for a in AB]))
	#print(A,B,C)
	#print((~C & ~A) | (C & B) | (A & ~B))
	return ((~C & ~A) | (C & B) | (A & ~B)).all()==True

#print(match(bitarray('0101'), [bitarray('00'), bitarray('01'), bitarray('11'), bitarray('11')]))

carriers_case=[]
case_count=[]
cluster_num=[] 
with open(sys.argv[1]) as cluster_file:
	for num, line in enumerate(cluster_file, 1):
		carriers_case_temp=[]
		case_count_temp=0
		nodes=line.rstrip('\n').split(',')
		if len(nodes)==1:
			continue
		snps_indices=[]
		alleles=[]
		for node in nodes:
			snps_indices+=[int(node.split('_')[0]), ]
			alleles+=[int(node.split('_')[1]), ]
		flag=0
		for index, row in case_df.iterrows():
			AB = (row[snps_indices]).to_list()
			if match(bitarray(alleles), AB) == True:
				if flag==0:
					cluster_num.append(num)
					flag=1
				carriers_case_temp+=[index,]
				case_count_temp+=1
		carriers_case+=[carriers_case_temp, ]
		case_count+=[case_count_temp,]

carriers_ctrl=[]
ctrl_count=[]
for line in open(sys.argv[1], 'r').readlines():
	carriers_ctrl_temp=[]
	ctrl_count_temp=0
	nodes=line.rstrip('\n').split(',')
	if len(nodes)==1:
		continue
	snps_indices=[]
	alleles=[]
	for node in nodes:
		snps_indices+=[int(node.split('_')[0]), ]
		alleles+=[int(node.split('_')[1]), ]

	for index, row in ctrl_df.iterrows():
		AB = (row[snps_indices]).to_list()
		if match(bitarray(alleles), AB) == True:
			carriers_ctrl_temp+=[index,]
			ctrl_count_temp+=1
	carriers_ctrl+=[carriers_ctrl_temp, ]
	ctrl_count+=[ctrl_count_temp,]



print('Case Count:\n', case_count)
print('\nControl Count:\n', ctrl_count)
print('\nCluster Number:\n', cluster_num)

p = np.array(case_count)/case_df.shape[0]
q = np.array(ctrl_count)/ctrl_df.shape[0]

odds_ratio = (p*(1-q))/(q*(1-p))
print('\nOdds Ratio:\n')
for oR in odds_ratio:
	print(oR)
