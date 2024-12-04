import sys
from collections import defaultdict

grid = {}
totals = [0, 0]

with open(sys.argv[1]) as puzzle:
    x = 0
    for line in puzzle:
        y = 0
        for item in line.rstrip():
            grid[(x, y)] = item
            y += 1
        x += 1

def xmas(coord):
    count = 0
    directions = [-1, 0, 1]
    for x in directions:
        for y in directions:
            word = ""
            for i in range(4):
                word += grid.get((coord[0]+(x*i), coord[1]+(y*i)), '.')
            if word == "XMAS":
                count += 1
    return count

def x_mas(coord):
    word1 = grid.get((coord[0]-1, coord[1]-1), '.') + grid[coord] + grid.get((coord[0]+1, coord[1]+1), '.')
    word2 = grid.get((coord[0]-1, coord[1]+1), '.') + grid[coord] + grid.get((coord[0]+1, coord[1]-1), '.')
    if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
        return 1
    else:
        return 0

for key, value in grid.items():
    totals[0] += xmas(key)
    totals[1] += x_mas(key)

print(totals)
