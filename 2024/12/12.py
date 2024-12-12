import sys
from itertools import combinations

grid = {}
adj = [(1,0), (0,1), (-1,0), (0,-1)]
totals = [0, 0]

with open(sys.argv[1]) as puzzle:
    y = 0
    for line in puzzle:
        x = 0
        for char in line.rstrip():
            grid[(x, y)] = char
            x += 1
        y += 1

def flood(point, filled, perim, edges):
    filled.add(point)
    for a in range(len(adj)):
        x = (point[0]+adj[a][0], point[1]+adj[a][1])
        if x not in grid or grid[x] != grid[point]:
            perim += 1
            edges.add((point, a))
        elif x not in filled:
            filled, perim, edges = flood(x, filled, perim, edges)
    return filled, perim, edges

done = set()
blocks = []
for k in grid.keys():
    if k not in done:
        x, y, z = flood(k, set(), 0, set())
        done = done.union(x)
        blocks.append((x, y, z))
        totals[0] += len(x) * y

for i in range(len(blocks)):
    merged = 0
    for x, y in combinations(blocks[i][2], 2):
        if y[0] in [(x[0][0]+a[0], x[0][1]+a[1]) for a in adj] and x[1] == y[1]:
            merged += 1
    totals[1] += len(blocks[i][0]) * (blocks[i][1] - merged)

print(totals)
