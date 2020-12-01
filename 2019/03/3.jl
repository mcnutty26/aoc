f = open("input.txt")
lines = []
for line in readlines(f)
	lines.append(split(line, ','))
end

print(lines[2][2:5])
