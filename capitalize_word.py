# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.
#
# You'll want to use the `split` and `join` methods. Also, the String
# method `upcase`, which converts a string to all upper case will be
# helpful.
#
# Difficulty: medium.

def capitalize_words(string):
    sentence_list = string.split(" ")
    result = ""

    for word in sentence_list:
        result = "%s %s" % (result, word.capitalize())

    return result

print capitalize_words("this is a sentence")
print capitalize_words("mike bloomfield")
