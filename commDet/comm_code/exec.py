import os
import sys

init_params=[0.5,0.6,0.7,0.8,0.9]

for file in os.listdir('Ado_top/'):
	for i in init_params:
		os.system('python3 commDet.py Ado_top/' + file + ' ' + str(i))

for file in os.listdir('Gru_top/'):
	for i in init_params:
		os.system('python3 commDet.py Gru_top/' + file + ' ' + str(i))

for file in os.listdir('cluster_outputs/'):
	os.system('python3 format_clus.py cluster_outputs/' + file + ' > temp')
	os.system('rm cluster_outputs/' + file)
	os.system('mv temp cluster_outputs/' + file)