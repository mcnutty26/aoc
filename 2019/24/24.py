from copy import deepcopy

raw = []

# Load the 5x5 grid
with open('input.txt', 'rt') as textfile:
    for line in textfile:
        raw.append([])
        for char in line.strip():
            if char == '#':
                raw[-1].append(1)
            else:
                raw[-1].append(0)


# Return the sum of neighbours on a flat grid
def neighbours(g: list, y: int, x: int) -> int:
    out = []
    rels = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for rel in rels:
        if len(g) > y+rel[0] >= 0 and len(g[0]) > x + rel[1] >= 0:
            out.append(grid[y + rel[0]][x + rel[1]])
    return sum(out)


# Return the sum of neighbours on a recursive grid
def recursive_neighbours(l: dict, g: int,  y: int, x: int) -> int:
    out = []
    rels = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for rel in rels:

        # inner edge -> fetch value from level g+1
        if y+rel[0] == 2 and x+rel[1] == 2:
            if g+1 not in l:
                continue
            # going right into the middle
            elif rel[1] == 1:
                out += [n[0] for n in l[g+1]]
            # going left into the middle
            elif rel[1] == -1:
                out += [n[4] for n in l[g+1]]
            # going down into the middle
            elif rel[0] == 1:
                out += l[g+1][0]
            # going up into the middle
            elif rel[0] == -1:
                out += l[g+1][4]

        # top edge
        elif y+rel[0] == -1 and g-1 in l:
            out.append(l[g-1][1][2])
        # bottom edge
        elif y+rel[0] == 5 and g-1 in l:
            out.append(l[g-1][3][2])
        # left edge
        elif x+rel[1] == -1 and g-1 in l:
            out.append(l[g-1][2][1])
        # right edge
        elif x+rel[1] == 5 and g-1 in l:
            out.append(l[g-1][2][3])

        # otherwise proceed as normal
        elif 0 <= y+rel[0] < 5 and 0 <= x + rel[1] < 5:
            out.append(l[g][y+rel[0]][x+rel[1]])
    return sum(out)


# Return a biodiversity hash of a grid
def biodiversity(g: list) -> int:
    score = 0
    inc = 1
    for y in range(len(g)):
        for x in range(len(g[0])):
            score += g[y][x] * inc
            inc *= 2
    return score


# Move between sucessive states for a flat grid
def state_step(g: list) -> list:
    new = deepcopy(g)
    for y in range(len(g)):
        for x in range(len(g[0])):
            n = neighbours(g, y, x)
            if g[y][x] == 1 and n != 1:
                new[y][x] = 0
            elif g[y][x] == 0 and (n == 1 or n == 2):
                new[y][x] = 1
    return new


# Move between sucessive states for a recursive grid
def recursive_state_step(l: dict) -> dict:
    mn = min(l.keys())
    mx = max(l.keys())

    if sum([sum(x) for x in l[mn]]) != 0:
        l[mn-1] = []
        for i in range(5):
            l[mn-1].append([0, 0, 0, 0, 0])
    
    if sum([sum(x) for x in l[mx]]) != 0:
        l[mx+1] = []
        for i in range(5):
            l[mx+1].append([0, 0, 0, 0, 0])
    
    new = deepcopy(l)

    for i in l:
        g = l[i]
        for y in range(5):
            for x in range(5):
                if y != 2 or x != 2:
                    n = recursive_neighbours(l, i, y, x)
                    if g[y][x] == 1 and n != 1:
                        new[i][y][x] = 0
                    elif g[y][x] == 0 and (n == 1 or n == 2):
                        new[i][y][x] = 1

    return new


# Part 1
grid = deepcopy(raw)
states = set()
while True:
    if biodiversity(grid) not in states:
        states.add(biodiversity(grid))
    else:
        print(biodiversity(grid))
        break

    grid = state_step(grid)


# Part 2
grid = deepcopy(raw)
levels = {0: grid}
bugs = 0

for _ in range(200):
    levels = recursive_state_step(levels)

for level in levels:
    bugs += sum([sum(y) for y in levels[level]])

print(bugs)
