using DelimitedFiles

const raw_program = readdlm("input.csv", ',', Int)
const program = reshape(raw_program, length(raw_program))
const TARGET = 19690720

function p1(p, noun, verb)
	ip = 0
	p[2] = noun
	p[3] = verb
	while true
		op = p[ip+1]
		
		if op == 1
			p[p[ip+4]+1] = p[p[ip+2]+1] + p[p[ip+3]+1]
		elseif op == 2
			p[p[ip+4]+1] = p[p[ip+2]+1] * p[p[ip+3]+1]
		elseif op == 99
			break
		end
		ip += 4
	end
	return p[1]
end

function p2(p)
	for i in 0:99
		for j in 0:99
			if p1(copy(p), i, j) == TARGET
				return 100*i + j
			end
		end
	end
end

println(p1(copy(program), 12, 2))
println(p2(program))
