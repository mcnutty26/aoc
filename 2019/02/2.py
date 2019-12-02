import csv
cells = []
with open('input.csv', 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for cell in row:
            cells.append(int(cell))

def run(array):
    index = 0
    while array[index] != 99:

        if array[index+1] >= len(array) or array[index+2] >= len(array) or array[index+3] >= len(array):
            return [-1]

        if array[index] == 1:
            array[array[index+3]] = array[array[index+1]] + array[array[index+2]]
        elif array[index] == 2:
            array[array[index+3]] = array[array[index+1]] * array[array[index+2]]
        index += 4
    return array

part1 = cells.copy()
part1[1] = 12
part1[2] = 2

answer = 0
noun = -1
verb = 0

while answer != 19690720:
    if noun < 99:
        noun += 1
    else:
        noun = 0
        verb += 1

    trial = cells.copy()
    trial[1] = noun
    trial[2] = verb
    answer = run(trial)[0]

print(run(cells)[0], (100*noun)+verb)
