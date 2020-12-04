input = readlines(open("input.txt"))

function check(right, down)
	x = 1
	y = 1
	trees = 0
	width = length(input[1])
	while y <= length(input)
		if input[y][x] == '#'
			trees += 1
		end
		x += right
		y += down
		if x > width
			x -= width
		end
	end
	return trees
end

println(check(3, 1))
println(check(1, 1) * check(3, 1) * check(5, 1) * check(7, 1) * check(1, 2))
