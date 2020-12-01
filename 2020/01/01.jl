using DelimitedFiles
input = readdlm("input.txt", Int)

function p1()
	for i in input
		for j in input
			if i + j == 2020
				return i * j
			end
		end
	end
end

function p2()
	for i in input
		if i < 2020
			for j in input
				if i + j < 2020
					for k in input
						if i + j + k == 2020
							return i * j * k
						end
					end
				end
			end
		end
	end
end

println(p1())
println(p2())
