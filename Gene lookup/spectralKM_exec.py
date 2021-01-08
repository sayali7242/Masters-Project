import sys
import os


for file in os.listdir('spectralKM_ssID/'):
	os.system('python3.8 lookup.py ' + 'spectralKM_ssID/' + file + ' > spectralKM_lookups/'+file)

