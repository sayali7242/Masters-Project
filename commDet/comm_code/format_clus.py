import sys
f=open(sys.argv[1], 'r')

c_dict={}

for line in f.readlines():
	x=line.rstrip('\n').split('  ')
	if x[1] in c_dict:
		c_dict[x[1]] += [x[0], ]
	else:
		c_dict[x[1]] = [x[0] ]

del c_dict['0']

for k,v in c_dict.items():
	if len(v)>2:
		print(','.join(v))