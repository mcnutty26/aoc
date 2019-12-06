import csv, sys
program = []
input_queue = []
ip = 0

with open(sys.argv[1], 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

for i in range(2, len(sys.argv)):
    input_queue.append(int(sys.argv[i]))

def get_data(mode, value):
    if mode == 0:
        return program[value]
    elif mode == 1:
        return value

##############
# Operations #
#############

def add(a, b, c):
    print("ADD", a, b, c)
    program[c] = a + b

def mul(a, b, c):
    print("MUL", a, b, c)
    program[c] = a * b

def io_in(a):
    print("IN", a)
    program[a] = input_queue.pop(0)

def io_out(a):
    print("OUT", a)

def jit(a, b):
    global ip
    print("JIT", a, b)
    if a != 0:
        ip = b
    else:
        ip += 3

def jif(a, b):
    print("JIF", a, b)
    global ip
    if a == 0:
        ip = b
    else:
        ip += 3

def lt(a, b, c):
    print("LT", a, b, c)
    if a < b:
        program[c] = 1
    else:
        program[c] = 0

def eq(a, b, c):
    print("EQ", a, b, c)
    if a == b:
        program[c] = 1
    else:
        program[c] = 0

#############
# Main Loop #
#############

print("START")
while program[ip] != 99:
    ins = program[ip]
    mode_1 = 0
    mode_2 = 0
    mode_3 = 0

    # Load the opcode
    if ins < 99:
        opcode = ins
    else:
        opcode = int(str(ins)[-2] + str(ins)[-1])

    # Load the parameter modes
    if ins > 99:
        mode_1 = int(str(ins)[-3])
    if ins > 999:
        mode_2 = int(str(ins)[-4])
    if ins > 9999:
        mode_3 = int(str(ins)[-5])

    # Run the instruction
    if opcode == 1:
        add(get_data(mode_1, program[ip + 1]), get_data(mode_2, program[ip + 2]), program[ip + 3])
        ip += 4
    elif opcode == 2:
        mul(get_data(mode_1, program[ip + 1]), get_data(mode_2, program[ip + 2]), program[ip + 3])
        ip += 4
    elif opcode == 3:
        io_in(program[ip + 1])
        ip += 2
    elif opcode == 4:
        io_out(get_data(mode_1, program[ip + 1]))
        ip += 2
    elif opcode == 5:
        jit(get_data(mode_1, program[ip + 1]), get_data(mode_2, program[ip + 2]))
    elif opcode == 6:
        jif(get_data(mode_1, program[ip + 1]), get_data(mode_2, program[ip + 2]))
    elif opcode == 7:
        lt(get_data(mode_1, program[ip + 1]), get_data(mode_2, program[ip + 2]), program[ip + 3])
        ip += 4
    elif opcode == 8:
        eq(get_data(mode_1, program[ip + 1]), get_data(mode_2, program[ip + 2]), program[ip + 3])
        ip += 4
    else:
        print("FAULT", opcode)
        break

print("HALT")
