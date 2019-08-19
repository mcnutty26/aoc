import sys
inp = []
with open(sys.argv[1], "r") as f:
        raw = f.readline().rstrip().split('\t')
        for r in raw:
            inp.append(int(r))
def loop(cycle):
    global inp
    seen = set()
    counter = 0
    while str(inp) not in seen:
        if not cycle or len(seen) == 0:
            seen.add(str(inp))
        counter += 1
        i = inp.index(max(inp))
        val = inp[i]
        inp[i] = 0
        i += 1
        while val > 0:
            if i > len(inp)-1:
                i = 0
            inp[i] += 1
            val -= 1
            i += 1
    return counter
print(loop(False), loop(True))
