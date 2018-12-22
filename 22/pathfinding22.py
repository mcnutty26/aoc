#heuristic function for A* (uses manhattan distance)
#is admissible, i.e. never overestimates the distance between a and b
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#returns the element in a list with the smallest A* fscore
def getmin(heap, fscore):
    low = heap.pop()
    heap.add(low)
    for item in heap:
        if fscore.get(item, 10000) < fscore.get(low, 10000): low = item
    return low

#given a destination, constructs the path to that point from the start point
#uses an A* adjaency list
def rebuildpath(camefrom, target):
    path = [target]
    while target in camefrom.keys():
        target = camefrom[target]
        path.append(target)
    path.reverse()
    return path

#main A* algorithm
#at each iteration, A* chooses paths to expand that minimise f(n) = g(n) + h(n) for intrmediate point n
#where g(n) is the shortest constructed path to n and h(n) is the estimated distance from n to the destination
def astar(start, dest, g):
    oset = set()
    cset = set()
    camefrom = dict()
    gscore = dict()
    fscore = dict()

    rocky, wet, narrow = 0,1,2
    none, torch, gear = 0,1,2
    items = {none: [wet, narrow], torch: [rocky, narrow], gear: [rocky, wet]}
    regions = {rocky: [gear, torch], wet: [none, gear], narrow: [none, torch]}

    #to begin with, the only open point for exploration is the starting point
    oset.add(start)
    gscore[start] = 0
    fscore[start] = h(start, dest)

    #continue while there are open points to expand
    while len(oset) > 0:
        current = getmin(oset, fscore)
        
        #we found the destination!
        if current == dest:
            return (fscore[dest], rebuildpath(camefrom, current))

        #mark the current point as explored
        oset.remove(current)
        cset.add(current)

        #generate possible neighbours of the current point
        neighbours = []
        for delta in [-1, 0, 1]:
            new_x = current[0] + delta
            if new_x >= 0 and new_x < len(g):
                for delta_ in [-1, 0, 1]:
                    if abs(delta + delta_) == 1:
                        new_y = current[1] + delta_
                        if new_y >= 0 and new_y < len(g[0]):
                            if g[new_x][new_y][1] in items[current[2]]:
                                    neighbours.append((new_x, new_y, current[2]))
        for item in items:
            if item != current[2] and g[current[0]][current[1]][1] in items[item]:
                neighbours.append((current[0], current[1], item))

        #add neighbours to exploration list if we haven't visited them before
        for n in neighbours:
            
            time = 0
            if current[0] != n[0] or current[1] != n[1]: time = 1
            else: time = 7
            
            #(we already explored from this neighbour)
            if n in cset: continue

            #(explore this neighbour, as we haven't seen it before)
            if n not in oset: oset.add(n)

            #(we already found a better way to this neighbour)
            elif gscore[current] + time >= gscore.get(n, 10000): continue

            #(this is best route to this neighbour so far, so record it)
            camefrom[n] = current
            gscore[n] = gscore[current] + time
            fscore[n] = gscore[n] + h(n, dest)
