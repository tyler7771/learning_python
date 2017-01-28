# Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime.
#
# Difficulty: medium.

def is_prime(number):
    idx = 2

    while idx <= (number / 2):
        if number % idx == 0:
            return False
        idx += 1

    return True

def nth_prime(number):
    result = []
    idx = 2

    while len(result) < number:
        if is_prime(idx):
            result.append(idx)
        idx += 1

    return result[-1]

print nth_prime(1)
print nth_prime(2)
print nth_prime(3)
print nth_prime(4)
print nth_prime(5)
print nth_prime(6)
