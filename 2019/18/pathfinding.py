#heuristic function for A* (uses manhattan distance)
#is admissible, i.e. never overestimates the distance between a and b
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#returns the element in a list with the smallest A* fscore
def getmin(heap, fscore):
    low = heap.pop()
    heap.add(low)
    for item in heap:
        if fscore.get(item, 1000) < fscore.get(low, 1000): low = item
    return low

#given a destination, constructs the path to that point from the start point
#uses an A* adjaency list
def rebuildpath(camefrom, target, g, dest):
    doors = set()
    path = [target]
    while target in camefrom.keys():
        if g[target[0]][target[1]].islower() and g[target[0]][target[1]] != dest:
            doors.add(g[target[0]][target[1]])
        target = camefrom[target]
        if g[target[0]][target[1]].isupper():
            doors.add(g[target[0]][target[1]].lower())
        path.append(target)
    path.reverse()
    return (len(path)-1,doors)

#main A* algorithm
#at each iteration, A* chooses paths to expand that minimise f(n) = g(n) + h(n) for intrmediate point n
#where g(n) is the shortest constructed path to n and h(n) is the estimated distance from n to the destination
def astar(s, d, g, k):
    oset = set()
    cset = set()
    camefrom = dict()
    gscore = dict()
    fscore = dict()
    start = k[s]
    if type(d) is tuple:
        dest = d
    else:
        dest = k[d]

    #short circuit if given a stupid input
    if start[0] == dest[0] and start[1] == dest[1]:
        #(start point is the goal point)
        return [dest]
    if g[start[0]][start[1]] == '#':
        print("S")
        #(start point is a wall)
        return False
    if g[dest[0]][dest[1]] == '#':
        print("D")
        #(start point is a wall)
        return False
    
    #to begin with, the only open point for exploration is the starting point
    oset.add(start)
    gscore[start] = 0
    fscore[start] = h(start, dest)

    #continue while there are open points to expand
    while len(oset) > 0:
        current = getmin(oset, fscore)
        
        #we found the destination!
        if current == dest:
            return rebuildpath(camefrom, current, g, d)

        #mark the current point as explored
        oset.remove(current)
        cset.add(current)

        #generate possible neighbours of the current point
        neighbours_ = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]
        neighbours = []

        #add neighbours if they're not blocked
        for n in neighbours_:
            if n == dest:
                #(always add the destination)
                neighbours.append(n)
            elif n[0] >= len(g) or n[1] >= len(g[0]):
                #(neighbour is out of bounds)
                continue
            elif g[n[0]][n[1]] == '#':
                #(neighbour is a wall)
                continue
            else: 
                #(neighbour is empty space, so add it)
                neighbours.append(n)

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

    #(there is no valid path to the destination)
    return False
