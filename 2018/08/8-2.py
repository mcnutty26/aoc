class node:
    def __init__(self):
        self.children = []
        self.meta = []
        self.value = 0
with open('8.txt', 'r') as txtfile: r = txtfile.readline().strip('\n').split(' ')
r.reverse()
def process(data):
    control = [int(data.pop()), int(data.pop())]
    n = node()
    for c in range(control[0]):
        n.children.append(process(data))
    for m in range(control[1]):
        n.meta.append(int(data.pop()))
        if n.meta[-1] <= len(n.children): n.value += n.children[n.meta[-1]-1].value
    if len(n.children) == 0: n.value = sum(n.meta)
    return n
print(process(r).value)
