import sys
layers = dict()
with open(sys.argv[1], "r") as f:
    for line in f:
        layer = int(line.rstrip().split(': ')[0])
        depth = int(line.rstrip().split(': ')[1])
        layers[layer] = {"depth": depth, "position": 1, "down": False}
    end = max(layers.keys()) # final layer

position = -1 # initial position
severity = 0
while position < end:
    position += 1
    if position in layers and layers[position]["position"] == 1:
        severity += position * layers[position]["depth"]
    for layer in layers:
        if layer >= position:
            scanner = layers[layer]
            if scanner["position"] == 1 or scanner["position"] == scanner["depth"]:
                scanner["down"] = not scanner["down"]
            if scanner["position"] < scanner["depth"] and scanner["down"]:
                scanner["position"] += 1
            elif scanner["position"] > 1 and not scanner["down"]:
                scanner["position"] -= 1
print(severity) # part 1

i = 0
done = False
while not done:
    done = True
    for layer in layers:
        if (i+layer) % ((layers[layer]["depth"]*2)-2) == 0:
            done = False
            break
    i += 1
print(i-1) # part 2

