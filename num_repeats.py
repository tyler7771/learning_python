# Write a method that takes in a string and returns the number of
# letters that appear more than once in the string. You may assume
# the string contains only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.
#
# Difficulty: hard.

def num_repeats(string):
    repeated = []

    for idx1, letter1 in enumerate(string):
        for idx2, letter2 in enumerate(string):
            if letter1 == letter2 and idx1 != idx2:
                if letter1 not in repeated:
                    repeated.append(letter1)

    return len(repeated)
    
print num_repeats("abdbc") #1
print num_repeats("aaa") #1
print num_repeats("abab") #2
print num_repeats("cadac") #2
print num_repeats("abcde") #0
