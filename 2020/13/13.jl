using DelimitedFiles

notes = readdlm("input.txt", ',')
start = notes[1][1]
filtered = [x for x in notes if !(x in ["x", "", start])]
busses = [x for x in notes if !(x in ["", start])]

options = []
for bus in filtered push!(options, bus - (start % bus)) end
best = filtered[getindex(options, minimum(options))]
println(best * (best - (start % best)))

function p2(filtered)
	offsets = []
	for x in 1:length(busses)
		if typeof(busses[x]) == Int
			push!(offsets, (busses[x], x-1))
		end
	end
	println(offsets)
	N = prod(filtered)
	return mod(sum((offset * invmod(N ÷ bus, bus) * N) ÷ bus for (bus, offset) in  offsets), N)

end

println(p2(filtered))
