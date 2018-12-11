g= []
for x in range(300):
    r = x+10
    g.append([])
    for y in range(300): g[x].append(int(str(((r*y)+5034)*r)[-3])-5)
top = [[0,0], 0]
for x in range(300-3):
    for y in range(300-3):
        total = 0
        for a in range(3):
            for b in range(3): total += g[x+a][y+b]
        if total > top[1]: top = [[x,y],total]
print(top[0][0], top[0][1])
