from blist import blist
r = blist([3,7])
e = [0,1]
target = 607331
improved = []
while len(improved) < 10:
    s = r[e[0]] + r[e[1]]
    if s > 9:
        if len(r) >= target:
            improved.append(int(str(s)[0]))
            improved.append(int(str(s)[1]))
        r.append(int(str(s)[0]))
        r.append(int(str(s)[1]))
    else:
        if len(r) >= target: improved.append(s)
        r.append(s)
    for elf in range(len(e)): e[elf] = (e[elf] + r[e[elf]] + 1) % len(r)
print(improved)
