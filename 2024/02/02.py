import sys
from itertools import pairwise, combinations

reports = []
aCount = 0
bCount = 0

with open(sys.argv[1]) as puzzle:
    for line in puzzle:
        reports.append([int(x) for x in line.split(' ')])

def safe(report):
    inc = True
    dec = True
    gentle = True
    for x, y in pairwise(report):
        if x < y:
            dec = False
        elif y < x:
            inc = False
        if abs(x - y) < 1 or abs(x - y) > 3:
            gentle = False
    return (inc or dec) and gentle

for report in reports:
    if safe(report):
        aCount += 1
    else:
        for subReport in combinations(report, len(report) - 1):
            if safe(subReport):
                bCount += 1
                break

print(aCount, aCount + bCount)
