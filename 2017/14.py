import sys
import networkx as nx
inp = []
with open(sys.argv[1], "r") as f:
    inp = f.readline().rstrip()
class node:
    def __init__(self, content):
        self.content = content
        self.next = None
        self.last = None
    def reverse(self):
        temp = self.next
        self.next = self.last
        self.last = temp
class cl_list:
    def __init__(self):
        self.pointer = None
    def to_list(self):
        start = self.pointer
        ret = [self.pointer.content]
        current = self.pointer.next
        while current != start:
            ret.append(current.content)
            current = current.next
        return ret
    def insert(self, content=None):
        if self.pointer is None:
            self.pointer = node(content)
            self.pointer.next = self.pointer
            self.pointer.last = self.pointer
        else:
            new = node(content)
            new.next = self.pointer.next
            new.last = self.pointer
            self.pointer.next = new
            new.next.last = new
            self.move()
    def move(self, iterations=1):
        if self.pointer is not None:
            for i in range(iterations):
                    self.pointer = self.pointer.next
    def reverse(self):
        start = self.pointer
        current = self.pointer.next
        self.pointer.reverse()
        while current != start:
            current.reverse()
            current = current.last
        self.pointer = self.pointer.last.last
skip = 0
jumps = 0
list_len = 256
cll = cl_list()
def knot_inner(lengths):
    global skip, jumps, cll
    for length in lengths:
        rev = []
        start = cll.pointer.last
        jumps += int(length) + skip
        if length == list_len:
            cll.reverse()
        elif int(length) > 0:
            for i in range(int(length)):
                rev.append(cll.pointer)
                cll.move()
            end = cll.pointer
            rev = list(reversed(rev))
            for i in range(1, len(rev)):
                rev[i-1].next = rev[i]
                rev[i].last = rev[i-1]
            start.next = rev[0]
            rev[0].last = start
            end.last = rev[-1]
            rev[-1].next = end
        cll.move(skip)
        skip += 1
def knot(key):
    global skip, jumps, cll
    skip = 0
    jumps = 0
    cll = cl_list()
    for i in range(0,list_len):
        cll.insert(i)
    cll.move()
    for i in range(64):
        knot_inner(key + [17, 31, 73, 47, 23])
    cll.move(list_len - (jumps % list_len))
    sparse_hash = cll.to_list()
    dense_hash = []
    for i in range(0,16):
        total = sparse_hash[i*16]
        for j in range(1,16):
            total = total ^ sparse_hash[(16*i)+j]
        dense_hash.append(format(total, 'b'))
    for i in range(len(dense_hash)):
        while len(dense_hash[i]) < 8:
            dense_hash[i] = '0' + dense_hash[i]
    answer = ""
    for item in dense_hash:
        answer += item
    return answer
def convert(key):
    out = []
    for char in key:
        out.append(ord(char))
    return out

grid = []
total = 0
for i in range(128):
    grid.append(knot(convert(inp + '-' + str(i))))
    total += sum([1 for char in grid[-1] if char == '1'])
print(total)

G = nx.Graph()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '1':
            G.add_node(f"{i},{j}")
            if j > 0 and grid[i][j-1] == '1':
                G.add_edge(f"{i},{j}", f"{i},{j-1}")
            if j < len(grid[i])-1 and grid[i][j+1] == '1':
                G.add_edge(f"{i},{j}", f"{i},{j+1}")
            if i > 0 and grid[i-1][j] == '1':
                G.add_edge(f"{i},{j}", f"{i-1},{j}")
            if i < len(grid)-1 and grid[i+1][j] == '1':
                G.add_edge(f"{i},{j}", f"{i+1},{j}")
print(sum([1 for component in nx.connected_components(G)]))
