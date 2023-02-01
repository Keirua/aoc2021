require 'set'

score = 0
lines = []
def rate(common)
	score = 0
	if common.ord >= 'a'.ord and common.ord <= 'z'.ord
		score += common.ord - 'a'.ord + 1
	elsif common.ord >= 'A'.ord and common.ord <= 'Z'.ord
		score += common.ord - 'A'.ord + 27
	end
	score
end

File.open("d3.txt").readlines.each do |line|
	len = line.length
	left = line[0..len/2-1].split("").to_set
	right = line[len/2..].split("").to_set
	common = (left & right).to_a()[0]
	score += rate(common)
end

puts score