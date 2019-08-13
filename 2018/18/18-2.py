import sys
g = []
with open("18.txt") as f:
    for line in f:
        l = []
        for char in line.strip('\n'): l.append(char)
        g.append(l)
g_ = []
for x in g: g_.append(x.copy())
def get_neighbours(x, y):
    n = []
    if x-1 >= 0:
        n.append(g[x-1][y])
        if y-1 >= 0: n.append(g[x-1][y-1])
        if y+1 < ymax: n.append(g[x-1][y+1])
    if x+1 < xmax:
        n.append(g[x+1][y])
        if y-1 >= 0: n.append(g[x+1][y-1])
        if y+1 < ymax: n.append(g[x+1][y+1])
    if y-1 >= 0: n.append(g[x][y-1])
    if y+1 < ymax: n.append(g[x][y+1])
    return n
xmax = len(g)
ymax = len(g[0])
scores = dict()
trials = 1000
for i in range(trials):
    for x in range(len(g)):
        for y in range(len(g[x])):
            trees = 0
            lumber = 0
            for n in get_neighbours(x,y):
                if n == '|': trees += 1
                elif n == '#': lumber += 1
            if g[x][y] == '.':
                if trees >= 3:
                    g_[x][y] = '|'
            elif g[x][y] == '|':
                if lumber >= 3:
                    g_[x][y] = '#'
            elif g[x][y] == '#':
                if trees < 1 or lumber < 1:
                    g_[x][y] = '.'

    trees = 0
    lumber = 0
    for x in range(len(g)):
        for y in range(len(g[x])):
            if g[x][y] == '|': trees += 1
            elif g[x][y] == '#': lumber += 1
    score = trees*lumber

    if score in scores:
        scores[score].append(i)
    else: scores[score] = [i]
    
    g = []
    for line in g_: g.append(line.copy())

#find the score that occured most often
top = 0
top_score = 0
for k,v in scores.items():
    if len(v) > top:
        top = len(v)
        top_score = k
item = scores[top_score]
print(f"starting point is {item[-1]}")

#find the periodicity of this score (assuming the score cycles)
diff = 0
for i in range(1,len(item)):
    diff = item[i] - item[i-1]
print(f"period is {diff} ticks")

#determine the largest observed tick that would have had the same score as at tick 1000000000
i = 1000000000
while i >= trials:
    i -= diff
print(f"target tick is {i}")

#get the score for that tick
for k,v in scores.items():
    if i in v:
        print(k)
