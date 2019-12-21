def outer(a: tuple, g: list) -> bool:
    if a[1] == 2 or a[1] == len(g[0]) - 4:
        return True
    if a[0] == 2 or a[0] == len(g) -3:
        return True
    return False

def h(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def getmin(heap: set, fscore: dict) -> tuple:
    low = heap.pop()
    heap.add(low)
    for item in heap:
        if fscore.get(item, 1000) < fscore.get(low, 1000): low = item
    return low

def rebuildpath(camefrom: dict, target: tuple) -> list:
    path = [target]
    while target in camefrom.keys():
        target = camefrom[target]
        path.append(target)
    path.reverse()
    return path

def astar(start: tuple, dest: tuple, g: list, adj: dict, shenanigans: bool) -> list:
    oset = set()
    cset = set()
    camefrom = dict()
    gscore = dict()
    fscore = dict()

    #short circuit if given a stupid input
    if start[0] == dest[0] and start[1] == dest[1] and start[2] == dest[2]:
        #(start point is the goal point)
        return [dest]
    if g[start[0]][start[1]] != '.':
        #(start point is a wall)
        return []
    
    #to begin with, the only open point for exploration is the starting point
    oset.add(start)
    gscore[start] = 0
    fscore[start] = h(start, dest)

    #continue while there are open points to expand
    while len(oset) > 0:
        current = getmin(oset, fscore)

        #we found the destination!
        if current == dest:
            return rebuildpath(camefrom, current)

        #mark the current point as explored
        oset.remove(current)
        cset.add(current)

        #generate possible neighbours of the current point
        neighbours_ = [(current[0] + 1, current[1], current[2]), (current[0] - 1, current[1], current[2]), (current[0], current[1] + 1, current[2]), (current[0], current[1] - 1, current[2])]
        neighbours = []

        #add neighbours if they're not blocked
        for n in neighbours_:
            if n == dest:
                #(always add the destination)
                neighbours.append(n)
            elif n[0] >= len(g) or n[1] >= len(g[n[0]]):
                #(neighbour is out of bounds)
                continue
            elif g[n[0]][n[1]] != '.':
                #(neighbour is a wall)
                continue
            else: 
                #(neighbour is empty space, so add it)
                neighbours.append(n)
            
        if (current[0], current[1]) in adj:
            #(we're on a portal, so add the other square)
            p = adj[(current[0], current[1])]
            
            if not shenanigans:
                neighbours.append((p[0], p[1], current[2]))
            else:
                if outer(current, g) and current[2] > 0:
                    #(outer portal and level > 0 => go down a level)
                    neighbours.append((p[0], p[1], current[2] - 1))
                elif not outer(current, g) and current[2] < len(adj):
                    neighbours.append((p[0], p[1], current[2] + 1))

        #add neighbours to exploration list if we haven't visited them before
        for n in neighbours:
            if n in cset:
                #(we already explored from this neighbour)
                continue

            #(explore this neighbour, as we haven't seen it before)
            if n not in oset: oset.add(n)

            #(we already found a better way to this neighbour)
            elif gscore[current] + 1 >= gscore.get(n, 1000):
                continue

            #(this is best route to this neighbour so far, so record it)
            camefrom[n] = current
            gscore[n] = gscore[current] + 1
            fscore[n] = gscore[n] + h(n, dest)
