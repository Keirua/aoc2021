import pprint as pp

operations = open(f"d17.txt").read().strip()

flat_h = ["####"]
cross = [".#.","###",".#."]
reverse_l = ["..#", "..#", "###"]
flat_v = ["#", "#", "#", "#"]
square = ["##", "##"]
shapes = [flat_h, cross, reverse_l, flat_v, square]

print(operations)
