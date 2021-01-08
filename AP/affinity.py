#This file contains the code that finds the clusters in our graph using affinity propagation algorithm. 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from mpl_toolkits import mplot3d
import sys

n=10000

ids={}
node_dict={}

snp=0
index=0

for i in range(5000):
	node_dict[index]=str(snp)+'_0'
	ids[str(snp)+'_0'] = index
	node_dict[index+1]=str(snp)+'_1'
	ids[str(snp)+'_1'] = index+1
	index+=2
	snp+=1

adj_list=np.zeros(shape=(10000,10000))

for line in open(sys.argv[1]).readlines():
	x=line.split(' ')
	adj_list[ids[x[0]]][ids[x[1]]]=float(x[2])
	adj_list[ids[x[1]]][ids[x[0]]]=float(x[2])

np.fill_diagonal(adj_list, 1)

damp = float(sys.argv[2])

nodes=np.array(list(node_dict.values()))

ap = AffinityPropagation(affinity='precomputed', verbose=True, damping = damp, max_iter=600, random_state=0).fit(adj_list)

for i in range(max(ap.labels_)+1):
	print(nodes[ap.labels_==i])
