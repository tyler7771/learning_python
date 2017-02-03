# Write a Python program to calculate the length of a string

def string_length(str):
    return len(str)

# print string_length("abcd")

# Write a Python program to count the number of characters
# (character frequency) in a string.

def letter_count(str):
    count = {}

    for letter in str:
        keys = count.keys()
        if letter in keys:
            count[letter] += 1
        else:
            count[letter] = 1

    return count

# print letter_count("google.com")

# Write a Python program to get a string made of the first 2 and the
# last 2 chars from a given a string. If the string length is less than 2,
# return instead of the empty string.

def first_and_last(str):
    if len(str) < 2:
        return ""
    else:
        return str[0:2] + str[-2:]

# print first_and_last("w3resource")
# print first_and_last("w3")
# print first_and_last("w")

# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first
# char itself.

def string_replace(str):
    return str[0] + str[1:].replace(str[0], "$")

# print string_replace("restart")

# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

def character_swap(str):
    split = str.split(" ")
    word1 = split[0]
    word2 = split[1]
    split[0] = word2[0:2] + word1[2:]
    split[1] = word1[0:2] + word2[2:]

    return " ".join(split)

# print character_swap("abc xyz")

# Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with
# 'ing' then add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.

def add_an_ending(str):
    if len(str) < 3:
        return str
    elif str[-3:] == "ing":
        return str + "ly"
    else:
        return str + "ing"

# print add_an_ending("abc")
# print add_an_ending("string")
# print add_an_ending("a")

# Write a Python program to remove the nth index character from a nonempty
# string

def remove_nth(str, n):
    if n == 0:
        return str[1:]
    else:
        return str[0:n] + str[(n + 1):]

# print remove_nth("abcdefg", 4)
# print remove_nth("abcdefg", 0)
# print remove_nth("abcdefg", 6)

# Write a Python program to change a given string to a new string where
# the first and last chars have been exchanged.

def string_swap(str):
    return str[0].replace(str[0], str[-1]) + str[1:-1] + str[-1].replace(str[-1], str[0])

# print string_swap("abcd")

# Write a Python program to remove the characters which have odd index
# values of a given string.

def remove_odd_index(str):
    result = ""

    for idx, letter in enumerate(str):
        if idx % 2 == 0:
            result += letter

    return result

# print remove_odd_index("abcdefg")

# Write a Python program to count the occurrences of each word in a given
# sentence.

def word_count(str):
    split = str.split()
    count = {}

    for word in split:
        keys = count.keys()
        if word in keys:
            count[word] += 1
        else:
            count[word] = 1

    return count

# print word_count("the quick brown fox jumps over the lazy dog")


# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form

def sort_string(str):
    split = str.split(", ")
    split.sort()
    return ", ".join(split)

# print sort_string("red, white, black, red, green, black")

# Write a Python function to create the HTML string with tags around the
# word(s).

def html_tags(tag, str):
    return "<%s>%s</%s>" % (tag, str, tag)

# print html_tags("i", "Python")
# print html_tags("div", "Python")
# print html_tags("span", "Python")

# Write a Python function to insert a string in the middle of a string.

def insert_string_middle(str1, str2):
    mid = len(str1) / 2
    return "%s%s%s" % (str1[0:mid], str2, str1[mid:])

# print insert_string_middle('[[]]', 'Python')
# print insert_string_middle('{{}}', 'PHP')

# Write a Python function to get a string made of 4 copies of the last two
# characters of a specified string (length must be at least 2)

def insert_end(str):
    if len(str) < 2:
        return ""
    else:
        return "%s%s%s%s" % (str[-2:], str[-2:], str[-2:], str[-2:])

# print insert_end('Python')
# print insert_end('Exercises')

# Write a Python function to get a string made of its first three
# characters of a specified string. If the length of the string is less
# than 3 then return the original string.

def first_three(str):
    if len(str) < 3:
        return str
    else:
        return str[0:3]

# print first_three('ipy')
# print first_three('python')

# Write a Python function to get the first half of a specified string of
# even length.

def string_first_half(str):
    mid = len(str) / 2
    return str[0:mid]

# print string_first_half('Python')
