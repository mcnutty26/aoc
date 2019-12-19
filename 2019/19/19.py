import csv, sys
sys.path.append('../13/')
from vm import intcode_vm

program = []
beams = 0
SIZE = 99
rows = dict()

# Read in the intcode program
with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

# Part 1 - quickly check the 50x50 grid
for i in range(50):
    for j in range(50):
        drone = intcode_vm(program, [i, j], True)
        beams += drone.run()[0]
print(beams)

# Part 2 - track the edges of the beam (linear complexity in the y axis)
start = 0
end = 0
i = -1
while True:
    i += 1
    
    # Not all of the early rows have beam squares :S
    if i < 10:
        rows[i] = (0, 0)
        continue

    # Find the start of the beam in the row
    for j in range(start, 5000):
        drone = intcode_vm(program, [i, j], True)
        r = drone.run()[0]
        if r == 1:
            start = j
            if end == 0:
                end = start 
            break

    # Find the end of the beam in the row
    for j in range(end, 5000):
        drone = intcode_vm(program, [i, j], True)
        if drone.run()[0] == 0:
            end = j - 1
            break

    # Store this so we can check back later
    rows[i] = (start, end)

    # Check if the row we saw SIZE times ago meets the criteria
    if i > SIZE:
        if rows[i-SIZE][1] - rows[i][0] == SIZE:
            print(((i-SIZE)*10000) + rows[i][0])
            break
