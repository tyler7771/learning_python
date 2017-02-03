# Dice Rolling Simulator
#
# The Goal: Like the title suggests, this project involves writing a
# program that simulates rolling dice. When the program runs, it will
# randomly choose a number between 1 and 6. (Or whatever other integer you
# prefer the number of sides on the die is up to you.) The program will
# print what that number is. It should then ask you if youd like to roll
# again. For this project, youll need to set the min and max number that
# your dice can produce. For the average die, that means a minimum of 1
# and a maximum of 6. Youll also want a function that randomly grabs a
# number within that range and prints it.

from random import randint

def dice_rolling():
    dice_sides = raw_input("How many sides to the die? ")
    print randint(1,int(dice_sides))
    print ""
    rerole = raw_input("Do you want to roll again? (y/n) ")

    if rerole == "y":
        dice_rolling()

# print dice_rolling()

# 2. Guess the Number
#
# The Goal: Similar to the first project, this project also uses the
# random module in Python. The program will first randomly generate a
# number unknown to the user. The user needs to guess what that number is.
# (In other words, the user needs to be able to input information.) If the
# users guess is wrong, the program should return some sort of indication
# as to how wrong (e.g. The number is too high or too low). If the user
# guesses correctly, a positive indication should appear. Youll need
# functions to check if the user input is an actual number, to see the
# difference between the inputted number and the randomly generated numbers,
# and to then compare the numbers.

def guess_the_number():
    number = randint(0,101)
    tries = 0

    while correct == False:
        guess = raw_input("Guess a number between 1 and 100! ")

        if int(guess) < number:
            print "%s is less than the correct number!" % guess
            tries += 1
        elif int(guess) > number:
            print "%s is greater than the correct number!" % guess
            tries += 1
        elif int(guess) == number:
            correct = True
            tries += 1

    print "The number was %s and was guessed in %s guesses." % (number, tries)

print guess_the_number()
