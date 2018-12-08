class node:
    def __init__(self):
        self.children = []
        self.meta = []
with open('8.txt', 'r') as txtfile:
    r = txtfile.readline().strip('\n').split(' ')
r.reverse()
meta_total = 0
def process(data):
    global meta_total
    control = [int(data.pop()), int(data.pop())]
    n = node()
    for c in range(control[0]): n.children.append(process(data))
    for m in range(control[1]):
        n.meta.append(int(data.pop()))
        meta_total += n.meta[-1]
    return n
process(r)
print(meta_total)
