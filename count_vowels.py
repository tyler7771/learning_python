# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.
# You can treat "y" as a consonant.
#
# Difficulty: easy.

def count_vowels(string):
    count = 0

    for letter in string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            count += 1

    return count

print count_vowels("abcd")
print count_vowels("color")
print count_vowels("colour")
print count_vowels("cecilia")
