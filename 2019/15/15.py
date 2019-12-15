import csv, sys
sys.path.append('../13/')
from vm import intcode_vm

program = []
rels = [[0, 1], [0, -1], [-1, 0], [1, 0]]
reverse = [1, 0, 3, 2]
grid = {}
location = (0, 0)
movement = []

with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

def move(direction, backtracking=False):
    global location

    # Feed the direction into the robot and see what we get back
    robot.input_queue.append(direction+1)
    output = robot.run()[0]
    rel = rels[direction]

    # We hit a wall :(
    if output == 0:
        grid[(location[0] + rel[0], location[1] + rel[1])] = 0
    
    # We moved somewhere! Update the grid
    else:
        location = (location[0] + rel[0], location[1] + rel[1])
        grid[location] = output
        if not backtracking:
            movement.append(direction)

def mapping():
    moved = False
    for i in range(len(rels)):
        #explore new tiles if we can
        if grid.get((location[0] + rels[i][0], location[1] + rels[i][1]), -1) == -1:
            move(i)
            moved = True
            break
    #otherwise backtrack
    if not moved:
        move(reverse[movement.pop()], True)

robot = intcode_vm(program.copy(), [])
robot.run()

# Part 1
while 2 not in grid.values():
    mapping()
print(len(movement))


# Part 2
time = 0

# Continue to map the rest of the area
while len(movement) > 0:
    mapping()

# Flood-fill the area with oxygen
while 1 in grid.values():
    oxygen = [loc for loc in grid if grid[loc] == 2]
    for loc in [loc for loc in grid if grid[loc] == 2]:
        for i in range(len(rels)):
            if grid[(loc[0] + rels[i][0], loc[1] + rels[i][1])] == 1:
                grid[(loc[0] + rels[i][0], loc[1] + rels[i][1])] = 2
    time += 1
print(time)
