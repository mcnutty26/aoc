n = []
with open("23.txt") as f:
    for line in f:
        l = []
        for cell in line.split(','): l.append(int(cell))
        n.append(l)
max_r = max(b[3] for b in n)
max_bot = None
for bot in n: 
    if bot[3] == max_r: max_bot = bot
print(sum(1 for bot in n if abs(bot[0] - max_bot[0]) + abs(bot[1] - max_bot[1]) + abs(bot[2] - max_bot[2]) <= max_bot[3]))
