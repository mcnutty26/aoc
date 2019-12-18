from pathfinding import astar
import heapq

cave = []
keys = dict()
cache = dict()
reqs = dict()

with open('input.txt', 'rt') as textfile:
    for line in textfile:
        cave.append([])
        for char in line:
            cave[-1].append(char)
            # Store keys and the entrance for pathfinding
            if char.islower() or char == '@':
                keys[char] = (len(cave)-1, len(cave[-1])-1)

# Cache a* path lengths between nodes, as well as the keys required
# Return False unless the required keys are a subset of the ones we have
def get_path(start: tuple, end: tuple, found) -> int:
    if (start, end) not in cache:
        cache[(start, end)] = astar(start, end, cave, keys)
    result = cache[(start, end)]
    if result and result[1] <= set(found):
            return result[0]
    return False

queue = [(0, '@')]
heapq.heapify(queue)
candidate = ''
value = 0
bests = dict()

# Do a BFS starting from the entrance
# Pop the smallest value path off the heap
# Prune any paths that are strictly worse than ones we've already tried
# Push on that current value + the reachable keys
while len(candidate) < len(keys):
    value, candidate = heapq.heappop(queue)
    if bests.get(str(sorted(candidate[:-1]))+candidate[-1], 1000000) < value:
        continue
    bests[str(sorted(candidate[:-1]))+candidate[-1]] = value
    for key in [k for k in keys if k not in candidate]:
        if get_path(candidate[-1], key, candidate):
            heapq.heappush(queue, (value + get_path(candidate[-1], key, candidate), candidate + key))
print(candidate, value)

# This is where things get messy
# We only need to run the above for each of the four subgrids
# I manually edited the input to make four text files
# The code is also bodged together, but it's 10 to midnight and it got me the star /shrug
# In future this could totally be worked into the code for part 1
cave = []
keys = dict()
doors = dict()
cache = dict()
reqs = dict()
queue = [(0, '@')]
heapq.heapify(queue)
candidate = ''
value = 0
bests = dict()
top = 0

with open('in-4.txt', 'rt') as textfile:
    for line in textfile:
        cave.append([])
        for char in line:
            cave[-1].append(char)
            if char.islower() or char == '@':
                keys[char] = (len(cave)-1, len(cave[-1])-1)
            elif char.isupper():
                doors[char] = (len(cave)-1, len(cave[-1])-1)

def do_cache(start, end, found):
    if (start, end) not in cache:
        cache[(start, end)] = astar(start, end, cave, keys)
    result = cache[(start, end)]
    if result and result[1] <= set(found):
        return result[0]
    return False

def get_path2(start: tuple, end: tuple, found) -> int:
    i = len(start) - 1
    while not do_cache(start[i], end, found) and i >= 0:
        i -= 1
    return do_cache(start[i], end, found)

for door in doors:
    if door.lower() not in keys:
        cave[doors[door][0]][doors[door][1]] = '.'

while len(candidate) < len(keys):
    value, candidate = heapq.heappop(queue)
    if bests.get(str(sorted(candidate[:-1]))+candidate[-1], 1000000) < value:
        continue
    bests[str(sorted(candidate[:-1]))+candidate[-1]] = value
    if len(candidate) > top:
        top = len(candidate)
        print(top)
    for key in [k for k in keys if k not in candidate]:
        if get_path2(candidate, key, candidate):
            heapq.heappush(queue, (value + get_path2(candidate, key, candidate), candidate + key))
print(candidate, value)
