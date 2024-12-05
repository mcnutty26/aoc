import sys
from collections import defaultdict

rules = defaultdict(set)
books = []
totals = [0, 0]

with open(sys.argv[1]) as puzzle:
    readRules = True
    for line in puzzle:
        if readRules:
            if line == "\n":
                readRules = False
                continue
            pages = line.rstrip().split('|')
            rules[int(pages[0])].add(int(pages[1]))
        else:
            books.append([int(x) for x in line.rstrip().split(',')])

def subReqs(pages):
    return {k:v.intersection(pages) for k, v in rules.items()}

def reorder(book):
    fixed = []
    while len(fixed) < len(book):
        remaining = set(book) - set(fixed)
        for key, value in subReqs(remaining).items():
            if (key in remaining) and ( value == set()):
                fixed.append(key)
                break
    return fixed

for book in books:
    seen = set()
    correct = True
    for page in book:
        if rules[page].isdisjoint(seen):
            seen.add(page)
        else:
            totals[1] += reorder(book)[(len(book)-1)//2]
            correct = False
            break
    if correct:
        totals[0] += book[(len(book)-1)//2]

print(totals)
