import sys
from pathfinding import get_adjacent, get_step

#set ELF_POWER to 3 for part one
ELF_POWER = 33
STARTING_ELVES = 0
DEBUG = False

g = []
c = []

#just to make accessing data about elves and goblins easier
#and less error prone
class creature:
    def __init__(self, y, x, t):
        self.y = y
        self.x = x
        self.type = t
        self.hp = 200
        self.alive = True
    #for reading order we need to sort the list, requiring < and > relations
    def __lt__(self, other):
        if self.y < other.y: return True
        if self.y == other.y and self.x < other.x: return True
        return False
    def __gt__(self, other):
        if self.y > other.y: return True
        if self.y == other.y and self.x > other.x: return True
        return False

#load the grid into memory
with open("15.txt") as f:
    for row in f:
        r = []
        for cell in row:
            r.append(cell)
        g.append(row)

#extract elves and goblins
for y in range(len(g)):
    for x in range(len(g[y])):
        if g[y][x] == 'E':
            c.append(creature(y,x,'E'))
            g[y] = g[y][:x] + '.' + g[y][x+1:]
            STARTING_ELVES += 1
        elif g[y][x] == 'G':
            c.append(creature(y,x,'G'))
            g[y] = g[y][:x] + '.' + g[y][x+1:]

#print the initial grid
if DEBUG:
    for y in range(len(g)):
        l = ""
        for x in range(len(g[y])):
            ischar = False
            for thing in c:
                if thing.y == y and thing.x == x:
                    l += thing.type
                    ischar = True
            if not ischar:
                l += g[y][x]
        print(l)

i = 0
while True:

    #print out how many units need to die before the combat ends (gives you something to watch while it runs)
    if i % 10 == 0: print(min(sum(1 for z in c if z.type=='E' and z.alive), sum(1 for z in c if z.type=='G' and z.alive)))

    #sort creatures into reading order
    c.sort()
    for thing in c:

        #dead things can't move or fight
        if not thing.alive: continue

        #check exit condition
        if sum(1 for thing in c if thing.type == 'E' and thing.alive) == 0 or sum(1 for thing in c if thing.type == 'G' and thing.alive) == 0:
            print("==========")
            survivors = sum(1 for a in c if a.type == 'E' and a.alive)
            if survivors == 0: print("Goblins win")
            else: print(f"Elves win with {STARTING_ELVES - survivors} losses ({ELF_POWER} power)")
            print(i, sum(z.hp for z in c if z.alive), i*sum(z.hp for z in c if z.alive))
            sys.exit(0)
       
        #move if not adjacent to an enemy
        if not get_adjacent(thing, c):
            if DEBUG: print(f"moving as {thing.y}, {thing.x}, {thing.type}")
            path = get_step(thing, g, c)
            thing.y = path[0]
            thing.x = path[1]

        #attack if adjacent to an enemy
        if get_adjacent(thing, c):
            if DEBUG: print(f"fighting as {thing.y}, {thing.x}, {thing.type}")
            
            if thing.type == 'G': get_adjacent(thing, c).hp -= 3
            else: get_adjacent(thing, c).hp -= ELF_POWER
            
            if get_adjacent(thing, c).hp <= 0:
                get_adjacent(thing, c).alive = False

        #make sure we're not going wrong somewhere
        if DEBUG:
            for other in c:
                if thing.y == other.y and thing.x == other.x and thing is not other and other.alive:
                    print("ERROR")
                    print(thing.y, thing.x, thing.type)
                    sys.exit(1)
    i += 1
    
    #print the battlefield after each step
    if DEBUG:
        print("  0123456")
        for y in range(len(g)):
            l = f"{y}|"
            for x in range(len(g[y])):
                ischar = False
                for thing in c:
                    if thing.y == y and thing.x == x and thing.alive:
                        l += thing.type
                        ischar = True
                if not ischar:
                    l += g[y][x]
            print(l)
        print("========================")
