import csv
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
zone = 0
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        dist = 0
        for _,a,b in points:
            dist += abs(x-a)+abs(y-b) 
        if dist < 10000:
            zone += 1
print(zone)
