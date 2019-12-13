import csv, os, time
from vm import intcode_vm

program = []
display_buffer = dict()
WIDTH = 37
HEIGHT = 20
tiles = [' ', '█', 'O', '-', '@']
tick = 0
ball = 19
paddle = 0
tickrate = 100000


with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

def render(state):
    global display_buffer, ball, paddle
    for i in range(0, len(state), 3):
        display_buffer[(state[i], state[i+1])] = state[i+2]
        if state[i+2] == 3:
            paddle = state[i]
        elif state[i+2] == 4:
            ball = state[i]

    os.system("clear")
    for j in range(HEIGHT):
        line = ''
        for i in range(WIDTH):
            line += tiles[display_buffer.get((i,j), 0)]
        print(line)
    print(f"SCORE: {display_buffer.get((-1, 0), 0)} BLOCKS: {sum([1 for n in display_buffer.values() if n == 2])}")

program[0] = 2
game = intcode_vm(program.copy(), [])

while game.halted is False:
    if tick != tickrate:
        tick += 1
    else:
        tick = 0
        if ball > paddle:
            game.input_queue.append(1)
        elif ball < paddle:
            game.input_queue.append(-1)
        else:
            game.input_queue.append(0)

        render(game.run())
