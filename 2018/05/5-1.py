with open('5.txt', 'r') as r: raw = r.readline().strip('\n')
def reacts(a,b):
    return (a.lower() == b.lower()) and (a.isupper() != b.isupper())
oldpolymer = []
newpolymer = list(raw)
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
print(len(newpolymer))
