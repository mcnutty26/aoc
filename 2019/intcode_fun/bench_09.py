import csv, sys
sys.path.append('../09/')
from vm import intcode_vm

program = []
input_queue = []

with open("fib.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

for item in sys.argv[1:]:
    input_queue.append(int(item))

intcode_vm(program, input_queue).run()
