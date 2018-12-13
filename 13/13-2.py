import sys
g = []
c = []

# 0 = up
# 1 = down
# 2 = left
# 3 = right

# x, y, dir, turn_state

with open("13.txt") as f:
    for line in f:
        l = []
        li = line.strip('\n')
        for char in li:
            l.append(char)
        g.append(l)

for y in range(len(g)):
    for x in range(len(g[y])):
        if g[y][x] == '<':
            c.append([y, x, 2, 0, 0])
            g[y][x] = '-'
        elif g[y][x] == '>':
            c.append([y, x, 3, 0, 0])
            g[y][x] = '-'
        elif g[y][x] == 'v':
            c.append([y, x, 1, 0, 0])
            g[y][x] = '|'
        elif g[y][x] == '^':
            c.append([y, x, 0, 0, 0])
            g[y][x] = '|'

alive = sum(1 for cart in c if cart[4] == 0)

while alive > 1:
    for cart in c:

        if cart[4] == 1:
            continue

        #UP, DOWN, LEFT, AND RIGHT
        if g[cart[0]][cart[1]] == '-':
            if cart[2] == 2: cart[1] -= 1
            elif cart[2] == 3: cart[1] += 1
            else:
                print("LR ERROR")
                sys.exit(1)
        elif g[cart[0]][cart[1]] == '|':
            if cart[2] == 0: cart[0] -= 1
            elif cart[2] == 1: cart[0] += 1
            else:
                print("UD ERROR")
                sys.exit(1)

        #TURNING
        elif g[cart[0]][cart[1]] == '/':
            # UP -> RIGHT
            if cart[2] == 0:
                cart[1] += 1
                cart[2] = 3
            # LEFT -> DOWN
            elif cart[2] == 2:
                cart[0] += 1
                cart[2] = 1
            # DOWN -> LEFT
            elif cart[2] == 1:
                cart[1] -= 1
                cart[2] = 2
            # RIGHT -> UP
            elif cart[2] == 3:
                cart[0] -= 1
                cart[2] = 0
            else:
                print("/ ERROR")
                sys.exit(1)
        elif g[cart[0]][cart[1]] == '\\':
            # UP -> LEFT
            if cart[2] == 0:
                cart[1] -= 1
                cart[2] = 2
            # LEFT -> UP
            elif cart[2] == 2:
                cart[0] -= 1
                cart[2] = 0
            # DOWN -> RIGHT
            elif cart[2] == 1:
                cart[1] += 1
                cart[2] = 3
            # RIGHT -> DOWN
            elif cart[2] == 3:
                cart[0] += 1
                cart[2] = 1
            else: 
                print("\ ERROR")
                sys.exit(1)

        #JUNCTIONS
        elif g[cart[0]][cart[1]] == '+':
            #END UP GOING UP
            if (cart[2] == 0 and cart[3] == 1) or (cart[2] == 2 and cart[3] == 2) or (cart[2] == 3 and cart[3] == 0):
                cart[0] -= 1
                cart[2] = 0
            #END UP GOING DOWN
            elif (cart[2] == 1 and cart[3] == 1) or (cart[2] == 2 and cart[3] == 0) or (cart[2] == 3 and cart[3] == 2):
                cart[0] += 1
                cart[2] = 1
            #END UP GOING LEFT
            elif (cart[2] == 0 and cart[3] == 0) or (cart[2] == 1 and cart[3] == 2) or (cart[2] == 2 and cart[3] == 1):
                cart[1] -= 1
                cart[2] = 2
            #END UP GOING RIGHT
            elif (cart[2] == 0 and cart[3] == 2) or (cart[2] == 1 and cart[3] == 0) or (cart[2] == 3 and cart[3] == 1):
                cart[1] += 1
                cart[2] = 3
            else: 
                print("JUNCTION ERROR")
                sys.exit(1)
            cart[3] = (cart[3] + 1) % 3
        else: 
            print("TILE ERROR")
            sys.exit(1)
        
        for a in c:
            if a is not cart and a[0] == cart[0] and a[1] == cart[1] and a[4] == 0:
                    crash = True
                    print("Crash", a[1], a[0])
                    a[4] = 1
                    cart[4] = 1

    c.sort()
    alive = sum(1 for cart in c if cart[4] == 0)

print("=============================")
for cart in c:
    if cart[4] == 0: print(cart[1], cart[0])
#print("=============================")
#for y in range(len(g)):
#    line = ""
#    for x in range(len(g[y])):
#        iscart = False
#        for cart in c:
#            if cart[0] == y and cart[1] == x:
#                iscart = True
#                if cart[2] == 0: line += "^"
#                elif cart[2] == 1: line += "v"
#                elif cart[2] == 2: line += "<"
#                elif cart[2] == 3: line += ">"
#        if not iscart:
#            line += g[y][x]
#    print(line)
