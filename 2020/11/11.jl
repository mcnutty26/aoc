lounge = []
open("input.txt") do input
	for line in eachline(input)
		push!(lounge, collect(line))
	end
end

# returns an array of the characters neighbouring a given point
function neighbours(grid, x, y, easy)
	n = []
	if easy
		if y > 1
			push!(n, grid[y-1][x])
			if x > 1 push!(n, grid[y-1][x-1]) end
			if x < length(grid[1]) push!(n, grid[y-1][x+1]) end
		end
		if y < length(grid)
			push!(n, grid[y+1][x])
			if x > 1 push!(n, grid[y+1][x-1]) end
			if x < length(grid[1]) push!(n, grid[y+1][x+1]) end
		end
		if x > 1 push!(n, grid[y][x-1]) end
		if x < length(grid[1]) push!(n, grid[y][x+1]) end
	else
		if y > 1
			for i in 1:y-1
				if grid[y-i][x] in ['#', 'L'] push!(n, grid[y-i][x]); break end
			end
		end
		if y < length(grid)
			for i in 1:length(grid)-y
				if grid[y+i][x] in ['#', 'L'] push!(n, grid[y+i][x]); break end
			end
		end
		if x > 1
			for i in 1:x-1
				if grid[y][x-i] in ['#', 'L'] push!(n, grid[y][x-i]); break end
			end
		end
		if x < length(grid[1])
			for i in 1:length(grid[1])-x
				if grid[y][x+i] in ['#', 'L'] push!(n, grid[y][x+i]); break end
			end
		end
		if x > 1 && y > 1
			for i in 1:minimum([x-1, y-1])
				if grid[y-i][x-i] in ['#', 'L'] push!(n, grid[y-i][x-i]); break end
			end
		end
		if x > 1 && y < length(grid)
			for i in 1:minimum([x-1, length(grid)-y])
				if grid[y+i][x-i] in ['#', 'L'] push!(n, grid[y+i][x-i]); break end
			end
		end
		if x < length(grid[1]) && y > 1
			for i in 1:minimum([length(grid[1])-x, y-1])
				if grid[y-i][x+i] in ['#', 'L'] push!(n, grid[y-i][x+i]); break end
			end
		end
		if x < length(grid[1]) && y < length(grid)
			for i in 1:minimum([length(grid[1])-x, length(grid)-y])
				if grid[y+i][x+i] in ['#', 'L'] push!(n, grid[y+i][x+i]); break end
			end
		end
	end
	return n
end

# determines if a given point should become #
function grows(grid, x, y, easy)
	if grid[y][x] == 'L'
		if sum([1 for n in neighbours(grid, x, y, easy) if n == '#']) == 0
			return true 
		end
	end
	return false
end

# determines if a given point should become L
function shrinks(grid, x, y, easy)
	limit = easy ? 4 : 5
	if grid[y][x] == '#'
		if sum([1 for n in neighbours(grid, x, y, easy) if n == '#']) ≥ limit return true end
	end
	return false
end

# solves the puzzle for the easy and harder line of sight specifications
function solve(l, easy)
	old = deepcopy(l)
	new = deepcopy(l)
	changes = true
	while changes
		changes = false
		for y in 1:length(old)
			for x in 1:length(old[1])
				if grows(old, x, y, easy) new[y][x] = '#'; changes = true end
				if shrinks(old, x, y, easy) new[y][x] = 'L'; changes = true end
			end
		end
		old = deepcopy(new)
	end
	return reduce(+, [sum([1 for char in line if char == '#']) for line in new])
end

println(solve(deepcopy(lounge), true))
println(solve(deepcopy(lounge), false))

