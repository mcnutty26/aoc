from z3 import *

class Bot:
    def __init__(self, x, y, z, r):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.r = int(r)
    def __str__(self):
        return f"({self.x},{self.y},{self.z}) => {self.r}"

n = []
with open("23.txt") as f:
    for line in f:
        li = line.strip('\n').split(',')
        n.append(Bot(li[0], li[1], li[2], li[3]))

s = Optimize()
ranges = []
x = Int('x')
y = Int('y')
z = Int('z')
count = Int('count')
dist = Int('d')

def z3_abs(x): return If(x >= 0,x,-x)

for i in range(len(n)):
    p = n[i]
    ranges.append(Int('in_range'+str(i)))
    s.add(ranges[i] == If(z3_abs(p.x - x) + z3_abs(p.y - y) + z3_abs(p.z - z) <= p.r, 1, 0))

s.add(count == sum(ranges)) 
s.add(d == z3_abs(x) + z3_abs(y) + z3_abs(z))

s.maximize(count)
goal = s.minimize(d)
s.check()

m = s.model()
print(f"({m[x]}, {m[y]}, {m[z]})")
print(s.lower(goal))
