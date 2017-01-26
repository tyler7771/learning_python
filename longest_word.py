# Write a method that takes in a string. Return the longest word in
# the string. You may assume that the string contains only letters and
# spaces.
#
# You may use the String `split` method to aid you in your quest.
#
# Difficulty: easy.

def longest_word(sentence):
    sentence_list = sentence.split(" ")
    result = ""

    for word in sentence_list:
        if len(word) > len(result):
            result = word

    return result
    
print longest_word('abcde abc def')
