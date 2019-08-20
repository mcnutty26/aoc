import sys
inp = []
inp2 = []

#parse input as ints and as chars
with open(sys.argv[1], "r") as f:
    line = f.readline()
    for value in line.rstrip().split(','):
        inp.append(int(value))
    for value in line.rstrip():
        inp2.append(ord(value))

#double-linked list node
class node:
    def __init__(self, content):
        self.content = content
        self.next = None
        self.last = None
    def reverse(self):
        temp = self.next
        self.next = self.last
        self.last = temp

#make a circular double-linked list
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

#setup
skip = 0
jumps = 0
list_len = 256

#main knot function
def knot(lengths):
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

#part 1
cll = cl_list()
for i in range(0,list_len):
    cll.insert(i)
cll.move()
knot(inp)
head = cll.pointer
cll.move(list_len - (jumps % list_len))
print(cll.pointer.content*cll.pointer.next.content)
while cll.pointer != head:
    cll.move()

#part 2
skip = 0
jumps = 0
inp2 += [17, 31, 73, 47, 23]
cll = cl_list()
for i in range(0,list_len):
    cll.insert(i)
cll.move()
for i in range(64):
    knot(inp2)
cll.move(list_len - (jumps % list_len))

#compute the hash from the knotted input
sparse_hash = cll.to_list()
dense_hash = []
for i in range(0,16):
    total = sparse_hash[i*16]
    for j in range(1,16):
        total = total ^ sparse_hash[(16*i)+j]
    dense_hash.append(format(total, 'x'))
for i in range(len(dense_hash)):
    if len(dense_hash[i]) == 1:
        dense_hash[i] = '0' + dense_hash[i]
answer = ""
for item in dense_hash:
    answer += item
print(answer)
