class node:
    def __init__(self, num_children, children, num_meta, meta):
        self.num_children = num_children
        self.children = children
        self.num_meta = num_meta
        self.meta = meta
with open('8.txt', 'r') as txtfile:
    r = txtfile.readline().strip('\n').split(' ')
r.reverse()
meta_total = 0
def process(data):
    global meta_total
    n = node(int(data.pop()), [], int(data.pop()), [])
    while n.num_children > 0:
        n.children.append(process(data))
        n.num_children -= 1
    while n.num_meta > 0:
        n.meta.append(int(data.pop()))
        meta_total += n.meta[-1]
        n.num_meta -= 1
    return n
process(r)
print(meta_total)
