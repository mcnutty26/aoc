g = []
with open("18.txt") as f:
    for line in f:
        l = []
        for char in line.strip('\n'): l.append(char)
        g.append(l)
g_ = []
for x in g: g_.append(x.copy())
def get_neighbours(x, y):
    n = []
    if x-1 >= 0:
        n.append(g[x-1][y])
        if y-1 >= 0: n.append(g[x-1][y-1])
        if y+1 < ymax: n.append(g[x-1][y+1])
    if x+1 < xmax:
        n.append(g[x+1][y])
        if y-1 >= 0: n.append(g[x+1][y-1])
        if y+1 < ymax: n.append(g[x+1][y+1])
    if y-1 >= 0: n.append(g[x][y-1])
    if y+1 < ymax: n.append(g[x][y+1])
    return n
xmax = len(g)
ymax = len(g[0])
for i in range(10):
    for x in range(len(g)):
        for y in range(len(g[x])):
            trees = 0
            lumber = 0
            for n in get_neighbours(x,y):
                if n == '|': trees += 1
                elif n == '#': lumber += 1
            if g[x][y] == '.':
                if trees >= 3:
                    g_[x][y] = '|'
            elif g[x][y] == '|':
                if lumber >= 3:
                    g_[x][y] = '#'
            elif g[x][y] == '#':
                if trees < 1 or lumber < 1:
                    g_[x][y] = '.'
    g = []
    for line in g_: g.append(line.copy())
trees = 0
lumber = 0
for x in range(len(g)):
    for y in range(len(g[x])):
        if g[x][y] == '|': trees += 1
        elif g[x][y] == '#': lumber += 1
print(trees*lumber)
