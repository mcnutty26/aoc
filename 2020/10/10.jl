using LightGraphs
adapters = []

# read the input
open("input.txt") do input
	for line in eachline(input)
		push!(adapters, parse(Int, line))
	end

	# add the start and end nodes, and sort the collection
	push!(adapters, 0)
	push!(adapters, maximum(adapters) + 3)
	sort!(adapters)
end

# count the number of 1 and 3 gaps
function p1(a)
	ones = sum([1 for x in 1:length(a)-1 if a[x+1]-a[x] == 1])
	threes = sum([1 for x in 1:length(a)-1 if a[x+1]-a[x] == 3])
	return ones * threes
end

# tree_solve helper function
function three_diff(x)
	return f(y) = (y-x ≤ 3) && (x < y)
end

function tree_solve(a)
	# create a DiGraph to hold our tree
	g = SimpleDiGraph()
	add_vertex!(g)
	
	# start by investigating the root node
	out = [1]

	# we need to keep track of which vertex refers to which adapter
	ref = Dict(1=>a[1])

	# go through the set of leaf nodes and expand them if we can with what can follow next
	while length(out) > 0
		new_out = []
		for node in out
			for option in findall(three_diff(ref[node]), a)
				add_vertex!(g)
				ref[nv(g)] = a[option]
				add_edge!(g, node, nv(g))
				push!(new_out, nv(g))
			end
		end
		out = new_out
	end

	# return all the remaining leaf nodes
	return sum([1 for x in vertices(g) if length(outneighbors(g, x)) == 0])
end

function p2(a)
	# sort the adapters into groups where the largest gap between them is 1
	groups = []
	group = [popfirst!(a)]
	while length(a) > 0
		if a[1] - group[length(group)] == 1
			push!(group, popfirst!(a))
		else
			push!(groups, group)
			group = [popfirst!(a)]
		end
	end

	# run the tree solver on each group and return the product
	return reduce(*, map(tree_solve, groups))
end

println(p1(adapters))
println(p2(adapters))
