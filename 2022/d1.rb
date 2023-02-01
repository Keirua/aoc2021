all = []
curr = 0
File.open("d1.txt").readlines.each do |line|
	line = line.strip
	if line != ""
		curr += line.to_i
	else
		all << curr
		curr = 0
	end
end
all = all.sort
part1 = all[-1]
part2 = all[-3..-1].sum
puts part1
puts part2
