import sys

grid = {}
totals = [0, 0]
startPos = (-1, -1)
startHdg = -1
dirs = [(0,-1),(1,0),(0,1),(-1,0)]

with open(sys.argv[1]) as puzzle:
    y = 0
    for line in puzzle:
        x = 0
        for char in line.rstrip():
            grid[(x, y)] = char
            if char in "^v<>":
                dirMap = ['^', 'v', '<', '>']
                startPos = (x, y)
                startHdg = dirMap.index(char)
            x += 1
        y += 1

def getNext(pos, hdg):
    return (pos[0] + dirs[hdg][0], pos[1] + dirs[hdg][1])

def run(pos, hdg, instance):
    i = 0
    while (pos in instance) and (i < 10000):
        instance[pos] = 'X'
        while instance.get(getNext(pos, hdg)) == '#':
            hdg = (hdg + 1) % 4
        pos = getNext(pos, hdg)
        i += 1
    if i == 10000:
        return False
    else:
        return instance

locs = run(startPos, startHdg, grid)
totals[0] = sum([1 for x in locs.values() if x == 'X'])

for key, value in locs.items():
    if value == 'X':
        modified = grid.copy()
        modified[key] = '#'
        if run(startPos, startHdg, modified) == False:
            totals[1] += 1

print(totals)
