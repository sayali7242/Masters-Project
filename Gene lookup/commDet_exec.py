import sys
import os


for file in os.listdir('commDet_ssID/'):
	os.system('python3.8 lookup.py ' + 'commDet_ssID/' + file + ' > commDet_lookups/'+file)

