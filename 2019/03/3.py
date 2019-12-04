import csv
wires = []
with open('input.csv', 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        wires.append([])
        for cell in row:
            wires[-1].append((cell[0], int(cell[1:])))

lines = []
intersections = set()
distances = dict()

for wire in wires:
    lines.append(set())
    x = 0
    y = 0
    d = 0
    for move in wire:
        for i in range(move[1]):
            if move[0] == "U":
                y += 1
            if move[0] == "D":
                y -= 1
            if move[0] == "R":
                x += 1
            if move[0] == "L":
                x -= 1
            d += 1
            lines[-1].add((x, y))
            if (x, y) not in distances:
                distances[(x, y)] = 0
            distances[(x, y)] += d

lowest = float('inf')
for intersect in lines[0].intersection(lines[1]):
    if distances[intersect] < lowest:
        lowest = distances[intersect]
    intersections.add(abs(intersect[0]) + abs(intersect[1]))
    
print(min(intersections), int(lowest))
