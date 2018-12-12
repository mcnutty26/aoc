s = ""
patterns = dict()
with open("12.txt", 'r') as f:
    s = f.readline().strip('\n')
    xstart = -len(s)
    s = len(s) * '.' + s + 3 * len(s) * '.'
    for line in f:
        temp = line.strip('\n').split(',')
        patterns[temp[0]] = temp[1]
scores = []
for generation in range(200):
    s_ = "." * len(s)
    for i in range(len(s) - 4): s_ = f"{s_[:i+2]}{patterns[s[i:i+5]]}{s_[i+3:]}"
    s = s_
    score = 0
    for plant in range(len(s)): 
        if s[plant] == '#': score += plant + xstart
    scores.append(score)
print(((50000000000 - 200) * (scores[-1]-scores[-2])) + scores[-1])

