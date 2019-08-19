import sys
inp = []
with open(sys.argv[1], "r") as f:
    for line in f:
        inp.append(line.rstrip())
class program:
    def __init__(self, name, weight, stack):
        self.name = name
        self.weight = weight
        self.stack = stack
    def stack_weight(self):
        if not len(self.stack):
            return self.weight
        else:
            weight = self.weight
            for prog in self.stack:
                weight += find(prog).stack_weight()
            return weight
def find(program):
    global tree
    for node in tree:
        if node.name == program:
            return node
tree = []
for raw in inp:
    tokens = raw.split(' ')
    stack = []
    if len(tokens) > 2:
        for token in tokens[3:]:
            stack.append(token.replace(',', ''))
    tree.append(program(tokens[0], int(tokens[1][1:-1]), stack))
current = tree[0]
while True:
    pre = current
    for node in tree:
        if current.name in node.stack:
            current = node
            break
    if pre == current:
        break
candidate = (0, 0)
for node in tree:
    weights = []
    names = []
    if len(node.stack):
        for p in node.stack:
            weights.append(find(p).stack_weight())
    if len(weights) and max(weights) is not min(weights):
        for w in weights:
            if weights.count(w) == 1:
                outlier = find(node.stack[weights.index(w)])
                target = max(weights) if max(weights) is not w else min(weights)
        if -outlier.stack_weight() < candidate[1]:
            candidate = (outlier.weight + target - outlier.stack_weight(), outlier.stack_weight())
print(current.name, candidate[0])
