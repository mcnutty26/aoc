using LightGraphs, SimpleWeightedGraphs

# set up an empty weighted directed graph
input = split(strip(read(open("input.txt"), String), '\n'), '\n')
g = SimpleWeightedDiGraph(length(input))
types = []

# helper function to keep track of suitcase colour IDs
function getorset(item)
	if !(item in types)
		push!(types, item)
	end
	return findfirst(isequal(item), types)
end

# populate the graph with an edge between a suitcase colour and what it contains
for rule in input
	tokens = split(rule, ' ')
	container = reduce(*, tokens[1:2])
	for i in 1:trunc(Int, (length(tokens)/4)-1)
		quantity = parse(Int, tokens[(4*i)+1])
		type = reduce(*,tokens[(4*i)+2:(4*i)+3])
		add_edge!(g, getorset(container), getorset(type), quantity)
	end
end

# count the number of suitcases that have a path to shiny gold suitcases
# digraph means that they must be able to contain a shiny gold suitcase
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

	# start with one shiny gold suitcase
	stack = [(getorset("shinygold"), 1)]
	
	# while there are still suitcases to unpack
	while length(stack) > 0
		# open the current suitcase
		current = pop!(stack)

		# add its contents to the stack
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

