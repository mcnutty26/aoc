q = []

# read the input
open("input.txt") do input
	for line in eachline(input)
		push!(q, parse(Int, line))
	end
end

# returns true if the target is the sum of two elements in subq
function isvalid(subq, target)
	for x in subq
		for y in subq
			if x + y == target
				return true
			end
		end
	end
	return false
end

# find the first invalid number
function p1(q)
	validity = [isvalid(q[x-25:x-1], q[x]) for x in 26:length(q)]
	return q[findfirst(isequal(false), validity) + 25]
end

# compute sums of increasing sub-arrays until we find the target
function p2(q, target)
	base = [x for x in q if x < target]
	combined = copy(base)
	len = 0
	while !(target in combined)
		len += 1
		combined = [sum(base[x:x+len]) for x in 1:length(base)-len]
	end
	pos = findfirst(isequal(target), combined)
	return sum(extrema(base[pos:pos+len]))
end

target = p1(q)
println(target)
println(p2(q, target))
