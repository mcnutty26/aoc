using DelimitedFiles

input = readdlm("input.txt", Int)

function p2(n)
    fuel = 0
	while n÷3 -2 > 0
        fuel += n÷3 -2
        n = n÷3 -2
	end
	return fuel
end

println(sum(input .÷ 3 .- 2))
println(sum(p2.(input)))
