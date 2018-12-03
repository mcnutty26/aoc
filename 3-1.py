import csv

claims = []

with open('3.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for claim in r:
        claims.append([int(claim[0]), int(claim[1]), int(claim[2]), int(claim[3]), int(claim[4])])

i_ = dict()

for claim in claims:
    icount = 0
    jcount = 0

    while icount < claim[3]:
        while jcount < claim[4]:
            ipos = claim[1] + icount
            jpos = claim[2] + jcount
            if ipos not in i_:
                i_[ipos] = dict()
            if jpos not in i_[ipos]:
                i_[ipos][jpos] = 0
            i_[ipos][jpos] += 1
            jcount += 1
        icount += 1
        jcount = 0

count = 0
for row in i_:
    for cell in i_[row]:
        if i_[row][cell] > 1:
            count += 1

print(count)
