import sys
import os


for file in os.listdir('../Spectral/Spectral_DS/ado1/'):
	os.system('python3.8 carriers.py ' + '../Spectral/Spectral_DS/ado1/' + file + ' > ado_spectral_DS_OR/'+file)

