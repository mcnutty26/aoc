import math
fuel1 = fuel2 = 0
with open('input.txt', 'rb') as textfile:
    for line in textfile:
        fuel1 += math.floor(float(line) / 3) - 2
        while math.floor(float(line) / 3) - 2 > 0:
            fuel2 += math.floor(float(line) / 3) - 2
            line = math.floor(float(line) / 3) - 2
print(fuel1, fuel2)
