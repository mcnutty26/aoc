route = []
const dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
open("input.txt") do input
	for line in eachline(input)
		push!(route, line)
	end
end

function mod(x, y)
	while x > y x -=y end
	while x < 1 x += y end
	return x
end

function rot(point, angle)
	x = round(Int, point[1]*cosd(angle) - point[2]*sind(angle))
	y = round(Int, point[2]*cosd(angle) + point[1]*sind(angle))
	return [x, y]
end

function p1(route, dirs)
	position = [0,0]
	heading = 2
	cardinals = ['N', 'E', 'S', 'W']
	for step in route
		magnitude = parse(Int, step[2:length(step)])
		if step[1] == 'F'
			position += magnitude .* dirs[heading]
		elseif step[1] == 'L'
			heading = mod(heading - div(magnitude, 90), 4)
		elseif step[1] == 'R'
			heading = mod(heading + div(magnitude, 90), 4)
		else
			position += magnitude .* dirs[findfirst(isequal(step[1]), cardinals)]
		end
	end
	return sum([abs(x) for x in position])
end

function p2(route, dirs)
	waypoint = [10,-1]
	ship = [0, 0]
	for step in route
		magnitude = parse(Int, step[2:length(step)])
		if step[1] == 'F'
			ship += magnitude .* waypoint
		elseif step[1] == 'L'
			waypoint = rot(waypoint, -magnitude)
		elseif step[1] == 'R'
			waypoint = rot(waypoint, magnitude)
		else
			waypoint += magnitude .* dirs[findfirst(isequal(step[1]), cardinals)]
		end
	end
	return sum([abs(x) for x in ship])
end

println(p1(route, dirs, cardinals))
println(p2(route, dirs, cardinals))
