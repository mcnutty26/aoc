input = read(open("input.txt"), String)
forms = split(input, "\n\n")

function p1()
	count = []
	for group in forms
		temp = Set(replace(group, "\n"=>""))
		push!(count, length(temp))
	end
	return sum(count)
end

function p2()
	count = []
	for group in forms
		temp = nothing
		for person in split(rstrip(group), "\n")
			if temp == nothing
				temp = Set(person)
			else
				temp = intersect(temp, Set(person))
			end
		end
		push!(count, length(temp))
	end
	return sum(count)
end

println(p1())
println(p2())
