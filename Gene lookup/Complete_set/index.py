import pandas as pd

df = pd.read_csv('ado_case_5000.csv', sep='\t')

c=1
for line in open('spectralKM_complete', 'r').readlines():
	f=open('spectralKM_ssID/spectralKM_ssIDs_'+str(c), 'w')
	nodes=line.rstrip('\n').split(', ')
	snps_indices=[]
	for node in nodes:
		snps_indices+=[int(node.split('_')[0]), ]
	asd=[x+162000 for x in snps_indices]
	sdf=[df["dbSNP_ss"].iloc[x] for x in snps_indices]
	for i,j in zip(asd, sdf):
		f.write(str(i) + '\t' + str(j) +'\n')
	f.close()
	c+=1