f1=open('Spectral_KM/ado_spectral_KM_top_ORs', 'r')
f2=open('Spectral_KM/gru_spectral_KM_top_ORs', 'r')
l1=list(f1.readlines())
l2=list(f2.readlines())

ado_sets={}
gru_sets={}
ado_hyperparam=0
gru_hyperparam=0
ado_set_ORs={}
gru_set_ORs={}

for l in l1:
	if l.startswith('('):
		x=l.split('(')[2][:-3]
		if x[0]!='n':
			x=x.split(', ')
			oR=x[0]
			x=set(x[1:])
			if ado_hyperparam in ado_sets:
				ado_sets[ado_hyperparam]+=[x, ]
				ado_set_ORs[ado_hyperparam]+=[oR, ]
			else:
				ado_sets[ado_hyperparam]=[x]
				ado_set_ORs[ado_hyperparam]=[oR]
	elif l.startswith('ccc'):
		ado_hyperparam=float(l.split('_')[-1].rstrip('\n'))
	
for l in l2:
	if l.startswith('('):
		x=l.split('(')[2][:-3]
		if x[0]!='n':
			x=x.split(', ')
			oR=x[0]
			x=set(x[1:])
			if gru_hyperparam in gru_sets:
				gru_sets[gru_hyperparam]+=[x, ]
				gru_set_ORs[gru_hyperparam]+=[oR, ]
			else:
				gru_sets[gru_hyperparam]=[x]
				gru_set_ORs[gru_hyperparam]=[oR]
	elif l.startswith('ccc'):
		gru_hyperparam=float(l.split('_')[-1].rstrip('\n'))

for k1 in gru_sets.keys():
	for v1, o1 in zip(gru_sets[k1], gru_set_ORs[k1]):
		for k2 in ado_sets.keys():
			for v2, o2 in zip(ado_sets[k2], ado_set_ORs[k2]):
				#if len(v1.intersection(v2))!=0:
				if v1==v2:
					#print(k1, v1, o1, k2, v2, o2, v1.intersection(v2), sep='\t')
					print(k1, o1, k2, o2, v1, sep='\t')
