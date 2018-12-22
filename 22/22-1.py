t = (13,726)
d = 3066
g = []
s = 0
for x in range(t[0]+1):
    g.append([])
    for y in range(t[1]+1):
        i = 0
        if x == 0 and y == 0: i = 0
        elif x == t[0] and y == t[1]: i = 0
        elif y == 0: i = x*16807
        elif x == 0: i = y*48271
        else: i = g[x-1][y] * g[x][y-1]
        g[x].append((i+d)%20183)
for y in range(t[1]+1):
    for x in range(t[0]+1):
        s += g[x][y]%3
print(s)
