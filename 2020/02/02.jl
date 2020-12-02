using DelimitedFiles
input = readdlm("input.txt", ' ')

count1 = 0
count2 = 0

for i in 1:Int(length(input)/3)
	#seperate out the components
	min, max = map(x->parse(Int, x), split(input[i,1], '-'))
	letter = input[i,2][1]
	password = input[i,3]

	#check part 1
	found = 0
	for char in password
		if char == letter
			found += 1
		end
	end
	if min <= found <= max
		global count1 += 1
	end

	#check part 2
	if (password[min] == letter) ⊻ (password[max] == letter)
		global count2 += 1
	end
end

println(count1)
println(count2)
