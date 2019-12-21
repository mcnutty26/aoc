from math import ceil
from collections import defaultdict

productions = {}
produced = {}
GOAL = 1000000000000

with open('input.txt', 'rt') as textfile:
    for line in textfile:
        csv = line.replace('=>', ',')
        items = csv.split(',')
        product = items.pop().strip().split(' ')
        reactants = []
        for item in items:
            temp = item.strip().split(' ')
            reactants.append((temp[1], int(temp[0])))
        productions[product[1]] = reactants
        produced[product[1]] = int(product[0])

def make(compound: str, quantity: int) -> int:
    ore = 0
    stack = [(compound, quantity)]
    extra = defaultdict(int)

    while len(stack) > 0:
        a, b = stack.pop(0)
        current = [a, b]

        if current[0] == "ORE":
            ore += current[1]
            continue
           
        # if we have some extra left over, use it now
        if extra[current[0]] >= current[1]:
            extra[current[0]] -= current[1]
            continue
        elif extra[current[0]] > 0:
            current[1] -= extra[current[0]]
            extra[current[0]] = 0

        # we need to do the reaction this many batches
        total = ceil(current[1] / produced[current[0]])
        
        # maybe we made too much
        extra[current[0]] = max(0, (produced[current[0]] * total) - current[1])

        # order the ingredients
        for req in productions[current[0]]:
            stack.append((req[0], total * req[1]))

    return ore

print(make("FUEL", 1))

low = 1
high = GOAL
guess = None

while low <= high:
    guess = ceil((low + high) / 2)
    n = make("FUEL", guess)
    if n > GOAL:
        high = guess - 1
    else:
        low = guess + 1

print(guess)
