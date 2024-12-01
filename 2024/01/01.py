import sys

listA = []
listB = []
diffs = 0
similarity = 0

with open(sys.argv[1]) as puzzle:
    for line in puzzle:
        items = line.split(' ')
        listA.append(int(items[0]))
        listB.append(int(items[-1].strip()))

listA.sort()
listB.sort()

for i in range(len(listA)):
    diffs += abs(listA[i] - listB[i])
    similarity += listA[i] * listB.count(listA[i])

print(diffs, similarity)

