import csv
from datetime import datetime
from collections import defaultdict
points = []
count = 0
with open('6.csv', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for point in r:
        points.append((count,int(point[1]), int(point[0])))
        count += 1
xmin = min(point[1] for point in points)
xmax = max(point[1] for point in points)
ymin = min(point[2] for point in points)
ymax = max(point[2] for point in points)
inf = set()
size = defaultdict(int)
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        dists = sorted([(abs(x-a)+abs(y-b)),i] for i,a,b in points)
        if dists[0][0] is not dists[1][0]:
            size[dists[0][1]] += 1
        if x is xmin or x is xmax or y is ymin or (y == ymax): #wth doesn't this work for "y is ymax"?!
            inf.add(dists[0][1])
print(max(b for a, b in size.items() if a not in inf))
