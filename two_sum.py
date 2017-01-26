# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `nil`.
#
# Difficulty: medium.

def two_sum(nums):
    result = []

    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if num1 + num2 == 0 and idx1 != idx2:
                result.append((idx1, idx2))

    if result == []:
        return "nil"
    else:
        return result

print two_sum([1, 3, 5, -3])
print two_sum([1, 3, 5])
