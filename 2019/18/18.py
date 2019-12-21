from pathfinding import astar
import sys, heapq

cave = []
keys = dict()
doors = dict()
cache = dict()
reqs = dict()

with open('input.txt', 'rt') as textfile:
    # Load the cave from the input file
    for line in textfile:
        cave.append([])
        for char in line.strip():
            cave[-1].append(char)

def gen() -> None:
    # bookkeeping function to set up variables for bfs
    global keys, doors, cache, reqs
    keys = dict()
    doors = dict()
    cache = dict()
    reqs = dict()
    
    # Determine locations of keys and doors in the maze
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            if cave[y][x].islower() or cave[y][x] == '@':
                keys[cave[y][x]] = (y, x)
            elif cave[y][x].isupper():
                doors[cave[y][x]] = (y, x)

    # Remove doors that are not present in the cave (for part 2)
    for door in doors:
        if door.lower() not in keys:
            cave[doors[door][0]][doors[door][1]] = '.'

def get_path(start: str, end: str, found) -> int or bool:
    # Cache a* path lengths between nodes, as well as the keys required
    if (start, end) not in cache:
        cache[(start, end)] = astar(start, end, cave, keys)
    result = cache[(start, end)]
    if result and result[1] <= set(found):
            return result[0]
    return False

def bfs() -> int:
    # Do a BFS starting from the entrance, pruning any paths that are strictly worse than ones we've already tried
    queue = [(0, '@')]
    heapq.heapify(queue)
    candidate = ''
    value = 0
    bests = dict()
    while len(candidate) < len(keys):
        value, candidate = heapq.heappop(queue)
        sys.stdout.write(f" Trying path: {candidate}\r")
        sys.stdout.flush()
        if bests.get(str(sorted(candidate[:-1]))+candidate[-1], 1000000) < value:
            continue
        bests[str(sorted(candidate[:-1]))+candidate[-1]] = value
        for key in [k for k in keys if k not in candidate]:
            if get_path(candidate[-1], key, candidate):
                heapq.heappush(queue, (value + get_path(candidate[-1], key, candidate), candidate + key))
    print('\n')
    return value

# Part 1 - one robot
gen()
print(bfs())

# Part 2 - four robots
# Modify the cave to add extra walls and entrances
start = keys['@']
cave[start[0]][start[1]] = '#'
cave[start[0] + 1][start[1]] = '#'
cave[start[0] - 1][start[1]] = '#'
cave[start[0]][start[1] + 1] = '#'
cave[start[0]][start[1] - 1] = '#'
cave[start[0] + 1][start[1] + 1] = '@'
cave[start[0] + 1][start[1] - 1] = '@'
cave[start[0] - 1][start[1] + 1] = '@'
cave[start[0] - 1][start[1] - 1] = '@'

# Split the cave into four subcaves
subcaves = [[],[],[],[]]
subcaves[0] = cave[:(len(cave) // 2) + 1]
subcaves[1] = cave[:(len(cave) // 2) + 1]
subcaves[2] = cave[(len(cave) // 2):]
subcaves[3] = cave[(len(cave) // 2):]
for i in range(len(subcaves[0])):
    subcaves[0][i] = cave[i][:(len(cave[0]) // 2) + 1]
    subcaves[1][i] = cave[i][(len(cave[0]) // 2):]
    subcaves[2][i] = cave[i+(len(cave)//2)][:(len(cave[0]) // 2) + 1]
    subcaves[3][i] = cave[i+(len(cave)//2)][(len(cave[0]) // 2):]

# Run bfs on each subcave and sum the results
total = 0
for i in range(4):
    cave = subcaves[i]
    gen()
    total += bfs()
print(total)
