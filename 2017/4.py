import sys
inp = []
with open(sys.argv[1], "r") as f:
    for line in f:
        inp.append(line.rstrip().split(' '))
total = [0,0]
for line in inp:
    p_set_1 = set()
    p_set_2 = set()
    for word in line:
        p_set_1.add(word)
        p_set_2.add(''.join(sorted(list(word))))
    if len(line) == len(p_set_1):
        total[0] += 1
    if len(line) == len(p_set_2):
        total[1] += 1
print(total[0], total[1])
