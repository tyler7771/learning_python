# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.
#
# Difficulty: medium.

def greatest_common_factor(number1, number2):
    if number1 < number2:
        num = number1
    else:
        num = number2

    while num > 0:
        if number1 % num == 0 and number2 % num == 0:
            return num
        num -= 1

print greatest_common_factor(3, 9) #3
print greatest_common_factor(16, 24) #8
print greatest_common_factor(3, 5) #1
