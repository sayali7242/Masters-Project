l1 = list(open('AP_clusters', 'r').readlines())
l2 = list(open('MCL_clusters', 'r').readlines())
l3 = list(open('commDet_clusters', 'r').readlines())
l4 = list(open('BFS_clusters', 'r').readlines())
l5 = list(open('spectralDS_clusters', 'r').readlines())
l6 = list(open('spectralKM_clusters', 'r').readlines())

c1=set(frozenset(l.rstrip('\n').split(', ')) for l in l1)
c2=set(frozenset(l.rstrip('\n').split(', ')) for l in l2)
c3=set(frozenset(l.rstrip('\n').split(', ')) for l in l3)
c4=set(frozenset(l.rstrip('\n').split(', ')) for l in l4)
c5=set(frozenset(l.rstrip('\n').split(', ')) for l in l5)
c6=set(frozenset(l.rstrip('\n').split(', ')) for l in l6)

x=[c1,c2,c3,c4,c5,c6]
y=['c1','c2','c3','c4','c5','c6']

print('Intersection over all sets:\n')
for i in range(len(x)):
	for j in range(i+1, len(x)):
		if len(set.intersection(x[i],x[j]))>0:
			print(y[i], y[j])
			for inter in set.intersection(x[i], x[j]):
				print(inter)

c1=[set(l.rstrip('\n').split(', ')) for l in l1]
c2=[set(l.rstrip('\n').split(', ')) for l in l2]
c3=[set(l.rstrip('\n').split(', ')) for l in l3]
c4=[set(l.rstrip('\n').split(', ')) for l in l4]
c5=[set(l.rstrip('\n').split(', ')) for l in l5]
c6=[set(l.rstrip('\n').split(', ')) for l in l6]

a=[c1,c2,c3,c4,c5,c6]
b=['c1','c2','c3','c4','c5','c6']

print('\n\nIntersection over pair of sets')
for i in range(len(a)):
	for j in range(i+1, len(a)):
		print(b[i], b[j])
		for set1 in a[i]:
			for set2 in a[j]:
				if len(set.intersection(set1, set2))>2:
					print(set.intersection(set1, set2))