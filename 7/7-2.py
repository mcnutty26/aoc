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
workers = dict({1:[None,0],2:[None,0],3:[None,0],4:[None,0],5:[None,0]})
time = 0
while len(stack):
    stack.sort()
    for worker in workers:
        if time >= workers[worker][1]:
            if workers[worker][0] is not None:
                done.append(workers[worker][0])
                workers[worker][0] = None
            if workers[worker][0] is None:
                for x in stack:
                    cando = True
                    for y in rsteps[x]:
                        if y not in done:
                            cando = False
                    if cando:
                        workers[worker] = [x,time + ord(x) -4]
                        stack.remove(x)
                        break
    time = min(x[1] for _,x in workers.items() if x[0] is not None)
print(time)
