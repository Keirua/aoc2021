require 'set'

score = 0
lines = []
def rate(common)
	c = common.ord
	if c >= 'a'.ord and c <= 'z'.ord
		return c - 'a'.ord + 1
	elsif c >= 'A'.ord and c <= 'Z'.ord
		return c - 'A'.ord + 27
	end
end

lines = File.open("d3.txt").readlines
lines.map!(&:strip)
part1 = 0
lines.each do |line|
	len = line.length
	left = line[0..len/2-1].split("")
	right = line[len/2..].split("")

	common = (left & right)[0]
	part1 += rate(common)
end

part2=0
lines.each_slice(3) do |l1, l2, l3|
	l1 = l1.split("")
	l2 = l2.split("")
	l3 = l3.split("")
	common = (l1&l2&l3)[0]
	part2 += rate(common)
end

part2b=0
lines.each_slice(3) do |l|
	l.map! { |k| k.split("") }
	common = l.reduce(&:intersection	)
	part2b += rate(common[0])
end

puts part1
puts part2
puts part2b