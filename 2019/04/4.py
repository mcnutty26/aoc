lo = 134564
hi = 585159
sat1 = []
sat2 = []

def asc(n):
    last = 0
    for digit in str(n):
        if int(digit) < last:
            return False
        last = int(digit)
    return True

def adj1(n):
    last = ''
    for digit in str(n):
        if digit == last:
            return True
        last = digit
    return False

def adj2(n):
    last = ''
    s = str(n)
    for i in range(len(str(n)) - 3):
        if s[i] != s[i+1] and s[i+1] == s[i+2] and s[i+2] != s[i+3]:
            return 1
    if (s[0] == s[1] and s[1] != s[2]) or (s[-1] == s[-2] and s[-2] != s[-3]):
        return 1
    return 0

for i in range(lo, hi):
    if not asc(i):
        continue
    if adj1(i):
        sat1.append(i)
    if adj2(i):
        sat2.append(i)

print(len(sat1), len(sat2))
