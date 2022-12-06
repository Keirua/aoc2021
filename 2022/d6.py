def solve(input:str, N:int) -> int:
    for i in range(N, len(input)):
        if len(set(input[i - N:i])) == N:
            return i

input = open("d6.txt").read()
# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
print(solve(input, 4))
print(solve(input, 14))
