import sys
inp = []
with open(sys.argv[1], "r") as f:
    for line in f:
        inp.append(int(line.rstrip()))
def loop(data, switch):
    pc = 0
    total = 0
    while 0 <= pc and pc < len(data):
        inc_dec = 1
        if switch and data[pc] >= 3:
            inc_dec = -1
        data[pc] += inc_dec
        pc += data[pc] - inc_dec
        total += 1
    return total
print(loop(inp.copy(), False), loop(inp, True))

    
