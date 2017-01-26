# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.
#
# Difficulty: easy.

def reverse(string):
    idx = 1
    result = ""
    for character in string:
        result += string[len(string) - idx]
        idx += 1
    return result

print reverse("This is crazy")
