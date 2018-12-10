import csv
from collections import defaultdict
points = []
with open('10.csv', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for point in r: points.append([int(point[0]),int(point[1]),int(point[2]),int(point[3])])
def converged():
    min_max = max(b for _,b,_,_ in points) - min(b for _,b,_,_ in points)
    x = defaultdict(int)
    for point in points: x[point[0]] += 1
    if max(b for _,b in x.items()) >= min_max - 2: return True
    else: return False
while not converged():
    for point in points:
        point[0] += point[2]
        point[1] += point[3]
x_min_max = (min(a for a,_,_,_ in points), max(a for a,_,_,_ in points))
y_min_max = (min(b for _,b,_,_ in points), max(b for _,b,_,_ in points))
for y in range(y_min_max[0],y_min_max[1]+1):
    out = ""
    for x in range(x_min_max[0],x_min_max[1]+1):
        char = '.'
        for point in points:
            if point[0] == x and point[1] == y: char = '#'
        out += char
    print(out)
