# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
#
# Difficulty: easy.

def palindrome(string):
    idx = 0

    while idx < (len(string) / 2):
        if string[idx] != string[(len(string) - idx) - 1]:
            return False
        else:
            idx += 1

    return True

print palindrome("abc")
print palindrome("abcba")
print palindrome("z")
