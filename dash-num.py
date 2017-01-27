# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#
# Difficulty: medium.

def dasherize_number(num):
    result = ""
    for idx, d in enumerate(str(num)):
        if int(d) % 2 == 1:
            if idx == 0:
                result = "%s-" % d
            elif idx == (len(str(num)) - 1):
                if result[len(result) - 1] != "-":
                    result = "%s-%s" % (result, d)
                else:
                    result = "%s%s" % (result, d)
            else:
                if result[len(result) - 1] != "-":
                    result = "%s-%s" % (result, d)
                else:
                    result = "%s%s-" % (result, d)
        else:
            result = "%s%s" % (result, d)
    return result

print dasherize_number(203)
print dasherize_number(303)
print dasherize_number(333)
print dasherize_number(3223)
