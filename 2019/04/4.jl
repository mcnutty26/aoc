input = 134564:585159

function ascending(n)
	acc = n % 10
	while n > 0
		n ÷= 10
		if n % 10 > acc
			return false
		end
		acc = n % 10
	end
	return true
end

function p1(n)
	acc = n % 10
	double = false
	while n > 0
		n ÷= 10
		if n % 10 > acc
			return false
		end
		if n % 10 == acc
			double = true
		end
		acc = n % 10
	end
	return double
end

function p2(n)
	if !ascending(n)
		return false
	end

	d = digits(n)
	for i in 1:length(d)-3
		if d[i] != d[i+1] && d[i+1] == d[i+2] && d[i+2] != d[i+3]
			return true
		end
	end
	if (d[1] == d[2] != d[3]) || (d[end] == d[end-1] != d[end-2])
		return true
	end
	return false
end

println(sum(p1.(input)))
println(sum(p2.(input)))
