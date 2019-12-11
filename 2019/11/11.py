import csv, sys
sys.path.append('../09/')
from vm import intcode_vm

program = []
ship = dict()
position = (0, 0)
painted = set()

with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

def painting(robot):
    global ship
    position = (0, 0) # start at the origin
    offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)] # up, right, down, left
    offset = 0 # start facing up

    while robot.halted is False:
        robot.input_queue.append(ship.get(position, 0)) # feed in the colour of the current position
        output = (robot.run(), robot.output_queue.pop()) # (only returns last output by default)
        ship[position] = output[1] # update robot's position
        painted.add(position) # record that this position was painted
        if output[0] == 0:
            offset = (offset - 1) % 4 # turn left
        else:
            offset = (offset + 1) % 4 # turn right
        position = (position[0] + offsets[offset][0], position[1] + offsets[offset][1]) # move forward one square

robot1 = intcode_vm(program.copy(), [])
painting(robot1)
print(len(painted)) # answer to part 1

robot2 = intcode_vm(program.copy(), [])
ship = dict({(0, 0): 1}) # start on a white square
painting(robot2)

for j in range(1, -7, -1):
    line = ""
    for i in range(0, 42):
        if ship.get((i, j), 0) == 0:
            line += ' ' # square is black
        else:
            line += 'X' # square is white
    print(line)
