import pandas as pd
import numpy as np
import itertools
import sys
import time
import networkx as nx
import threading

df = pd.read_csv('combined_'+sys.argv[1]+'_case_ctrl', header=None)

nanlist = list(open('NaNs_'+sys.argv[1]+'_combined', 'r').readlines())

q=1.5

f0=open(sys.argv[1]+'_g0', 'a')
f1=open(sys.argv[1]+'_g1', 'a')
f2=open(sys.argv[1]+'_g2', 'a')
f3=open(sys.argv[1]+'_g3', 'a')
f4=open(sys.argv[1]+'_g4', 'a')

file_dict={
	0: f0,
	1: f1,
	2: f2,
	3: f3,
	4: f4
}

#print(np.fromstring(nanlist[0][1:-2], sep=',', dtype=int))

def scoreouts(first, start, end, tnum):
	s1 = np.array(list(df.iloc[first][0]), dtype=int)
	nan1 = set(np.fromstring(nanlist[first][1:-2], sep=',', dtype=int))
	for j in range(start, end):
		ij_matrix=np.array([[0,0],[0,0]])
		s2 = np.array(list(df.iloc[j][0]), dtype=int)
		nan2 = np.fromstring(nanlist[j][1:-2], sep=',', dtype=int)
		nans_union = sorted( nan1.union(set(nan2)) )
		num_nans=int(len(nans_union)/2)

		s1_temp = np.delete(s1, nans_union)
		s2_temp = np.delete(s2, nans_union)

		s1_1 = s1_temp[::2]
		not_s1_1 = (1+s1_1)%2
		s1_2 = s1_temp[1::2]
		not_s1_2 = (1+s1_2)%2

		s2_1 = s2_temp[::2]
		not_s2_1 = (1+s2_1)%2
		s2_2 = s2_temp[1::2]
		not_s2_2 = (1+s2_2)%2

		ij_matrix[1][1] += np.dot(s1_1, s2_1)
		ij_matrix[1][1] += np.dot(s1_1, s2_2)
		ij_matrix[1][1] += np.dot(s1_2, s2_1)
		ij_matrix[1][1] += np.dot(s1_2, s2_2)

		ij_matrix[0][1] += np.dot(not_s1_1, s2_1)
		ij_matrix[0][1] += np.dot(not_s1_1, s2_2)
		ij_matrix[0][1] += np.dot(not_s1_2, s2_1)
		ij_matrix[0][1] += np.dot(not_s1_2, s2_2)

		ij_matrix[1][0] += np.dot(s1_1, not_s2_1)
		ij_matrix[1][0] += np.dot(s1_1, not_s2_2)
		ij_matrix[1][0] += np.dot(s1_2, not_s2_1)
		ij_matrix[1][0] += np.dot(s1_2, not_s2_2)

		ij_matrix[0][0] += np.dot(not_s1_1, not_s2_1)
		ij_matrix[0][0] += np.dot(not_s1_1, not_s2_2)
		ij_matrix[0][0] += np.dot(not_s1_2, not_s2_1)
		ij_matrix[0][0] += np.dot(not_s1_2, not_s2_2)

		f_1_0 = 1- ((ij_matrix[0][0]+ij_matrix[0][1])/(2*q*((len(s1))-(num_nans*2))))
		f_1_1 = 1- ((ij_matrix[1][0]+ij_matrix[1][1])/(2*q*((len(s1))-(num_nans*2))))
		f_2_0 = 1- ((ij_matrix[0][0]+ij_matrix[1][0])/(2*q*((len(s1))-(num_nans*2))))
		f_2_1 = 1- ((ij_matrix[0][1]+ij_matrix[1][1])/(2*q*((len(s1))-(num_nans*2))))


		ij_matrix = ij_matrix/((len(s1)/2)-num_nans)
		ij_matrix = ij_matrix/4

		ij_matrix[0][0] = ij_matrix[0][0]*f_1_0*f_2_0
		ij_matrix[0][1] = ij_matrix[0][1]*f_1_0*f_2_1
		ij_matrix[1][0] = ij_matrix[1][0]*f_1_1*f_2_0
		ij_matrix[1][1] = ij_matrix[1][1]*f_1_1*f_2_1

		CCC = 4.5*ij_matrix

		file_dict[tnum].write(str(i) +  '_0 ' + str(j) + '_0 ' + str(CCC[0][0]) + '\n')
		file_dict[tnum].write(str(i) +  '_1 ' + str(j) + '_0 ' + str(CCC[1][0]) + '\n')
		file_dict[tnum].write(str(i) +  '_0 ' + str(j) + '_1 ' + str(CCC[0][1]) + '\n')
		file_dict[tnum].write(str(i) +  '_1 ' + str(j) + '_1 ' + str(CCC[1][1]) + '\n')

	print('Thread : ' + str(first)+'_'+str(start)+'_'+str(end)+'_'+str(tnum))


popsize=len(df)
for i in range(popsize-1):
	threadlist = []
	n=popsize-i-1
	thr_indices=[i+1, 1+i+int(n/4), 1+i+int(n/2), 1+i+int((3*n)/4), popsize]
	if thr_indices[0]!=thr_indices[1]:
		threadlist.append(threading.Thread(target=scoreouts, args=(i, thr_indices[0],  thr_indices[1], 0)))
		threadlist.append(threading.Thread(target=scoreouts, args=(i, thr_indices[1],  thr_indices[2], 1)))
		threadlist.append(threading.Thread(target=scoreouts, args=(i, thr_indices[2],  thr_indices[3], 2)))
		threadlist.append(threading.Thread(target=scoreouts, args=(i, thr_indices[3],  thr_indices[4], 3)))
		for t in threadlist:
			t.start()
		for t in threadlist:
			t.join()

	else:
		scoreouts(i, i+1, popsize, 4)


f0.close()
f1.close()
f2.close()
f3.close()
f4.close()