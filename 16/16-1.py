r = [0, 0, 0, 0]
def addr(a, b, c): r[c] = r[a] + r[b]
def addi(a, b, c): r[c] = r[a] + b
def mulr(a, b, c): r[c] = r[a] * r[b]
def muli(a,b,c): r[c] = r[a] * b
def banr(a,b,c): r[c] = r[a] & r[b]
def bani(a,b,c): r[c] = r[a] & b
def borr(a,b,c): r[c] = r[a] | r[b]
def bori(a,b,c): r[c] = r[a] | b
def setr(a,b,c): r[c] = r[a]
def seti(a,b,c): r[c] = a
def gtir(a,b,c):
    if a > r[b]: r[c] = 1
    else: r[c] = 0
def gtri(a,b,c):
    if r[a] > b: r[c] = 1
    else: r[c] = 0
def gtrr(a,b,c):
    if r[a] > r[b]: r[c] = 1
    else: r[c] = 0
def eqir(a,b,c):
    if a == r[b]: r[c] = 1
    else: r[c] = 0
def eqri(a,b,c):
    if r[a] == b: r[c] = 1
    else: r[c] = 0
def eqrr(a,b,c):
    if r[a] == r[b]: r[c] = 1
    else: r[c] = 0
opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
with open("16a.txt") as f:
    counter = 0
    start = []
    ins = []
    triples = 0
    for line in f:
        l = []
        for char in line.strip('\n').split(','): l.append(int(char))
        if counter == 0: start = l.copy()
        elif counter == 1: ins = l.copy()
        else:
            poss = 0
            for opcode in opcodes:
                r = start.copy()
                opcode(ins[1], ins[2], ins[3])
                if r == l: poss += 1
            if poss >= 3: triples += 1
        counter = (counter + 1) % 3
print(triples)
