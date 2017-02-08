# Write a program which will find all such numbers which are divisible by
# 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on
# a single line.

def divisible_by_seven_not_five (start, end):
    result = []

    for num in range(start, (end + 1)):
        if num % 7 == 0 and num % 5 != 0:
            result.append(num)

    return result

# print divisible_by_seven_not_five(2000, 3200)

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single
# line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(num):
    result = 1

    for num in range(1, (num + 1)):
        result *= num

    return result

# print factorial(8)

# With a given integral number n, write a program to generate a dictionary
# that contains (i, i*i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def range_library(num):
    library = {}

    for num in range(1, (num + 1)):
        library[num] = num * num

    return library

# print range_library(8)

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = raw_input()

    def print_string(self):
        print self.s.upper()

strObj = InputOutString()
strObj.get_string()
strObj.print_string()
