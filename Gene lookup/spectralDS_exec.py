import sys
import os


for file in os.listdir('spectralDS_ssID/'):
	os.system('python3.8 lookup.py ' + 'spectralDS_ssID/' + file + ' > spectralDS_lookups/'+file)

