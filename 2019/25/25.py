import csv, sys
sys.path.append('../13/')
from vm import intcode_vm

program = []

# Read in the intcode program
with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))


# Convert intcode vm output into readable characters
def deasciify(ins: str) -> list:
    out = []
    for char in ins:
        out.append(ord(char))
    out.append(10)
    return out


# Convert readable input into ascii values
def asciify(obs: list) -> str:
    out = ''
    for item in obs:
        out += chr(item)
    return out


# Let's play an interactive text adventure!
print("CHEAT CODE: mutex, festive hat, whirled peas, coin")
print("CHEAT CODE: 16410")
droid = intcode_vm(program, [])
while True:
    print(asciify(droid.run()))
    droid.input_queue += deasciify(input())
