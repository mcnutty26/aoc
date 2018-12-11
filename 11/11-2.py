g= []
for x in range(300):
    r = x+10
    g.append([])
    for y in range(300): g[x].append(int(str(((r*y)+5034)*r)[-3])-5)
top = [[0,0,0], 0]
for s in range(1,300):
    for x in range(300-s):
        for y in range(300-s):
            total = 0
            for a in range(s):
                for b in range(s): total += g[x+a][y+b]
            if total > top[1]:
                top = [[x,y,s],total]
                print("=> ", top[0][0], top[0][1], top[0][2])
