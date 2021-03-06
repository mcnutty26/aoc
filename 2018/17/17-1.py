import time
DEBUG = False
in_points = []
g = dict()
with open("17.txt") as f:
    for line in f: in_points.append(line.strip('\n').split(','))

for point in in_points:
    ybase = ""
    xbase = ""
    
    if point[0].find('y') != -1:
        ybase = point[0][2:]
        xbase = point[1][3:]
    else:
        ybase = point[1][3:]
        xbase = point[0][2:]

    yexp = []
    xexp = []
    
    if ybase.find('..') != -1:
        r = ybase.split('..')
        yexp = range(int(r[0]), int(r[1])+1)
    else: yexp = [int(ybase)]
    
    if xbase.find('..') != -1:
        r = xbase.split('..')
        xexp = range(int(r[0]), int(r[1])+1)
    else: xexp = [int(xbase)]
    
    
    for y in yexp:
        for x in xexp:
            g[(y,x)] = '#'


ymax = max(point[0] for point in g.keys())
ymin = min(point[0] for point in g.keys())
xmax = max(point[1] for point in g.keys())
xmin = min(point[1] for point in g.keys())

g[(0,500)] = '+'
moved = True

def settled(coord):
    current = coord
    while g.get(current, '.') != '#' and g.get(current, '.').lower() == 'w' and current[1] > xmin: current = (current[0], current[1] - 1)
    if g.get(current, '.') != '#': return False
    current = coord
    while g.get(current, '.') != '#' and g.get(current, '.').lower() == 'w' and current[1] < xmax: current = (current[0], current[1] + 1)
    if g.get(current, '.') != '#': return False
    return True

while moved:

    moved = False
    water = list(g.keys())
    water.sort()
    water.reverse()

    for w in water:

        left = (w[0], w[1]-1)
        right = (w[0], w[1]+1)
        up = (w[0]-1, w[1])
        down = (w[0]+1, w[1])

        if g[w] == '#' or g[w] == '.' or g[w] == 'W':
            continue

        elif g[w] == '+':
            if g.get(down, '.') == '.':
                g[down] = 'w'
                moved = True

        elif g[w] == 'w':
            #advance downwards if empty
            if g.get(down, '.') == '.' and down[0] <= ymax:
                g[down] = 'w'
                moved = True
            #settle if settled
            if settled(w):
                g[w] = "W"
                moved = True
            #disperse on hard surface
            if (g.get(down, '.') == '#' or g.get(down, '.') == 'W') and g.get(left, '.') == '.':
                g[left] = 'w'
                moved = True
            if (g.get(down, '.') == '#' or g.get(down, '.') == 'W') and g.get(right, '.') == '.':
                g[right] = 'w'
                moved = True

    if DEBUG:
        print()
        for y in range(0, ymax+1):
            l = ""
            for x in range(xmin-1,xmax+2):
                if (y,x) in g:
                    l += g[(y,x)]
                else:
                    l += '.'
            print(l)
        time.sleep(0.5)

counterw = 0
counterW = 0
for k,v in g.items():
    if k[0] < ymin or k[0] > ymax: continue
    if v == 'w': counterw += 1 
    if v == 'W': counterW += 1
print(counterw + counterW)
print(counterW)
