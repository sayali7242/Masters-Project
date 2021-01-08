from collections import deque
import networkx as nx
import sys 

G = nx.read_edgelist('gru_top_5k', nodetype=str, data=(('weight',float),), create_using=nx.Graph())

#components = [c for c in sorted(nx.connected_components(G), key=len, reverse=True)]

for c in sorted(nx.connected_components(G), key=len, reverse=True):
	print(c)