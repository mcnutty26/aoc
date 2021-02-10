ops = []

# parse the input
open("input.txt") do input
	for line in eachline(input)
		if occursin("mask", line)
			push!(ops, (true, collect(line)[8:43]))
		else
			m1 = match(r"(?<=\[).*(?=\])", line)
			m2 = match(r"(?<=\= ).*", line)
			push!(ops, (false, parse(Int, m1.match), parse(Int, m2.match)))
		end
	end
end

function process(mask, value)
	v = digits(value, base=2)
	out = []
	for i in 1:length(mask)
		if mask[i] != 'X'
			push!(out, parse(Int, mask[i]))
		elseif i <= length(v)
			push!(out, v[i])
		else
			push!(out, 0)
		end
	end
	result = 0
	for i in 0:length(out)-1
		result += (2^i)*out[i+1]
	end
	return result
end

function p1(ops)
	mask = []
	memory = Dict()
	for op in ops
		if op[1]
			mask = reverse(op[2])
		else
			memory[op[2]] = process(mask, op[3])
		end
	end
	return sum(values(memory))
end

println(p1(ops))
