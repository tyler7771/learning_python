# Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.
#
# Difficulty: medium.

def scramble_string(string, positions):
    result = list(string)

    for idx, letter in enumerate(string):
        result[positions[idx]] = letter

    return "".join(result)


print scramble_string("abcd", [3, 1, 2, 0]) #"dbca"
print scramble_string("markov", [5, 2, 4, 1, 3, 0]) #"vkaorm"
