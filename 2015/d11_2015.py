import aoc

input = aoc.input_as_string(aoc.challenge_filename(11, 2015))

def next_password(p):
    while not is_valid(p):
        p = inc_password(p)
    return p

def next_char(c): return chr(ord(c)+1)

def inc_password(p):
    pos = len(p)-1
    p2 = list(p)
    carry = 1
    while carry == 1:
        if p2[pos] != 'z':
            p2[pos] = next_char(p2[pos])
            carry = 0
        else:
            p2[pos] = 'a'
            pos -= 1
            carry = 1
            if pos < 0:
                raise ValueError("Everything has been exhausted !")

    return "".join(p2)

def has_forbidden(p):
    for c in "iol":
        if c in p:
            return True
    return False

def has_run3(p):
    for i in range(2, len(p)):
        c1, c2, c3 = p[i-2], p[i-1], p[i]
        if c2 == next_char(c1) and c3 == next_char(c2):
            return True
    return False

def has_two_pairs(p):
    for i in range(1, len(p)):
        if p[i-1] == p[i]:
            for j in range(i+2, len(p)):
                if p[j - 1] == p[j] and p[j] != p[i]:
                    return True
    return False

def is_valid(p):
    return has_two_pairs(p) and has_run3(p) and not has_forbidden(p)

assert(has_two_pairs("aabb"))
assert(has_two_pairs("abbeffc"))
assert(not has_two_pairs("aabc"))
assert(has_run3("abc"))
assert(has_run3("abefg"))
assert(has_run3("abecdefz"))
assert(not has_run3("abd"))
assert(inc_password("abc") == "abd")
assert(inc_password("abz") == "aca")
assert(inc_password("azz") == "baa")
assert(is_valid("hijklmmn") == False)
assert(is_valid("abbceffg") == False)
assert(is_valid("abbcegjk") == False)

assert(next_password("abcdefgh") == "abcdffaa")
# assert(next_password("ghijklmn") == "ghjaabcc") # passing, but very slow

print(next_password(input))
# answer is hxbxxyzz, we manually increment to hxbxxzaa which is invalid, and we can ask part 2
print(next_password("hxbxxzaa"))