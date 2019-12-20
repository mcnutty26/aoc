from pathfinding import astar
import heapq

maze = []
portals = dict()
adj = dict()

# Same order as for neighbours, makes it easier to track which direction we're going in
RELS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Dump the maze characters into a grid (yx indexed!)
with open('input.txt', 'rt') as textfile:
    for line in textfile:
        maze.append([])
        for char in line:
            maze[-1].append(char)

# Helper function to get the squares adjacent to the given square
def neighbours(y, x):
    return [maze[y][x+1], maze[y][x-1], maze[y+1][x], maze[y-1][x]]

# Search for portals in the grid
for y in range(1, len(maze) - 1):
    for x in range(1, len(maze[0]) - 1):
        if maze[y][x] == '.':
            n = neighbours(y, x)
            for i in range(4):
                if n[i].isupper():
                    point = (y,x)
                    name = n[i]
                    for z in neighbours(y+RELS[i][0], x+RELS[i][1]):
                        if z.isupper():
                            name += z
                            name = '' + sorted(name)[0] + sorted(name)[1]
                            if name not in portals:
                                portals[name] = [point]
                            else:
                                portals[name].append(point)

# Create a lookup of portal-adjacent squares
for portal in portals:
    p = portals[portal]
    if len(p) == 2:
        adj[p[0]] = p[1]
        adj[p[1]] = p[0]

# Slight hack as A* is working on three dimensions, but the portals are only defined by two
start = (portals['AA'][0][0], portals['AA'][0][1], 0)
end = (portals['ZZ'][0][0], portals['ZZ'][0][1], 0)

# Part 1 (shenanigans = False)
print(len(astar(start, end, maze, adj, False)) -1)

# Part 2 (shenanigans = True)
print(len(astar(start, end, maze, adj, True)) -1)
