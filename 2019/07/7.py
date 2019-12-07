import csv, sys, itertools
from vm import intcode_vm

program = []
phases1 = [0, 1, 2, 3, 4]
phases2 = [5, 6, 7, 8, 9]

with open(sys.argv[1], 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

hi1 = 0
for i in itertools.permutations(phases1, 5):
    o1 = intcode_vm(program.copy(), [i[0], 0]).run()[0]
    o2 = intcode_vm(program.copy(), [i[1], o1]).run()[0]
    o3 = intcode_vm(program.copy(), [i[2], o2]).run()[0]
    o4 = intcode_vm(program.copy(), [i[3], o3]).run()[0]
    o5 = intcode_vm(program.copy(), [i[4], o4]).run()[0]
    hi1 = max(o5, hi1)

hi2 = 0
for i in itertools.permutations(phases2, 5):
    v1 = intcode_vm(program.copy(), [i[0], 0])
    v2 = intcode_vm(program.copy(), [i[1], v1.run()[0]])
    v3 = intcode_vm(program.copy(), [i[2], v2.run()[0]])
    v4 = intcode_vm(program.copy(), [i[3], v3.run()[0]])
    v5 = intcode_vm(program.copy(), [i[4], v4.run()[0]])
    v1.input_queue.append(v5.run()[0])
    
    while v5.halted == False:
        v2.input_queue.append(v1.run()[0])
        v3.input_queue.append(v2.run()[0])
        v4.input_queue.append(v3.run()[0])
        v5.input_queue.append(v4.run()[0])
        o6 = v5.run()[0]
        v1.input_queue.append(o6)
    hi2 = max(o6, hi2)
print(hi1, hi2)
