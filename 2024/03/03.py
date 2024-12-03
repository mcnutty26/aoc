import sys
import re
from functools import reduce
from operator import mul

code = ""
opMul = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
opDo = re.compile(r"do\(\).*?don't\(\)")
total1 = 0
total2 = 0

with open(sys.argv[1]) as puzzle:
    code += "do()"
    for line in puzzle:
        code += line.rstrip()
    code += "don't()"

ops = opMul.findall(code)
for op in ops:
    args = [int (arg) for arg in op[4:-1].split(',')]
    total1 += reduce(mul, args)

ops = opDo.findall(code)
for op in ops:
    subOps = opMul.findall(op)
    for subOp in subOps:
        args = [int (arg) for arg in subOp[4:-1].split(',')]
        total2 += reduce(mul, args)

print(total1, total2)
