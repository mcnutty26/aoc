import csv, sys
sys.path.append('../13/')
from vm import intcode_vm

program = []
grid = [[]]
pos = (0, 0)
scaffold = 0
CARDINALS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

def update(o):
    global grid, pos, scaffold
    grid = [[]]
    while len(o) > 0:
        token = o.pop(0)
        if token == 94:
            pos = (len(grid[-1]), len(grid)-1)
        if token == 10:
            grid.append([])
        else:
            if token == 35:
                scaffold += 1
            grid[-1].append(chr(token))

def g(x, y):
    if y >= len(grid) or x >= len(grid[y]):
        return False
    return grid[y][x]

def extract_path(start):
    path = ""
    vec = 0
    l = pos
    streak = 0
    while True:
        # Carry on going in the same direction if we can (straight through junctions)
        if g(l[0]+CARDINALS[vec][0], l[1]+CARDINALS[vec][1]) == '#':
            l = (l[0]+CARDINALS[vec][0], l[1]+CARDINALS[vec][1])
            streak += 1

        # Otherwise we're at a turn
        elif g(l[0]+CARDINALS[(vec + 1) % 4][0], l[1]+CARDINALS[(vec + 1) % 4][1]) == '#':
            vec = (vec + 1) % 4
            if streak > 0:
                path += str(streak) + ','
                streak = 0
            path += 'R,'
        elif g(l[0]+CARDINALS[(vec - 1) % 4][0], l[1]+CARDINALS[(vec - 1) % 4][1]) == '#':
            vec = (vec - 1) % 4
            if streak > 0:
                path += str(streak) + ','
                streak = 0
            path += 'L,'
        else:
            path += str(streak)
            break
    return path

def extract_routines(path):
    #consume from the start until there are fewer than 

# Part 1
robot = intcode_vm(program, [])
update(robot.run())
total = 0
for y in range(1, len(grid) - 3):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] == '#':
            if sum([1 for z in CARDINALS if grid[y+z[1]][x+z[0]] == '#']) > 2:
               total += x * y
print(total)

mfun = "A,B,A,B,C,C,B,A,C,A"
mroa = "L,10,R,8,R,6,R,10"
mrob = "L,12,R,8,L,12"
mroc = "L,10,R,8,R,8"
vout = "n"

ingredients = [mfun, mroa, mrob, mroc, vout]
crafted_input = []

for ingredient in ingredients:
    for char in ingredient:
        crafted_input.append(ord(char))
    crafted_input.append(10)

robot = intcode_vm(program, crafted_input)
robot.program[0] = 2
print("Path is", extract_path(pos))
print("Movement function is", mfun)
print("Movement routine A is", mroa)
print("Movement routine B is", mrob)
print("Movement routine C is", mroc)

print(robot.run()[-1])
