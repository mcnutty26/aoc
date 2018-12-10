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
seconds = 0
while not converged():
    for point in points:
        point[0] += point[2]
        point[1] += point[3]
    seconds += 1
print(seconds)
