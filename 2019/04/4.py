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
    s = str(n)
    for i in range(len(str(n)) - 3):
        if s[i] != s[i+1] and s[i+1] == s[i+2] and s[i+2] != s[i+3]:
            return True
    if (s[0] == s[1] and s[1] != s[2]) or (s[-1] == s[-2] and s[-2] != s[-3]):
        return True
    return False

for j in range(lo, hi):
    if not asc(j):
        continue
    if adj1(j):
        sat1.append(j)
    if adj2(j):
        sat2.append(j)

print(len(sat1), len(sat2))
