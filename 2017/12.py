import sys
import networkx as nx
nodes = set()
edges = []
with open(sys.argv[1], "r") as f:
    for line in f:
        raw = line.rstrip().split(' ')
        current = int(raw.pop(0))
        raw.pop(0) # <->
        nodes.add(current)
        while len(raw):
            edges.append((current, int(raw.pop(0).replace(',', ''))))
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
print(len(nx.node_connected_component(G, 0)))
print(sum([1 for component in nx.connected_components(G)]))
