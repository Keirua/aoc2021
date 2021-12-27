def check(input):
    z = 0
    if 11 > 0:
        z = z / 1
        z = 26 * z + (input[0]) + 16
    else:
        z = z // 26
        if (z + 11 != input[0]):
            z = 26 * z + input[0] + 16

    if 12 > 0:
        z = z / 1
        z = 26 * z + (input[1]) + 11
    else:
        z = z // 26
        if (z + 12 != input[1]):
            z = 26 * z + input[1] + 11

    if 13 > 0:
        z = z / 1
        z = 26 * z + (input[2]) + 12
    else:
        z = z // 26
        if (z + 13 != input[2]):
            z = 26 * z + input[2] + 12

    if -5 > 0:
        z = z / 1
        z = 26 * z + (input[3]) + 12
    else:
        z = z // 26
        if (z + -5 != input[3]):
            z = 26 * z + input[3] + 12

    if -3 > 0:
        z = z / 1
        z = 26 * z + (input[4]) + 12
    else:
        z = z // 26
        if (z + -3 != input[4]):
            z = 26 * z + input[4] + 12

    if 14 > 0:
        z = z / 1
        z = 26 * z + (input[5]) + 2
    else:
        z = z // 26
        if (z + 14 != input[5]):
            z = 26 * z + input[5] + 2

    if 15 > 0:
        z = z / 1
        z = 26 * z + (input[6]) + 11
    else:
        z = z // 26
        if (z + 15 != input[6]):
            z = 26 * z + input[6] + 11

    if -16 > 0:
        z = z / 1
        z = 26 * z + (input[7]) + 4
    else:
        z = z // 26
        if (z + -16 != input[7]):
            z = 26 * z + input[7] + 4

    if 14 > 0:
        z = z / 1
        z = 26 * z + (input[8]) + 12
    else:
        z = z // 26
        if (z + 14 != input[8]):
            z = 26 * z + input[8] + 12

    if 15 > 0:
        z = z / 1
        z = 26 * z + (input[9]) + 9
    else:
        z = z // 26
        if (z + 15 != input[9]):
            z = 26 * z + input[9] + 9

    if -7 > 0:
        z = z / 1
        z = 26 * z + (input[10]) + 10
    else:
        z = z // 26
        if (z + -7 != input[10]):
            z = 26 * z + input[10] + 10

    if -11 > 0:
        z = z / 1
        z = 26 * z + (input[11]) + 11
    else:
        z = z // 26
        if (z + -11 != input[11]):
            z = 26 * z + input[11] + 11

    if -6 > 0:
        z = z / 1
        z = 26 * z + (input[12]) + 6
    else:
        z = z // 26
        if (z + -6 != input[12]):
            z = 26 * z + input[12] + 6

    if -11 > 0:
        z = z / 1
        z = 26 * z + (input[13]) + 15
    else:
        z = z // 26
        if (z + -11 != input[13]):
            z = 26 * z + input[13] + 15

    return z == 0


# def part1():
#     for i in range(41299994880000, 41199994879959, -1):
#     # for i in range(100000000000000, 10000000000000, -1):
#         v = str(i)
#         if "0" in v:
#             continue
#         if check(list(map(int, v))) == True:
#             return i
#         print(i)
print(check(list(map(int, str(41299994879959)))))