f = open('5.txt', 'r')
raw = f.readline().strip('\n')

def reacts(a,b):
    return (a.lower() == b.lower()) and (a.isupper() != b.isupper())

def react(polymer):
    oldpolymer = []
    newpolymer = list(polymer)
    done = False
    while not done:
        i = 0
        done = True
        oldpolymer = newpolymer.copy()
        newpolymer = []
        while i < len(oldpolymer) - 1:
            if reacts(oldpolymer[i], oldpolymer[i+1]):
                done = False
                i += 2
            else:
                newpolymer.append(oldpolymer[i])
                i += 1
        newpolymer.append(oldpolymer[i])
    return list(newpolymer)

reduced = react(raw)
results = dict()
temp = ""
smallest = len(reduced)
for letter in "abcdefghijklmnopqrstuvwxyz":
    temp = ""
    for poly in reduced:
        if poly.lower() != letter:
            temp += poly
    if len(react(temp)) < smallest:
        smallest = len(react(temp))
print(smallest)
