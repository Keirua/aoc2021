import numpy as np

# The goal here is to find the last 20 digits of the number of fishes after the 10**100th generation
# https://www.reddit.com/r/adventofcode/comments/ra3f5i/2021_day_6_part_3_day_googol/
modulo_part3 = 10 ** 20


# with U = vector containing [u0, …, u8], we can describe the recurrence relation f like this:
# f_{n+1}(U) = [
#           f_n(u1),
#           f_n(u2),
#           f_n(u3),
#           f_n(u4),
#           f_n(u5),
#           f_n(u6),
#           f_n(u7) + f_n(u0),
#           f_n(u8),
#           f_n(u0)
# ]
# It can be represented in matrix form. This is close to a [permutation matrix](https://en.wikipedia.org/wiki/Permutation_matrix):
#  - all the elements from day n are moved to day n-1, for n>=1
#  - day 0 data are added to day 6 and day 8 (see the first column, the only one with two 1s.)
def get_start_mat():
    return np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=object)

# Then, in order to find the amount of fishes at generation n, we need to :
# - compute A_n = A**n
# - compute U_n = A_n * U
# - compute the sum of the elements of U_n
# Our main problem is to perform a fast matrix exponentiation

# the natural iterative implementation:
# computes mat**n, with mat a matrix
def mat_power(mat, n):
    res = np.identity(9, dtype="int")
    for i in range(n):
        res = np.dot(mat, res)
    return res

## Then we implementation fast matrix exponentiation
def mat_power_fast(matrix, n):
    # inspired from https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
    result = np.identity(9, dtype="int")
    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, matrix)
        matrix = np.dot(matrix, matrix)
        n = n // 2
    return result

## finally, we add the modulo, since all we care about for part3 is the last 20 digits
def mat_power_with_modulo(matrix, n, mod):
    # inspired from https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
    result = np.identity(9, dtype="int")
    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, matrix) % mod
        matrix = np.dot(matrix, matrix) % mod
        n = n // 2
    return result


def part3_googol(mat):
    return mat_power_with_modulo(mat, n=10 ** 100, mod=modulo_part3)


mat18 = mat_power_fast(get_start_mat(), 18)
mat18b = mat_power(get_start_mat(), 18)
mat80 = mat_power_fast(get_start_mat(), 80)
mat256 = mat_power_fast(get_start_mat(), 256)

sample_input = [3, 4, 3, 1, 2]
bc = np.bincount(sample_input, minlength=9)
assert (mat18.dot(bc).sum() == 26)
assert (mat18b.dot(bc).sum() == 26)
assert (mat80.dot(bc).sum() == 5934)
assert (mat256.dot(bc).sum() == 26984457539)

# Now we can
# input as suggested here: https://www.reddit.com/r/adventofcode/comments/ra3f5i/2021_day_6_part_3_day_googol/
input_part3 = [3, 1, 1, 0, 3, 7, 5, 5, 2, 4, 2, 1, 0, 2, 6, 4, 3, 0, 2, 1, 5, 1, 4, 2, 3, 0, 6, 3, 0, 5, 0, 5, 6, 0, 0,
               6, 7, 0, 1, 6, 3, 2, 1, 1, 2, 2, 0, 1, 1, 1, 6, 0, 2, 1, 0, 5, 1, 4, 7, 6, 3, 0, 7, 2, 0, 0, 2, 0, 2, 7,
               3, 7, 2, 4, 6, 1, 6, 6, 1, 1, 6, 3, 3, 1, 0, 4, 5, 0, 5, 1, 2, 0, 2, 0, 7, 4, 6, 1, 6, 1, 5, 0, 0, 2, 3]
bc3 = np.bincount(input_part3, minlength=9)
mat_part3 = part3_googol(get_start_mat())
print(mat_part3.dot(bc3).sum() % modulo_part3)
