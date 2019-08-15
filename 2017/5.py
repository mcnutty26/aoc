import sys
inp = []
with open(sys.argv[1], "r") as f:
    for line in f:
        inp.append(int(line.rstrip()))
total = [0,int(sys.argv[2])]
pc = 0
while 0 <= pc and pc < len(inp):
    inc_dec = 1
    if total[1] == 2 and inp[pc] >= 3:
        inc_dec = -1
    inp[pc] += inc_dec
    pc += inp[pc] - inc_dec
    total[0] += 1
print(total[0])

    
