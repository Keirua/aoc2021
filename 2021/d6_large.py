import numpy as np
# with U = vector containing [u0, …, u8], we can describe the recurrence relation like this:
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
#  - day 0 data are added to day 6 and day 8 (see column 1)
mat = np.array([[0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,1,0,0],
                [1,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0]], dtype=object)

sample_input = [3,4,3,1,2]
bc = np.bincount(sample_input, minlength=9)

def step_iterative(mat, n):
    tmp = np.identity(9, dtype="int")
    # we loop to n-1 because we do not start from the identity
    for i in range(n):
        tmp = np.dot(mat, tmp)
    return tmp

def step_fast(matrix, n):
    # inspired from https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
    res = np.identity(9, dtype="int")
    while n > 0:
        if n % 2 == 1:
            res = np.dot(res, matrix)
        matrix = np.dot(matrix, matrix)
        n = n//2
    return res

mat_after = step_fast(mat, 18)
print(mat)
print(mat_after)
print(mat.dot(bc).sum())
# population_count = sum(bc.dot([i for i in range(len(bc))])
