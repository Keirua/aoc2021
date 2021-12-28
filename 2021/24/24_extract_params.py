from common24 import extract_parameters

input = open("input/24_2021.txt").read()
occurences = extract_parameters(input)
for oc in occurences:
    print(list(map(int, oc)))