import sys

disk1 = []

with open(sys.argv[1]) as puzzle:
    for ID, size in enumerate(puzzle.read().rstrip()):
        if int(size):
            disk1.append((-1 if ID%2 else ID//2, int(size)))

disk2 = disk1.copy()

def isSpace(disk, i, size):
    for i, block in enumerate(disk[:i]):
        if block[0] == -1 and block[1] >= size:
            return i
    return 0

def consolidate(disk):
    for i in range(len(disk)-1):
        if i < len(disk)-1 and disk[i][0] == -1 and disk[i+1][0] == -1:
            disk[i] = (-1, disk[i][1] + disk[i+1][1])
            disk.pop(i+1)

def checksum(disk):
    pos, total = 0, 0
    for block in disk:
        for i in range(block[1]):
            if block[0] != -1:
                total += block[0]*pos
            pos += 1
    return total

while isSpace(disk1, len(disk1), 1):
    curr = disk1.pop()
    if curr[0] != -1:
        loc = isSpace(disk1, len(disk1), 1)
        slack = disk1[loc][1]-1
        if slack:
            disk1[loc] = (-1, slack)
            disk1.insert(loc, (curr[0], 1))
        else:
            disk1[loc] = (curr[0], 1)
        if curr[1] > 1:
            disk1.append((curr[0], curr[1]-1))

target = len(set(x[0] for x in disk2))
done = {-1}

while len(done) < target:
    for i in range(len(disk2)-1, -1, -1):
        if disk2[i][0] not in done:
            done.add(disk2[i][0])
            loc = isSpace(disk2, i, disk2[i][1])
            if loc:
                curr = disk2.pop(i)
                disk2.insert(i, (-1, curr[1]))
                if disk2[loc][1] > curr[1]:
                    slack = disk2[loc][1] - curr[1]
                    disk2.insert(loc+1, (-1, slack))
                disk2[loc] = curr
                consolidate(disk2)
            break

print(checksum(disk1), checksum(disk2))
