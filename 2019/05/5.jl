using DelimitedFiles

const raw_program = readdlm("input.csv", ',', Int)
const program = reshape(raw_program, length(raw_program))

function get(p, loc, mode)
	if mode == 0
		return p[p[g+1]+1]
	elseif mode == 1
		return p[l+1]
	end
end

function set(p, l, v)
	p[p[l+1]+1] = v
end

function step(c::Channel, p, input)
	ip = 0

	while true
		op, mode1, mode2 = 0
		ins = digits(p[ip+1])

		
		if op == 1
			set(ip+3, get(ip+1) + get(ip+2))
			ip += 4
		elseif op == 2
			set(ip+3, get(p, ip+1, mode1) * get(p, ip+2, mode2))
			ip += 4
		elseif op == 3
			if length(input) == 0
				break
			end
			set(ip+1, pop!(input))
		elseif op == 4
			put!(c, get(p, ip+1, mode1))
		elseif op == 99
			break
		end
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
