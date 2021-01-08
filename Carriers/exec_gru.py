import sys
import os


for file in os.listdir('../Spectral/Spectral_DS/gru1/'):
	os.system('python3.8 carriers_gru.py ' + '../Spectral/Spectral_DS/gru1/' + file + ' > gru_spectral_DS_OR/'+file)

