import sys
import os


for file in os.listdir('bfs_ssID/'):
	os.system('python3.8 lookup.py ' + 'bfs_ssID/' + file + ' > bfs_lookup/'+file)

