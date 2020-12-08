input = split(strip(read(open("input.txt"), String), '\n'), '\n')

function run(program)
	ac = 0
	pc = 1

	while program[pc] != ""
		instruction = split(program[pc], ' ')[1]
		value = parse(Int, split(program[pc], ' ')[2])
		program[pc] = ""
		if instruction == "acc"
			ac += value
			pc += 1
		elseif instruction == "jmp"
			pc += value
		else
			pc += 1
		end

		if pc == length(program) + 1
			return (ac, true)
		end

	end
	return (ac, false)
end

function p2(program)
	for i in 1:length(program)
		if occursin("jmp", program[i])
			program2 = copy(program)
			program2[i] = replace(program2[i], "jmp"=>"nop")
			result = run(program2)
			if result[2] == true
				return result[1]
			end
		elseif occursin("nop", program[i])
			program2 = copy(program)
			program2[i] = replace(program2[i], "nop"=>"jmp")
			result = run(program2)
			if result[2] == true
				return result[1]
			end
		end
	end
end

println(run(copy(input))[1])
println(p2(input))
