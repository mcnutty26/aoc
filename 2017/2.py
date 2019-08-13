import sys
inp = []
with open(sys.argv[1], "r") as f:
    for line in f:
        inp.append(line.rstrip().split('\t'))
total = [0,0]
mx = -sys.maxsize
mn = sys.maxsize
for line in inp:
    for item in line:
        if item == '':
            continue
        if int(item) < mn:
            mn = int(item)
        if int(item) > mx:
            mx = int(item)
    total[0] += mx - mn
    mx = 0 - sys.maxsize
    mn = sys.maxsize
for line in inp:
    for item in line:
        for item_2 in line:
            if item != item_2 and int(item) % int(item_2) == 0:
                total[1] += int(int(item)/int(item_2))
print(total[0], total[1])
