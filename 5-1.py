f = open('5.txt', 'r')
raw = f.readline().strip('\n')

def reacts(a,b):
    return (ord(a.lower()) is  ord(b.lower())) and (a.isupper() is not b.isupper())

oldpolymer = []
newpolymer = []
for letter in raw:
    newpolymer.append(letter)
done = False
while not done:
    i = 0
    done = True
    oldpolymer = newpolymer.copy()
    newpolymer = []
    while i < len(oldpolymer) - 1:
        if reacts(oldpolymer[i], oldpolymer[i+1]):
            done = False
            #print("removing " + oldpolymer[i] + " " + oldpolymer[i+1])
            i += 2
        else:
            newpolymer.append(oldpolymer[i])
            i += 1
    newpolymer.append(oldpolymer[i])

print(len(newpolymer))
