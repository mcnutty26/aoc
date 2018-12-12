s = ""
patterns = dict()
with open("12.txt", 'r') as f:
    s = f.readline().strip('\n')
    xstart = -len(s)
    s = len(s) * '.' + s + len(s) * '.'
    for line in f:
        temp = line.strip('\n').split(',')
        patterns[temp[0]] = temp[1]
for generation in range(20):
    s_ = "." * len(s)
    for i in range(len(s) - 4):
        for p in patterns:
            if s[i:i+5] == p: s_ = s_[:i+2] + patterns[p] + s_[i+3:]
    s = s_
score = 0
for plant in range(len(s)):
    if s[plant] == '#': score += plant + xstart
print(score)

