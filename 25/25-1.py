class Point:
    def __init__(self, x, y, z, w):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.w = int(w)
points = []
with open("25.txt") as f:
    for line in f:
        li = line.strip('\n').split(',')
        points.append(Point(li[0], li[1], li[2], li[3]))
adj = dict()
for p1 in points:
    adj[p1] = []
    for p2 in points:
        if abs(p1.x-p2.x) + abs(p1.y-p2.y) + abs(p1.z-p2.z) + abs(p1.w-p2.w) <= 3: adj[p1].append(p2)
consts = []
stack = []
done = set()
new = None
current = None
while len(done) < len(points):
    if len(stack) == 0:
        for p in points:
            if p not in done:
                if new is not None: consts.append(new)
                stack.append(p)
                done.add(p)
                new = set()
                new.add(p)
                break
    else:
        current = stack.pop()
        for i in adj[current]:
            if i not in done:
                stack.append(i)
                done.add(i)
                new.add(i)
consts.append(new)
print(len(consts))
