import sys
with open(sys.argv[1], "r") as f:
    inp = f.readline().rstrip()
total = [0,0]
for i in range(0, len(inp)-2):
        if inp[i] == inp[i+1]:
            total[0] += int(inp[i])
        if inp[i] == inp[int((i+(len(inp)/2))%len(inp))]:
            total[1] += int(inp[i])
if inp[0] == inp[-1]:
    total[0] += int(inp[0])
if inp[i+1] == inp[int((i+1+(len(inp)/2))%len(inp))]:
    total[1] += int(inp[i+1])
if inp[i+2] == inp[int((i+2+(len(inp)/2))%len(inp))]:
    total[1] += int(inp[i+2])
print(total[0], total[1])
