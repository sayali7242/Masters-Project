import sys
import os


for file in os.listdir('ado_spectral_DS_OR/'):
	text_file = open("ado_spectral_DS_top_ORs", "a")
	n = text_file.write('\n'+file+'\n')
	text_file.close()
	os.system('python3.8 analysis.py ado_spectral_DS_OR/' + file + ' ../Spectral/Spectral_DS/ado/' + file + ' >> ado_spectral_DS_top_ORs')
