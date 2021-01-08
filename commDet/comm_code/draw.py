import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sys
from sklearn.cluster import AffinityPropagation

g = nx.read_edgelist('ado_top_5k', nodetype=str, data=(('weight',float),), create_using=nx.Graph())

nodes=list(g.nodes)
node_colors=[np.random.random(3) for i in range(len(nodes))]

clusfile=sys.argv[1]

for line in open(clusfile, 'r').readlines():
	arr = line.rstrip('\n').split()
	if arr[1]!='0':
		node_colors[nodes.index(arr[0])] = node_colors[nodes.index(arr[1])]
	else:
		node_colors[nodes.index(arr[0])] = [0,0,0]

nx.drawing.nx_pylab.draw_networkx(g, node_size=10, with_labels=False, node_color=node_colors)
# A = nx.to_numpy_array(g)
# np.fill_diagonal(A, 1)
# ap = AffinityPropagation(affinity='precomputed', random_state=None).fit(A)
# print(ap.labels_)
plt.show()