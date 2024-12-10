import sys

grid = {}
adj = [(1,0), (0,1), (-1,0), (0,-1)]
totals = [0, 0]

with open(sys.argv[1]) as puzzle:
    y = 0
    for line in puzzle:
        x = 0
        for char in line.rstrip():
            grid[(x, y)] = int(char)
            x += 1
        y += 1

def reachable(point, dests):
    if grid[point] == 9:
        if point not in dests:
            dests.add(point)
            return [1, 1]
        return [0, 1]
    total = [0, 0]
    for space in [(point[0]+a[0], point[1]+a[1]) for a in adj]:
        if grid.get(space, -1) == (grid[point] + 1):
            res = reachable(space, dests)
            total[0] += res[0]
            total[1] += res[1]
    return total
    
for trailhead in [k for k, v in grid.items() if v == 0]:
    res = reachable(trailhead, set())
    totals[0] += res[0]
    totals[1] += res[1]

print(totals)
