import sys
inp = []
with open(sys.argv[1], "r") as f:
    for value in f.readline().rstrip().split(','):
        inp.append(value)
reductions = []
reductions.append(('n', 's', None))
reductions.append(('e', 'w', None))
reductions.append(('sw', 'se', 's'))
reductions.append(('ne', 'nw', 'n'))
reductions.append(('ne', 'se', 'e'))
reductions.append(('nw', 'sw', 'w'))
reductions.append(('ne', 's', 'se'))
reductions.append(('nw', 's', 'sw'))
reductions.append(('sw', 'n', 'nw'))
reductions.append(('se', 'n', 'ne'))
maximum = 0
for i in range(1,len(inp)+1):
    path = inp[:i]
    change = True
    while change:
        change = False
        for reduction in reductions:
            if reduction[0] in path and reduction[1] in path:
                path.remove(reduction[0])
                path.remove(reduction[1])
                if reduction[2] is not None:
                    path.append(reduction[2])
                change = True
    maximum = max(maximum, len(path))
    minimum = len(path)
print(minimum, maximum)

