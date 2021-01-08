import sys
import os


for file in os.listdir('MCL_ssID/'):
	os.system('python3.8 lookup.py ' + 'MCL_ssID/' + file + ' > MCL_lookups/'+file)

