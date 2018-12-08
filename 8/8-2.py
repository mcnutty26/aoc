class node:
    def __init__(self, num_children, children, num_meta, meta, value):
        self.num_children = num_children
        self.children = children
        self.num_meta = num_meta
        self.meta = meta
        self.value = value
with open('8.txt', 'r') as txtfile:
    r = txtfile.readline().strip('\n').split(' ')
r.reverse()
def process(data):
    n = node(int(data.pop()), [], int(data.pop()), [], 0)
    while n.num_children > 0:
        n.children.append(process(data))
        n.num_children -= 1
    while n.num_meta > 0:
        n.meta.append(int(data.pop()))
        n.num_meta -= 1
        if n.meta[-1] <= len(n.children):
            n.value += n.children[n.meta[-1]-1].value
    if len(n.children) == 0:
        n.value = sum(n.meta)
    return n
print(process(r).value)
