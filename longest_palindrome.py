# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# You may want to use Array's `slice(start_index, length)` method,
# which returns a substring of length `length` starting at index
# `start_index`:
#
#     "abcd".slice(1, 2) == "bc"
#     "abcd".slice(1, 3) == "bcd"
#     "abcd".slice(2, 1) == "c"
#     "abcd".slice(2, 2) == "cd"
#
# Difficulty: hard.

def palindrome(string):
    idx = 0

    while idx < (len(string) / 2):
        if string[idx] != string[(len(string) - idx) - 1]:
            return False
        else:
            idx += 1

    return True

def longest_palindrome(string):


print longest_palindrome("abcbd")
print longest_palindrome("abba")
print longest_palindrome("abcbdeffe")
