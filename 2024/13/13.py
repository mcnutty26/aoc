import sys
import re
from sympy import Eq, solve
from sympy.abc import w, x

machines = []
totals = [0, 0]

class  machine:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

with open(sys.argv[1]) as puzzle:
    button = re.compile(r"(?P<X>(?<=X\+)\d*).*(?P<Y>(?<=Y\+)\d*)")
    prize = re.compile(r"(?P<X>(?<=X=)\d*).*(?P<Y>(?<=Y=)\d*)")
    lines = puzzle.readlines()
    for i in range(0, len(lines), 4):
        a = [int(x) for x in button.search(lines[i]).groups()]
        b = [int(x) for x in button.search(lines[i+1]).groups()]
        p = [int(x) for x in prize.search(lines[i+2]).groups()]
        machines.append(machine(a, b, p))

for m in machines:
    (aX, aY) = m.a
    (bX, bY) = m.b
    (pX, pY) = m.p
    
    sol = solve([
        Eq(aX*w + bX*x, pX),
        Eq(aY*w + bY*x, pY)])

    if sol[w] == int(sol[w]) and sol[x] == int(sol[x]):
        totals[0] += 3*sol[w] + sol[x]
    
    sol = solve([
        Eq(aX*w + bX*x, pX+10000000000000),
        Eq(aY*w + bY*x, pY+10000000000000)])

    if sol[w] == int(sol[w]) and sol[x] == int(sol[x]):
        totals[1] += 3*sol[w] + sol[x]

print(totals)
