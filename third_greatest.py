# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.
#
# Difficulty: medium.

def third_greatest(nums):
    first = 0
    second = 0
    third = 0

    for number in nums:
        if first == 0 or number > first:
            third = second
            second = first
            first = number
        elif second == 0 or number > second:
            third = second
            second = number
        elif third == 0 or number > third:
            third = number

    return third


print third_greatest([5, 3, 7])
print third_greatest([5, 3, 7, 4])
print third_greatest([2, 3, 7, 4])
