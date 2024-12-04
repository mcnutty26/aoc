import sys

listA = []
listB = []
totals = [0, 0]

with open(sys.argv[1]) as puzzle:
    for line in puzzle:
        items = line.split(' ')
        listA.append(int(items[0]))
        listB.append(int(items[-1].strip()))

listA.sort()
listB.sort()

for i in range(len(listA)):
    totals[0] += abs(listA[i] - listB[i])
    totals[1] += listA[i] * listB.count(listA[i])

print(totals)

