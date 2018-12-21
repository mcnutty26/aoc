comesfrom = dict()
stack = []
loc = (0,0)
d = dict({'N':[0,1], 'E': [1,0], 'S': [0,-1], 'W': [-1,0]})
processed = []
raw = ""
points = set()

def explore(regex):
    global loc

    while len(regex):
        c = regex.pop(0)
        if c == '(':
            stack.append(loc)

        elif c == ')':
            stack.pop()

        elif c == '|':
            loc = stack[-1]

        else:
            nloc = (loc[0] + d[c][0], loc[1] + d[c][1])
            if nloc not in comesfrom:
                comesfrom[nloc] = loc
                points.add(nloc)
            loc = nloc

def chart(l):
    i = 0
    x = l[0]
    y = l[1]
    while x != 0 or y != 0:
        i += 1
        x,y = comesfrom[(x,y)]
    return i

with open("20.txt") as f:
    raw = f.readline().strip('\n')
for char in raw:
    processed.append(char)

counter = 0
explore(processed[1:-1])
print(max(chart(x) for x in points))
print(sum(1 for x in points if chart(x) >= 1000))
