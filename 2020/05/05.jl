using DelimitedFiles
input = readdlm("input.txt")
seats = fill(false, 128, 8)

function p1()
	idmax = 0
	for line in input
		pass = replace(line, "F"=>"0")
		pass = replace(pass, "B"=>"1")
		pass = replace(pass, "L"=>"0")
		pass = replace(pass, "R"=>"1")
		vloc = parse(Int, pass[1:7], base=2)
		hloc = parse(Int, pass[8:10], base=2)
		global seats[vloc+1, hloc+1] = true
		idmax = max(idmax, (vloc*8)+hloc)
	end
	return(idmax)
end

function p2()
	global seats
	for i in 2:127
		for j in 1:8
			if !seats[i, j] && seats[i-1, j]
				return ((i-1)*8)+(j-1)
			end
		end
	end
end

println(p1())
println(p2())
