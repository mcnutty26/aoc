import csv, sys
sys.path.append('../13/')
from vm import intcode_vm

program = []

# Read in the intcode program
with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

# Helper function to ASCIIfy a list
def prep(spsc: list) -> list:
    out = []
    for command in spsc:
        for char in command:
            out.append(ord(char))
        out.append(10)
    return out

# Jump if (C=0 and D=1) or (A=0)
# i.e. we can execute a jump "in advance" of a pit, or we need to jump to not die
walk = ["NOT C J", "AND D J", "NOT A T", "OR T J", "WALK"] 
drone = intcode_vm(program, prep(walk))
print(drone.run()[-1])

# Jump if (A=0 or B=0 or C=0) and (E=1 or H=1) and (D=1)
# i.e only jump when there's a hole coming up and we can guarantee a safe move following the jump and the jump is safe
run = ["NOT A J", "NOT J J", "AND B J", "AND C J", "NOT J J", "NOT H T", "NOT T T", "OR E T", "AND T J", "AND D J", "RUN"] 
drone = intcode_vm(program, prep(run))
print(drone.run()[-1])
