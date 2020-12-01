import math

rocket = open("input.txt")
total = 0

def calculate(mass):
    return math.floor(mass/3)-2

for mass in rocket:
    total += calculate(mass)

print(total)


