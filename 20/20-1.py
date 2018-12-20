def parse(raw):
    global longest_path
    children = []
    path = []

    while len(raw):
        next_char = raw.pop(0)

        if next_char == '(':
            path.append(parse(raw))

        elif next_char == ')':
            children.append(path)
            return children

        elif next_char == '|':
            children.append(path)
            path = []

        else:
            path.append(next_char)

    return path

def extract(path):
    p = ""
    for item in path:
        if type(item) == type('A'):
            p += item
            print
        else:
            m = ""
            for sub_item in item:
                result = extract(sub_item)
                if len(reduced(result)) > len(m):
                    m = result
            p += m
    return p

def reduced(path):
    while path.count('NS') or path.count('EW') or path.count('SN') or path.count('WE'):
        path = path.replace("NS","")
        path = path.replace("SN","")
        path = path.replace("EW","")
        path = path.replace("WE","")
    return path

raw = ""
with open("20.txt") as f:
    raw = f.readline().strip('\n')

#get rid of ^ and $ characters
raw = list(raw[1:-1])

#parse the tree
longest_path = ""
t = parse(raw)

#find the longest path
c = extract(t)
print(len(reduced(c)))
