import sys
import os


for file in os.listdir('BFS_ssID/'):
	os.system('python3.8 lookup.py ' + 'BFS_ssID/' + file + ' > BFS_lookups/'+file)

