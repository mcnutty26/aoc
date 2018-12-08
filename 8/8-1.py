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
    while control[0] > 0:
        n.children.append(process(data))
        control[0] -= 1
    while control[1] > 0:
        n.meta.append(int(data.pop()))
        meta_total += n.meta[-1]
        control[1] -= 1
    return n
process(r)
print(meta_total)
