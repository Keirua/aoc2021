# First, we convert our naive solution using sets into binary ORs:
def solve_or(input:str, N:int) -> int:
    for i in range(len(input)-N):
        s = 0
        for j in range(N):
            # ord(input[i + j]) - ord('a') => turn a-z into 0-26
            # 1 << (ord(input[i + j]) - ord('a')) = 2 ** (letter position)
            # s |= b0001 -> sets bit 0001 in s
            s |= 1 << (ord(input[i + j]) - ord('a'))
        if bin(s).count("1") == N: # there was no native popcnt in python until 3.10
            return i + N

# but we want to remove the N loop. We use the fact that a ^ b ^ a == b
def solve(input:str, N:int) -> int:
    s = 0
    for i in range(len(input)):
        # Turn on bits as they enter the window
        s ^= 1 << (ord(input[i]) - ord('a'))
        if i >= N:
            # Turn bits off as we leave the window
            s ^= 1 << (ord(input[i - N]) - ord('a'))
        if s.bit_count() == N:
            return i + 1



input = open("d6.txt").read()
# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
print(solve(input, 4))
print(solve(input, 14))
