import sys
from math import pow, atan2, pi
asteroids = dict()

with open('input.txt', 'rt') as textfile:
    x = 0
    y = 0
    for line in textfile:
        for char in line.strip():
            if char == '#':
                asteroids[(x,y)] = 0
            x += 1
        x = 0
        y += 1

def angle(a, b): # angle between a and b
    return atan2(b[1] - a[1], b[0] - a[0])

def dist(a, b): # distance between a and b
    return pow(abs(a[0] - b[0]), 2) + pow(abs(a[1] - b[1]), 2)

##########
# PART 1 #
##########
for a in asteroids:
    los = set()
    for b in asteroids:
        if a is b or b in los:
            continue # don't consider asteroids we've already seen, asteroids can't see themselves
        clash = False
        clash_set = dict()
        for c in asteroids: # do any other asteroids lie on the same bearing
            if a is b or a is c or b is c:
                continue
            if angle(a, b) == angle(a, c):
                clash = True
                clash_set[b] = dist(a, b)
                clash_set[c] = dist(a, c)
        if not clash:
            los.add(b) # only asteroid on this bearing, so count it in the total
        else:
            los.add(min(clash_set.items(), key=lambda k: k[1])[0]) # count the closest one
    asteroids[a] = len(los)
print(max(asteroids.values()))

##########
# PART 2 #
##########
station = max(asteroids.items(), key=lambda k: k[1])[0]
for asteroid in asteroids:
    asteroids[asteroid] = angle(station, asteroid)

ang = (-pi / 2) - 0.00001
destroyed = set()
last = None
asteroids_k = [k for k, v in sorted(asteroids.items(), key=lambda item: item[1])] # all asteroid locations
asteroids_v = [v for k, v in sorted(asteroids.items(), key=lambda item: item[1])] # all asteroid bearings with station

while len(destroyed) < 200:
    for i in range(len(asteroids_k)):
        done = True
        if asteroids_v[i] > ang:
            ang = asteroids_v[i]
            choices = []
            for j in range(len(asteroids_v)):
                if asteroids_v[j] == ang:
                    choices.append(asteroids_k[j]) # consider all asteroids on this bearing
            closest = (99999,99999)
            for choice in choices:
                if dist(station, choice) < dist(station, closest) and choice not in destroyed and choice is not station:
                    closest = choice # closest non-destroyed asteroid
            if closest is not (99999,99999):
                destroyed.add(closest) # BOOM!
                done = False
                if len(destroyed) == 200:
                    print((closest[0] * 100) + closest[1]) # print out the 200th one
    if done:
        ang = -4
