from blist import blist
r = blist([3,7])
e = [0,1]
while True:
    if r[-6:] == blist([6,0,7,3,3,1]): break
    s = r[e[0]] + r[e[1]]
    if s > 9:
        r.append(int(str(s)[0]))
        if r[-6:] == blist([6,0,7,3,3,1]): break
        r.append(int(str(s)[1]))
    else: r.append(s)
    for elf in range(len(e)): e[elf] = (e[elf] + r[e[elf]] + 1) % len(r)
print(len(r)  -6)
