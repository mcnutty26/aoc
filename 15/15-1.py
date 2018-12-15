import sys
g = []
c = []
DEBUG = True
fscore = dict()
# y, x, (E)lf/(G)oblin, hp

with open("test.txt") as f:
    for row in f:
        r = []
        for cell in row:
            r.append(cell)
        g.append(row)

for y in range(len(g)):
    for x in range(len(g[y])):
        if g[y][x] == 'E':
            c.append([y,x,'E', 200])
            g[y] = g[y][:x] + '.' + g[y][x+1:]
        elif g[y][x] == 'G':
            c.append([y,x,'G', 200])
            g[y] = g[y][:x] + '.' + g[y][x+1:]

if DEBUG:
    for y in g:
        line = ""
        for x in y:
            line += x
        print(line)
    print(c)

def getmin(heap):
    global fscore
    low = heap.pop()
    heap.add(low)
    for item in heap:
        if fscore.get(item, 1000) < fscore.get(low, 1000): low = item
    return low

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def rebuildpath(camefrom, current):
    path = [current]
    while current in camefrom.keys():
        print(current)
        current = camefrom[current]
        path.append(current)
    path.reverse()
    return path

def astar(a, b):
    global fscore
    oset = set()
    cset = set()
    camefrom = dict()
    gscore = dict()

    start = (a[0], a[1])
    dest = (b[0], b[1])

    oset.add(start)
    gscore[start] = 0
    fscore[start] = h(start, dest)

    while len(oset) > 0:
        current = getmin(oset)
            
        if current == dest:
            #TODO: CONSIDER MOVE TIES (reading order, run again without the tile we were going to move to - is it the same distance?)
            return rebuildpath(camefrom, current)

        oset.remove(current)
        cset.add(current)

        neighbours_ = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]
        neighbours = []

        for n in neighbours_:
            if n == dest:
                neighbours.append(n)
            elif n[0] >= len(g) or n[1] >= len(g[n[0]]):
                continue
            elif g[n[0]][n[1]] != '.':
                continue
            else: 
                dup = False
                for thing in c:
                    if n[0:2] == c[0:2]:
                        dup = True
                if not dup:
                    neighbours.append(n)

        for n in neighbours:
            if n in cset:
                continue

            if n not in oset: oset.add(n)
            elif gscore[current] + 1 >= gscore.get(n, 1000):
                continue

            camefrom[n] = current
            gscore[n] = gscore[current] + 1
            fscore[n] = gscore[n] + h(n, dest)

def getpath(thing):
    #TODO: CONSIDER TIES (reading order)
    return max(astar(thing, target) for target in c if target[2] != thing[2])

i = 0
while not true:
    c.sort()
    for thing in c:
        #CHECK END CONDITION
        if sum(1 for thing in c if thing[2] == 'E') == 0 or sum(1 for thing in c if thing[2] == 'G') == 0:
            print(i*sum(z[3] for z in c))
            sys.exit(0)
        
        path = getpath(thing)
        if len(path) > 2:
            thing[0:2] = path[1]
        if len(path) <= 3:
            #TODO: ATTACK
