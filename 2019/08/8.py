import sys
image = [[[]]]
WIDTH = 25
HEIGHT = 6
OUTPUT = [' ', 'X']

with open('input.txt', 'rt') as textfile:
    for line in textfile:
        for char in line.strip():
            if len(image[-1][-1]) == WIDTH and len(image[-1]) == HEIGHT:
               image.append([[]])
            if len(image[-1][-1]) == WIDTH:
                image[-1].append([])
            image[-1][-1].append(int(char))

lo = WIDTH * HEIGHT
layer = 0
ones = 0
twos = 0

for i in range(len(image)):
    acc = 0
    for line in image[i]:
        acc = acc + sum([1 for char in line if char == 0])
    if acc < lo:
        lo = acc
        layer = i

for line in range(len(image[layer])):
    ones += sum([1 for char in image[layer][line] if char == 1])
    twos += sum([1 for char in image[layer][line] if char == 2])

print(ones*twos)

for i in range(HEIGHT):
    line = ""
    for j in range(WIDTH):
        current = 2
        level = 0
        while current == 2:
            current = image[level][i][j]
            level += 1
        line += OUTPUT[current]
    print(line)
