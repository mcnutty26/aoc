import sys
from collections import defaultdict
from itertools import combinations

grid = set()
freqs = defaultdict(list)
antinodes1, antinodes2 = set(), set()

with open(sys.argv[1]) as puzzle:
    x = 0
    for line in puzzle:
        y = 0
        for item in line.rstrip():
            grid.add((x, y))
            if item != '.':
                freqs[item].append((x, y))
            y += 1
        x += 1

for freq, locs in freqs.items():
    for a, b in combinations(locs, 2):
        dX = a[0] - b[0]
        dY = a[1] - b[1]
        newA = (a[0] + dX, a[1] + dY)
        newB = (b[0] - dX, b[1] - dY)
        if newA in grid:
            antinodes1.add(newA)
        if newB in grid:
            antinodes1.add(newB)
        i, j = 0, 0
        while (a[0] + i*dX, a[1] + i*dY) in grid:
            antinodes2.add((a[0] + i*dX, a[1] + i*dY))
            i += 1
        while (b[0] - j*dX, b[1] - j*dY) in grid:
            antinodes2.add((b[0] - j*dX, b[1] - j*dY))
            j += 1

print(len(antinodes1), len(antinodes2))
