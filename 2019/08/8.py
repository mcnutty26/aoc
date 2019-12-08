image = [[[]]]
WIDTH = 25
HEIGHT = 6
OUTPUT = [' ', 'X']

with open('input.txt', 'rt') as textfile:
    for line in textfile:
        for char in line.strip():
            if len(image[-1][-1]) == WIDTH and len(image[-1]) == HEIGHT: # create new layer
               image.append([[]])
            if len(image[-1][-1]) == WIDTH: # create new line
                image[-1].append([])
            image[-1][-1].append(int(char)) # set pixel in last column of last line

lo = WIDTH * HEIGHT
layer = 0
ones = 0
twos = 0

for i in range(len(image)):
    acc = 0
    for line in image[i]:
        acc = acc + sum([1 for char in line if char == 0]) # sum the number of zeros on each line in the layer
    if acc < lo: # this is the new 'best' layer (i.e. fewest zeros)
        lo = acc
        layer = i

for line in range(len(image[layer])):
    ones += sum([1 for char in image[layer][line] if char == 1]) # number of 1s in the layer
    twos += sum([1 for char in image[layer][line] if char == 2]) # number of 2s in the layer

print(ones*twos) # answer for part one

for i in range(HEIGHT):
    line = ""
    for j in range(WIDTH):
        current = 2
        level = 0
        while current == 2: # keep going through the layers until we hit a coloured pixel
            current = image[level][i][j]
            level += 1
        line += OUTPUT[current] # add the pixel to the 'display buffer'
    print(line) # print the 'display buffer' to the screen - answer for part two
