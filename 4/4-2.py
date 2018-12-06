import csv
from datetime import datetime

obs = []
with open('4.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for observation in r:
        obs.append([datetime.strptime(observation[0],"%Y-%m-%d %H:%M"), int(observation[1])])

obs.sort()
guards = dict()
gid = -1
start = datetime.now()

for ob in obs:
    if ob[1] == -1:
        start = ob[0]
    elif ob[1] == -2:
        guards[gid].append((start.minute,ob[0].minute))
    else:
        gid = ob[1]
        if gid not in guards:
            guards[gid] = []

def freq(gid):
    minutes = dict()
    top = 0
    minutes[0] = 0
    for nap in guards[gid]:
        start = nap[0]
        end = nap[1]
        i = start
        while i < end:
            if i not in minutes:
                minutes[i] = 0
            minutes[i] += 1
            if minutes[i] > minutes[top]:
                top = i
            i += 1
    return((top, minutes[top]))

tired = 157
for guard in guards:
    if freq(guard)[1] > freq(tired)[1]:
        tired = guard

print(freq(tired)[0]*tired)
