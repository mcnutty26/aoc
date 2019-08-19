import sys
inp = int(sys.argv[1])
i = 1

#general
def row(n):
    return ((n-1)*2)+1

#directions
def top(n):
    return (4*pow(n,2))-(9*n)+6

def top_n(n):
    i = 1
    while True:
        half = int((row(i) - 1) / 2)
        if n < top(i) - half:
            return -1
        elif n >= top(i) - half and n <= top(i) + half:
            return i
        i += 1

def top_dist(n):
    if top_n(n) == -1:
        return -1
    y = top_n(n)
    x = n - top(y)
    return top_n(n) + abs(n-top(top_n(n))) - 1

print(top_dist(inp))

# Notes for day 3 part 2:
# the sequence for this part is much more complicated than for part 1
# more detail (and lookup table) available at https://oeis.org/A141481
