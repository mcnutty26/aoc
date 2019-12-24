# Load the shuffling instructions
ins = []
with open('input.txt', 'rt') as textfile:
    for line in textfile:
        t = 0
        v = 0
        if "deal into" in line:
            t = 0
        elif "cut" in line:
            t= 1
            v = int(line.strip().split()[-1])
        elif "deal with" in line:
            t = 2
            v = int(line.strip().split()[-1])
        ins.append((t, v))

# Part 1
# v1 was with a giant array, but modular arithmetic is much nicer
# shame it doesn't work for part 2!
loc = 2019
SIZE = 10007
for a, b in ins:
    if a == 0:
        loc = SIZE - loc - 1
    elif a == 1:
        loc = (loc - b) % SIZE
    elif a == 2:
        loc = (loc * b) % SIZE

# Easy peasy!
print(loc)

# Part 2 (oh no)
# ngl I copied the algorithm because I don't have a maths degree :S
# I (mostly) understand how it works, but I don't think I could have discovered this in one day
SIZE = 119315717514047
ITERS = 101741582076661

# Represent the deck as an offset/increment pair
# offset is the first card in the deck
# increment is the difference between adjacent cards
offset_diff = 0
increment_mul = 1

#find how the deck changes after one pass of the instructions
for a, b in ins:
    if a == 0:
        # deal into new stack reverses the deck -> reverse the difference between adjacent cards
        increment_mul *= -1
        offset_diff += increment_mul
    elif a == 1:
        # cut moves the first card in the deck along
        offset_diff += increment_mul * b
    elif a == 2:
        # deal with increment somehow :S
        increment_mul *= pow(b, SIZE - 2, SIZE)

# increment always increases by a constant - so just raise it to a power
increment = pow(increment_mul, ITERS, SIZE)

# offset forms a geometric series
offset = offset_diff * (1 - increment) * pow(1 - increment_mul, SIZE - 2, SIZE)

# Not so easy peasy :(
print((offset + increment * 2020) % SIZE)
