# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
#
# Difficulty: easy.

def time_conversion(minutes):
    hours = 0

    while minutes > 59:
        hours += 1
        minutes -= 60

    if minutes < 10:
        minutes = "0%s" % str(minutes)

    return "%s:%s" % (hours, minutes)

print time_conversion(15)
print time_conversion(150)
print time_conversion(360)
