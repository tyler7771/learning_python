# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
#
# Difficulty: medium.

def nearby_az(string):
    idx = 0

    while idx < len(string):
        count = 1
        if string[idx] == "a":
            while count <= 3 and (idx + count) < len(string):
                if string[idx + count] == "z":
                    return True
                else:
                    count += 1
            idx += 1
        else:
            idx += 1
    return False

print nearby_az("baz")
print nearby_az("abz")
print nearby_az("abcz")
print nearby_az("a")
print nearby_az("z")
print nearby_az("za")
