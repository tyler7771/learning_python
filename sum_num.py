# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
#
# Difficulty: easy.

def sum_nums(num):
    result = 0
    idx = 0

    while idx <= num:
        result += idx
        idx += 1

    return result

print sum_nums(1)
print sum_nums(2)
print sum_nums(3)
print sum_nums(4)
print sum_nums(5)
