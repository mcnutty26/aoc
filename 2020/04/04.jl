input = read(open("input.txt"), String)
documents = split(input, "\n\n")
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

function isvalid(document)
	valid = true
	for field in fields
		valid &= occursin(field, document)
	end
	return valid
end

function p1()
	valid = 0
	for document in documents
		if isvalid(document)
			valid += 1
		end
	end
	return valid
end

function p2()
	count = 0
	byrchk = r"byr:(19[2-9][0-9]|200[0-2])(\s|$)"
	iyrchk = r"iyr:(201[0-9]|2020)(\s|$)"
	eyrchk = r"eyr:(202[0-9]|2030)(\s|$)"
	hgtchk = r"(?<=hgt:)\d{2,3}(cm|in)(?=(\s|$))"
	hclchk = r"hcl:#[0-9a-f]{6}(\s|$)"
	eclchk = r"ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)"
	pidchk = r"pid:\d{9}(\s|$)"
	for document in documents
		if isvalid(document)
			valid = true
			valid &= occursin(byrchk, document)
			valid &= occursin(iyrchk, document)
			valid &= occursin(eyrchk, document)
			
			hgt = match(hgtchk, document)
			if hgt == nothing
				valid = false
			elseif hgt.captures[1] == "cm"
				valid &= 150 <= parse(Int, String(strip(hgt.match, ['c', 'm']))) <= 193
			elseif hgt.captures[1] == "in"
				valid &= 59 <= parse(Int, String(strip(hgt.match, ['i', 'n']))) <= 76
			else
				valid = false
			end
				
			valid &= occursin(hclchk, document)
			valid &= occursin(eclchk, document)
			valid &= occursin(pidchk, document)
			if valid
				count += 1
			end
		end
	end
	return count
end

println(p1())
println(p2())
