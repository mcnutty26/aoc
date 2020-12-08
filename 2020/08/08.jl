input = split(strip(read(open("input.txt"), String), '\n'), '\n')

function run(program)
	ac = 0
	pc = 1

	while program[pc] != ""
		# fetch the instruction
		op = split(program[pc], ' ')[1]
		value = parse(Int, split(program[pc], ' ')[2])

		# "mark" the instruction as executed
		program[pc] = ""

		# decode and execute the instruction
		if op == "acc"
			ac += value
			pc += 1
		elseif op == "jmp"
			pc += value
		else
			pc += 1
		end

		# the program completed
		if pc == length(program) + 1
			return (ac, true)
		end

	end

	# the program looped
	return (ac, false)
end

function p2(program)
	# check every line of the program
	for i in 1:length(program)
		# if the line is a jump then try replacing it with a nop
		if occursin("jmp", program[i])
			program2 = copy(program)
			program2[i] = replace(program2[i], "jmp"=>"nop")

			# run it and see if it terminates properly
			result = run(program2)
			if result[2] == true
				return result[1]
			end
		# if the line is a nop then try replacing it with a jump
		elseif occursin("nop", program[i])
			program2 = copy(program)
			program2[i] = replace(program2[i], "nop"=>"jmp")
			
			# run it and see if it terminates properly
			result = run(program2)
			if result[2] == true
				return result[1]
			end
		end
	end
end

println(run(copy(input))[1])
println(p2(input))
