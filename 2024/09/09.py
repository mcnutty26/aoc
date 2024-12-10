import sys

disk1 = []
currentId = 0

with open(sys.argv[1]) as puzzle:
    isFile = True
    for line in puzzle:
        for digit in line.rstrip():
            if isFile:
                disk1 += [currentId for i in range(int(digit))]
                currentId += 1
            else:
                disk1 += ['.' for i in range(int(digit))]
            isFile = not isFile

disk2 = disk1.copy()

while '.' in disk1:
    curr = disk1.pop()
    if curr != '.':
        disk1[disk1.index('.')] = curr

print(sum([i*disk1[i] for i in range(len(disk1))]))

def getSpace(disk, size):
    for i in range(len(disk)-size):
        if set(disk[i:i+size]) == {'.'}:
            return i
    return -1

done = {'.'}
check = len(disk2)

while len(done) < currentId + 1:
    for block in disk2[::-1]:
        if block not in done:
            size = sum([1 for i in disk2 if i == block])
            loc = getSpace(disk2, size)
            if loc != -1 and loc < disk2.index(block):
                for i in range(size):
                    disk2[disk2.index(block)] = '.'
                for i in range(size):
                    disk2.pop(loc)
                for i in range(size):
                    disk2.insert(loc, block)
            done.add(block)

print(sum([i*disk2[i] for i in range(len(disk2)) if disk2[i] != '.']))
