import pandas as pd 
import sys
import os
import numpy as np
from math import isnan

f=open(sys.argv[1])
lines=list(f.readlines())
rows_list = []
for i in range(11, len(lines)): 
	rows_list.append(lines[i].rstrip())
clusnum=np.fromstring(lines[7].lstrip().rstrip()[1:-1], dtype=int, sep=',')

clusters_file = open(sys.argv[2])
c_lines = list(clusters_file.readlines())
clusters = [c_lines[i-1].rstrip() for i in clusnum]

or_dict={i:(j,k) for i,j,k in zip(clusnum, rows_list, clusters)}
sorted_ORs = sorted(or_dict.items(), key=lambda x: x[1][0], reverse=True)

c=0

for i in sorted_ORs:
	if i[1][0]!='nan' and i[1][0]!='inf':
		print(i)
		c+=1
	if c==15:
		break
