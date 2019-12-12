from functools import reduce
from math import gcd

positions = []
velocities = []
step = 1
total = 0
tracking = [set(), set(), set()]
repeat = [0, 0, 0]

with open('input.txt', 'rt') as textfile:
    for line in textfile:
        x, y, z = line.replace('<x=', '').replace(' y=', '').replace(' z=', '').replace('>', '').strip().split(',')
        positions.append([int(x), int(y), int(z)])
        velocities.append([0, 0, 0])

tracking[0].add((positions[0][0], positions[1][0], positions[2][0], velocities[0][0], velocities[1][0], velocities[2][0]))
tracking[1].add((positions[0][1], positions[1][1], positions[2][1], velocities[0][1], velocities[1][1], velocities[2][1]))
tracking[2].add((positions[0][2], positions[1][2], positions[2][2], velocities[0][2], velocities[1][2], velocities[2][2]))

def energy(moon):
    return sum([abs(n) for n in positions[moon]]) * sum([abs(n) for n in velocities[moon]])

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

while min(repeat) == 0:
    for i in range(len(positions)):
        for j in range(i):
            x = (positions[i][0] + positions[j][0]) / 2
            y = (positions[i][1] + positions[j][1]) / 2
            z = (positions[i][2] + positions[j][2]) / 2

            if positions[i][0] > x:
                velocities[i][0] -= 1
            elif positions[i][0] < x:
                velocities[i][0] += 1
            
            if positions[i][1] > y:
                velocities[i][1] -= 1
            elif positions[i][1] < y:
                velocities[i][1] += 1
            
            if positions[i][2] > z:
                velocities[i][2] -= 1
            elif positions[i][2] < z:
                velocities[i][2] += 1
            
            if positions[j][0] > x:
                velocities[j][0] -= 1
            elif positions[j][0] < x:
                velocities[j][0] += 1
            
            if positions[j][1] > y:
                velocities[j][1] -= 1
            elif positions[j][1] < y:
                velocities[j][1] += 1
            
            if positions[j][2] > z:
                velocities[j][2] -= 1
            elif positions[j][2] < z:
                velocities[j][2] += 1

    for i in range(len(positions)):
        positions[i][0] += velocities[i][0]
        positions[i][1] += velocities[i][1]
        positions[i][2] += velocities[i][2]
        
        if step == 1000:
            total += sum([abs(n) for n in positions[i]]) * sum([abs(n) for n in velocities[i]])

    x = (positions[0][0], positions[1][0], positions[2][0], velocities[0][0], velocities[1][0], velocities[2][0])
    y = (positions[0][1], positions[1][1], positions[2][1], velocities[0][1], velocities[1][1], velocities[2][1])
    z = (positions[0][2], positions[1][2], positions[2][2], velocities[0][2], velocities[1][2], velocities[2][2])

    if x not in tracking[0]:
        tracking[0].add(x)
    elif repeat[0] == 0:
        repeat[0] = step
    if y not in tracking[1]:
        tracking[1].add(y)
    elif repeat[1] == 0:
        repeat[1] = step
    if z not in tracking[2]:
        tracking[2].add(z)
    elif repeat[2] == 0:
        repeat[2] = step

    step += 1

print(total)
print(lcm(repeat))
