import csv, sys
from vm import intcode_vm

program = []
in_queue = []
with open(sys.argv[1], 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

for value in sys.argv[2:]:
    in_queue.append(int(value))

vm = intcode_vm(program.copy(), in_queue)
print(vm.run())
