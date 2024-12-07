import sys

eqns = []
totals = [0, 0]

with open(sys.argv[1]) as puzzle:
    for line in puzzle:
        total, args = line.rstrip().split(': ')
        eqn = [int(total)]
        for arg in args.split(' '):
            eqn.append(int(arg))
        eqns.append(eqn)

def recurse(eqn, isThreeOps):
    if len(eqn) == 2:
        return eqn[0] == eqn[1]
    x = eqn.pop(1)
    a = eqn.copy()
    a[1] += x
    b = eqn.copy()
    b[1] *= x
    if isThreeOps:
        c = eqn.copy()
        c[1] = int(str(x) + str(c[1]))
        return recurse(a, True) or recurse(b, True) or recurse(c, True)
    return recurse(a, False) or recurse(b, False)

for eqn in eqns:
    if recurse(eqn.copy(), False):
        totals[0] += eqn[0]
    if recurse(eqn.copy(), True):
        totals[1] += eqn[0]

print(totals)
