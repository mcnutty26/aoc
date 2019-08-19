import sys
from collections import defaultdict
inp = []
with open(sys.argv[1], "r") as f:
    for character in f.readline().rstrip():
            inp.append(character)
class node:
    def __init__(self, content=None, children=[]):
        self.content = content
        self.children = children
    def __repr__(self):
        ret = f"{self.content}("
        for child in self.children:
            ret += str(child)
        return ret + ")"
    def score(self, depth):
        return depth + sum(child.score(depth+1) for child in self.children)

def consume(stream, content):
    global total
    c = []
    while len(stream):
        char = stream.pop(0)
        if content == 'group' and char == '{':
            c.append(consume(stream, 'group'))
        elif content == 'group' and char == '}':
            return node('group', children=c)
        elif content == 'garbage' and char == '!':
            stream.pop(0)
        elif content == 'group' and char == '<':
            consume(stream, 'garbage')
        elif content == 'garbage' and char == '>':
            return node('garbage')
        elif content == 'garbage':
            total += 1
    return c[0]
total = 0
main = consume(inp, 'group')
print(main.score(1), total)
