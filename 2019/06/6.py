import networkx as nx
from networkx.algorithms import approximation
nodes = set()
edges = []

with open('input.txt', 'rt') as textfile:
    for line in textfile:
        nodes.add(line[0:3])
        nodes.add(line[-4:-1])
        edges.append((line[-4:-1], line[0:3]))

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

print(sum([len(nx.shortest_path(G, node, 'COM')) - 1 for node in nodes]))
print(len(nx.shortest_path(G, 'YOU', 'SAN')) - 3)
