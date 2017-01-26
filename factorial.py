# Write a method that takes an integer `n` in; it should return
# n*(n-1)*(n-2)*...*2*1. Assume n >= 0.
#
# As a special case, `factorial(0) == 1`.
#
# Difficulty: easy.

def factorial(n):
    idx= 0
    result = 1

    while idx < n:
        result *= (n - idx)
        idx += 1

    return result

print factorial(0)
print factorial(1)
print factorial(2)
print factorial(3)
print factorial(4)
