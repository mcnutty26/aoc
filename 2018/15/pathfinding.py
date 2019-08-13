#copied from the main file
#makes working with elves and goblins less error prone
class creature:
    def __init__(self, y, x, t):
        self.y = y
        self.x = x
        self.type = t
        self.hp = 200
        self.alive = True
    def __lt__(self, other):
        if self.y < other.y: return True
        if self.y == other.y and self.x < other.x: return True
        return False
    def __gt__(self, other):
        if self.y > other.y: return True
        if self.y == other.y and self.x > other.x: return True
        return False

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
def astar(thing, other, g, c):
    oset = set()
    cset = set()
    camefrom = dict()
    gscore = dict()
    fscore = dict()

    start = (thing.y, thing.x)
    dest = (other.y, other.x)

    #short circuit if given a stupid input
    if start[0] == dest[0] and start[1] == dest[1]:
        #(start point is the goal point)
        return [dest]
    if g[start[0]][start[1]] != '.':
        #(start point is a wall)
        return None
    for other in c:
        if thing.y == other.y and thing.x == other.x and other.alive and other is not thing:
            #(start point is another unit))
            return None
    
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
        neighbours_ = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]
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
                dup = False
                for thing in c:
                    if n[0] == thing.y and n[1] == thing.x and thing.alive:
                        #(neighbour is an elf or a goblin)
                        dup = True
                if not dup:
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

#return the closest enemy to this creature (sorted by distance, then by reading order)
def get_target(thing, g, c):
    stuff = c.copy()
    stuff.sort()
    closest = (1000, None)
    for other in stuff:
        if other.type != thing.type and other.alive:
            path = astar(thing, other, g, c)
            if path is not None and len(path) < closest[0]:
                closest = (len(path), other)
    return closest[1]

#return the next step for this creature (sorted by reading order)
def get_step(thing, g, c):
    target = get_target(thing, g, c)

    if target is None: return (thing.y, thing.x)

    up = astar(creature(thing.y-1,thing.x,thing.type), target, g, c)
    down = astar(creature(thing.y+1,thing.x,thing.type), target, g, c)
    left = astar(creature(thing.y,thing.x-1,thing.type), target, g, c)
    right = astar(creature(thing.y,thing.x+1,thing.type), target, g, c)

    best_distance = min(len(x) for x in [up, down, left, right] if x is not None)

    if up is not None and len(up) == best_distance:
        return up[0]
    elif left is not None and len(left) == best_distance:
        return left[0]
    elif right is not None and len(right) == best_distance:
        return right[0]
    else:
        return down[0]

#if this creature is adjacent to an enemy, return that enemy (sorted by reading order), otherwise return False
def get_adjacent(thing, c):
    stuff = c.copy()
    stuff.sort()
    target = None
    for other in c:
        if other.type != thing.type and other.alive:
            if abs(thing.x - other.x) + abs(thing.y - other.y) == 1:
                if target is None or other.hp < target.hp:
                    target = other
    if target is not None: return target
    return False
