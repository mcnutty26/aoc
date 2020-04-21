input = readlines("input.txt")[1]
array = [parse(Int64, char) for char in input]
offset = sum([array[k]*10^(7-k) for k=1:7])

const BASE = [0, 1, 0, -1]

function pattern(pos, el)
	if pos <= el % 4pos < 2pos
		return 1
	elseif 3pos <= el % 4pos
		return -1
	else
		return 0
	end
end

function fft(array)
	new = zeros(Int64, length(array))
	Threads.@threads for i in 1:length(array)
		new[i] = abs(sum([pattern(i, j) * array[j] for j in 1:length(array)])) % 10
	end
	return new
end

function ffft(array)
	new = zeros(Int64, length(array))
	total = 0
	for i in length(array):-1:1
		total += array[i]
		new[i] = total % 10
	end
	return new
end

function p1(array, iters)
	for _ in 1:iters
		array .= fft(array)
	end
	return array
end

function p2(array, iters)
	for _ in 1:iters
		array .= ffft(array)
	end
	return array
end

println(p1(copy(array), 100)[1:8])
println(p2(repeat(array, 10000)[offset+1:end], 100)[1:8])
