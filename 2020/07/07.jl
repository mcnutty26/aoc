using LightGraphs, SimpleWeightedGraphs

input = split(strip(read(open("input.txt"), String), '\n'), '\n')
g = SimpleWeightedDiGraph(length(input))
types = []

function getorset(item)
	if !(item in types)
		push!(types, item)
	end
	return findfirst(isequal(item), types)
end

for rule in input
	tokens = split(rule, ' ')
	container = reduce(*, tokens[1:2])
	for i in 1:trunc(Int, (length(tokens)/4)-1)
		quantity = parse(Int, tokens[(4*i)+1])
		type = reduce(*,tokens[(4*i)+2:(4*i)+3])
		add_edge!(g, getorset(container), getorset(type), quantity)
	end
end

function p1()
	count = -1
	for type in types
	if has_path(g, getorset(type), getorset("shinygold"))
			count += 1
		end
	end
	return count
end

function p2()
	total = 0
	stack = [(getorset("shinygold"), 1)]
	while length(stack) > 0
		current = pop!(stack)
		for neighbour in neighbors(g, current[1])
			w = g.weights[neighbour, current[1]]
			push!(stack, (neighbour, w*current[2]))
			total += w*current[2]
		end
	end
	return total
end

println(p1())
println(p2())

