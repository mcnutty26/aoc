import csv
import string
from datetime import datetime
from collections import defaultdict
fsteps = defaultdict(list)
rsteps = defaultdict(list)
with open('7.csv', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for step in r:
        fsteps[step[0]].append(step[1])
        rsteps[step[1]].append(step[0])
node = fsteps.keys()[0]
while len(rsteps[node]) > 0:
    node = rsteps[node][0]
stack = list(l for l in string.ascii_uppercase if l in fsteps or l in rsteps)
done = []
while len(stack):
    stack.sort()
    for x in stack:
        cando = True
        for y in rsteps[x]:
            if y not in done:
                cando = False
        if cando:
            node = x
            stack.remove(x)
            break
    done.append(node)
print(''.join(map(str, done)))
