from pathfinding22 import astar
t = (13,726)
d = 3066
g = []
for x in range(t[0]+100):
    g.append([])
    for y in range(t[1]+100):
        i = 0
        if x == 0 and y == 0: i = 0
        elif x == t[0] and y == t[1]: i = 0
        elif y == 0: i = x*16807
        elif x == 0: i = y*48271
        else: i = g[x-1][y][0] * g[x][y-1][0]
        i = (i+d)%20183
        g[x].append(((i+d)%20183, ((i+d)%20183)%3))
print(astar((0,0,1), (t[0], t[1], 1), g)[0])
