import sys
g = []
c = []
DEBUG = True
fscore = dict()
# y, x, (E)lf/(G)oblin, hp

#load the grid into memory
with open("test.txt") as f:
    for row in f:
        r = []
        for cell in row:
            r.append(cell)
        g.append(row)

#extract elves and goblins
for y in range(len(g)):
    for x in range(len(g[y])):
        if g[y][x] == 'E':
            c.append([y,x,'E', 200])
            g[y] = g[y][:x] + '.' + g[y][x+1:]
        elif g[y][x] == 'G':
            c.append([y,x,'G', 200])
            g[y] = g[y][:x] + '.' + g[y][x+1:]

#print the initial grid
if DEBUG:
    for y in range(len(g)):
        l = ""
        for x in range(len(g[y])):
            ischar = False
            for thing in c:
                if thing[0] == y and thing[1] == x:
                    l += thing[2]
                    ischar = True
            if not ischar:
                l += g[y][x]
        print(l)

#returns item in heap with lowest fscore
def getmin(heap):
    global fscore
    low = heap.pop()
    heap.add(low)
    for item in heap:
        if fscore.get(item, 1000) < fscore.get(low, 1000): low = item
    return low

#returns manhattan distance from a to b
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#derives the optimal path to the target node
def rebuildpath(camefrom, target):
    path = [target]
    while target in camefrom.keys():
        target = camefrom[target]
        path.append(target)
    path.reverse()
    return path

#main astar algorithm
def astar(a, b):
    global fscore
    oset = set()
    cset = set()
    camefrom = dict()
    gscore = dict()

    start = (a[0], a[1])
    dest = (b[0], b[1])

    if start[0] == dest[0] and start[1] == dest[1]:
        return [dest]
    if g[start[0]][start[1]] != '.':
        return None
    
    oset.add(start)
    gscore[start] = 0
    fscore[start] = h(start, dest)

    while len(oset) > 0:
        current = getmin(oset)
        
        if current == dest:
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
                    if n[0] == thing[0] and n[1] == thing[1]:
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

#determines the closest enemy for a unit, as well as the correct square to move to
def getpath(thing):
    option = None
    lowest = 1000
    for other in c:
        if other is not thing and thing[2] != other[2]:
            a = astar(thing, other)
            if a is None: continue
            if len(a) < lowest:
                option = other.copy()
                lowest = len(a)

    print(f"{thing} moving towards {option}")

    if option is None:
        return None

    optw = [thing[0]-1, thing[1], thing[2], thing[3]]
    opta = [thing[0], thing[1]-1, thing[2], thing[3]]
    optd = [thing[0], thing[1]+1, thing[2], thing[3]]
    opts = [thing[0]+1, thing[1], thing[2], thing[3]]

    resw = astar(optw, option)
    resa = astar(opta, option)
    resd = astar(optd, option)
    ress = astar(opts, option)
    
    for thing in c:
        if thing[0] == optw[0] and thing[1] == optw[1]:
            resw = None                  
        if thing[0] == opta[0] and thing[1] == opta[1]:
            resa = None                  
        if thing[0] == optd[0] and thing[1] == optd[1]:
            resd = None                  
        if thing[0] == opts[0] and thing[1] == opts[1]:
            ress = None                  

    if resw is None and resa is None and resd is None and ress is None:
        return None
    
    best = min(len(x) for x in [resw, resa, resd, ress] if x is not None)

    if resw is not None and len(resw) == best:
        return resw
    elif resa is not None and len(resa) == best:
        return resa
    elif resd is not None and len(resd) == best:
        return resd
    elif ress is not None: 
        return ress
    else: return None

i = 0
#while True:
for i in range(10):
    c.sort()
    for thing in c:

        if sum(1 for thing in c if thing[2] == 'E') == 0 or sum(1 for thing in c if thing[2] == 'G') == 0:
            print(i*sum(z[3] for z in c))
            sys.exit(0)
        
        path = getpath(thing)

        if path is not None and len(path) > 1:
            print(thing, path)
            thing[0] = path[0][0]
            thing[1] = path[0][1]
            print(f"moving {thing}")
        if path is not None and len(path) == 1:
            #TODO: ATTACK
            print("ATTACK!", thing)

        for other in c:
            if thing[0] == other[0] and thing[1] == other[1] and thing is not other:
                print("ERROR")
                print(c)
                sys.exit(1)

    if DEBUG:
        print("  0123456")
        for y in range(len(g)):
            l = f"{y}|"
            for x in range(len(g[y])):
                ischar = False
                for thing in c:
                    if thing[0] == y and thing[1] == x:
                        l += thing[2]
                        ischar = True
                if not ischar:
                    l += g[y][x]
            print(l)
        print("========================")
