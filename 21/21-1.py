from collections import defaultdict
r = [0,0,0,0,0,0]
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
program = []
with open("21.txt") as f: 
    for line in f: program.append(line.strip('\n').split(' '))
ip = 0
ip_r = int(program.pop(0)[1])
options = set()
#i = 0
lr4 = 0
#heat = defaultdict(int)
while True:
#    heat[ip] += 1
    if ip >= len(program): break
    #i += 1
    if ip == 28:
        if r[4] not in options:
            options.add(r[4])
            lr4 = r[4]
            print(len(options))
        else:
            print(lr4)
            break
        #print(program[ip], r)
    r[ip_r] = ip
    for opcode in opcodes:
        if opcode.__name__ == program[ip][0]: opcode(int(program[ip][1]), int(program[ip][2]), int(program[ip][3]))
    ip = r[ip_r]
    ip += 1
#for item in heat:
 #   print(item, heat[item])
#print(options)
#print(len(options))
