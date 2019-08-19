import sys
from collections import defaultdict
inp = []
with open(sys.argv[1], "r") as f:
    for line in f:
        l = []
        for item in line.rstrip().split(' '):
            l.append(item)
        inp.append(l)
registers = defaultdict(int)
global_max = -sys.maxsize
for i in inp:
    if i[1] == 'inc':
        v = int(i[2])
    else:
        v = -int(i[2])
    if i[5] == '<' and registers[i[4]] < int(i[6]):
        registers[i[0]] += v
    elif i[5] == '>' and registers[i[4]] > int(i[6]):
        registers[i[0]] += v
    elif i[5] == '<=' and registers[i[4]] <= int(i[6]):
        registers[i[0]] += v
    elif i[5] == '>=' and registers[i[4]] >= int(i[6]):
        registers[i[0]] += v
    elif i[5] == '==' and registers[i[4]] == int(i[6]):
        registers[i[0]] += v
    elif i[5] == '!=' and registers[i[4]] != int(i[6]):
        registers[i[0]] += v
    global_max = max(global_max, max(registers.values()))
print(max(registers.values()), global_max)
