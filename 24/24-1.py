import sys

DEBUG = False

if len(sys.argv) < 2:
    BOOST = 0
else:
    BOOST = int(sys.argv[1])

class Army:
    def __init__(self, goodies, units, hp, weak, immune, dmg, dmg_type, init, hash_val, ID):
        self.goodies = goodies
        self.units = units
        self.hp = hp
        self.weak = weak
        self.immune = immune
        self.dmg = dmg
        if self.goodies:
            self.dmg += BOOST
        self.dmg_type = dmg_type
        self.init = init
        self.hash_val = hash_val
        self.ID = ID

    def damage(self, amount):
        lost = 0
        while amount >= self.hp:
            if self.units > 0:
                self.units -= 1
                lost += 1
            amount -= self.hp
        return lost
    
    def eff_pwr(self):
        return self.dmg * self.units
    
    def __str__(self):
        return f"{self.ID} at {self.hp}/{self.units} units ({self.units*self.dmg}) at init {self.init}"
    
    def __lt__(self, other):
        if self.eff_pwr() != other.eff_pwr():
            return self.eff_pwr() < other.eff_pwr()
        return self.init < other.init
    
    def fight(self, other, silent=False):
        dmg = 0
        if self.dmg_type not in other.immune:
            dmg = self.eff_pwr()
        if self.dmg_type in other.weak:
            dmg *= 2
        if not silent and DEBUG: print(f"{self.ID} would deal {other.ID} {dmg} damage at init {self.init}")
        return dmg
    
    def __hash__(self):
        return self.hash_val

def get_init(army):
    return army.init

armies = []
with open("24.txt") as f:
    team = None
    counter = 0
    cIS = 1
    cI = 1
    for line in f:
        l = line.strip('\n')
        if l == "Immune System:":
            team = True
        elif l == "Infection:":
            team = False
        else:
            li = l.split(' ')
            units = int(li[0])
            hp = int(li[4])
            dmg = int(li[-6])
            dmg_t = li[-5]
            init = int(li[-1])
            for i in range(7):
                li.pop(0)
            for i in range(11):
                li.pop()
            weak = None
            we = []
            im = []
            for item in li:
                item = item.strip('(')
                item = item.strip(')')
                item = item.strip(',')
                item = item.strip(';')
                if item == "immune":
                    weak = False
                elif item == "weak":
                    weak = True
                elif item == "to":
                    pass
                else:
                    if weak:
                        we.append(item)
                    else:
                        im.append(item)
            ID = ""
            if team:
                ID = f"Immune System {cIS}"
                cIS += 1
            else:
                ID = f"Infection {cI}"
                cI += 1
            armies.append(Army(team, units, hp, we, im, dmg, dmg_t, init, counter, ID))
            counter += 1

while sum(a.units for a in armies if a.goodies) > 0 and sum(a.units for a in armies if not a.goodies) > 0:
    kills = 0
    armies = sorted(armies, key=lambda u: (-u.eff_pwr(), -u.init))

    if DEBUG:
        for a in armies:
            if a.units > 0:
                print(a, a.weak, a.immune)
    
    target = dict()
    for army in armies:
        if army.units > 0:
            for army_ in armies:
                if army_ not in target.values() and army.goodies is not army_.goodies and army_.units > 0  and army.fight(army_, silent=True) > 0:
                    m = max(army.fight(b, silent=True) for b in armies if b.goodies is not army.goodies and b.units > 0 and b not in target.values())
                    if army.fight(army_, silent=True) == m:
                        target[army] = army_
                        if DEBUG: print("T", army, "targeting", army_)
                        break
   
    if DEBUG: print()

    armies.sort(key=get_init, reverse=True)
    for army in armies:
        if army.units > 0 and army in target:
            lost = target[army].damage(army.fight(target[army], silent=True))
            kills += lost
            if DEBUG: print("F", army, "fighting", target[army], "killing", lost, "units")
    
    if DEBUG: print()
    if DEBUG: print(sum(a.units for a in armies if a.goodies and a.units > 0))
    if kills == 0: break


if kills > 0:
    print(f"Immune: {sum(a.units for a in armies if a.goodies and a.units > 0)}")
    print(f"Infection: {sum(a.units for a in armies if not a.goodies and a.units > 0)}")
else: print("Battle was a draw")

if DEBUG: 
    print(max(a.units for a in armies if a.goodies), max(a.units for a in armies if not a.goodies))
    for a in armies:
        if a.units > 0:
            print(a)
