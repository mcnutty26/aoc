import sys
from collections import defaultdict

stones = defaultdict(int)

with open(sys.argv[1]) as puzzle:
    for line in puzzle:
        for stone in [int(x) for x in line.rstrip().split(' ')]:
            stones[stone] += 1

def process(stone):
    s = str(stone)
    if stone == 0:
        return [1]
    elif len(s) % 2 == 0:
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    else:
        return [stone * 2024]

for i in range(75):
    newStones = defaultdict(int)
    for k, v in stones.items():
        for x in process(k):
            newStones[x] += v
    stones = newStones.copy()
    if i == 24:
        print(sum([v for v in stones.values()]))

print(sum([v for v in stones.values()]))
