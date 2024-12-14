import sys
import re
from itertools import combinations

robots = []
totals = [1,0]
maxX, maxY = 101, 103

class  robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def tick(self, maxX, maxY):
        self.x = (self.x + self.vx) % maxX
        self.y = (self.y + self.vy) % maxY
        if self.x < 0:
            self.x += maxX
        if self.y < 0:
            self.y += maxY

with open(sys.argv[1]) as puzzle:
    parse = re.compile(r"(?P<P>(?<=p=)-?\d*,-?\d*).*?(?P<V>(?<=v=)-?\d*,-?\d*)")
    for line in puzzle.readlines():
        p = parse.search(line).groups()
        [x, y] = [int(n) for n in p[0].split(',')]
        [vx, vy] = [int(n) for n in p[1].split(',')]
        robots.append(robot(x, y, vx, vy))

def show():
    for y in range(maxY):
        s = ""
        for x in range(maxX):
            total = 0
            for robot in robots:
                if robot.x == x and robot.y == y:
                    total += 1
            s += str(total) if total else '.'
        print(s)

t = 0
noTree = True
while noTree:
    t += 1
    for robot in robots:
        robot.tick(maxX, maxY)
    
    if t == 100: 
        lr = [(0, (maxX - 1) / 2 - 1), ((maxX - 1) / 2 + 1, maxX-1)]
        ud = [(0, (maxY - 1) / 2 - 1), ((maxY - 1) / 2 + 1, maxY-1)]

        for q1 in lr:
            for q2 in ud:
                total = 0
                for robot in robots:
                    if robot.x >= q1[0] and robot.x <= q1[1]:
                        if robot.y >= q2[0] and robot.y <= q2[1]:
                            total += 1
                totals[0] *= total
        print(totals)

    noTree = False
    for r1, r2 in combinations(robots, 2):
        if r1.x == r2.x and r1.y == r2.y:
            noTree = True

    if not noTree:
        print(t)
        show()
        break
