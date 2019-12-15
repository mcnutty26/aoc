from collections import defaultdict

productions = {}
produced = defaultdict(int)
allocated = defaultdict(int)
quantities = {}
guess = 1
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
        quantities[product[1]] = int(product[0])

def make(compound, quantity):
    # We can always find some more ORE
    if compound == "ORE":
        produced["ORE"] += quantity
        return
    
    # We have all of the ingredients on hand
    elif produced[compound] - allocated[compound] >= quantity:
        return
    
    #We need to manufacture the ingredients
    else:
        while produced[compound] - allocated[compound] < quantity:
            for req in productions[compound]:
                make(req[0], req[1])
                allocated[req[0]] += req[1]
            produced[compound] += quantities[compound]
        return

make("FUEL", 1)
print(produced["ORE"])

while produced["ORE"] < GOAL:
    guess += 1
    make("FUEL", guess)
print(guess - 1)
