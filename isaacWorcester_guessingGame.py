# File: isaacWorcester_guessingGame.py
# Author: Isaac Worcester
# Date: 9/23/2024
# Section: 1
# E-mail: isaac.worcester@maine.edu
# Description:
# This code takes multiple inputs for a madlib, and also has a loop with a number guessing game to reveal the last blank. 
# It prints out the variables in a long formatted string to make it easy to read for the user. 
# Collaboration:
# No one

# this code was to test the print statement
###################################
# noun1 = '[noun]'
# adjective1 = '[adjective]'
# noun2 = '[noun]'
# adjective2 = '[adjective]'
# proper_noun= '[proper noun]'
# adjective3 = '[adjective]'
# proper_noun2 = '[proper noun]'
# number = '[number]'
# verb = '[verb]'
#################################


# This takes the inputs, in order of the story for all the madlibbed words
noun1 = input("Enter first noun: ")
adjective1 = input("Enter first adjective: ")
noun2 = input("Enter a second noun: ")
adjective2 = input("Enter a second adjective: ")
proper_noun = input("Enter a proper noun: ")
adjective3 = input("Enter a third adjective:")
proper_noun2 = input("Enter a second proper noun: ")
number = input("Enter a number: ")
verb = input("Enter a verb: ")

# this is a formatted string that prints out the madlib with the missing word
# I used brackets around the guessing words so that when the user reads it they know which words they put in
print(f'''
      What the [{noun1}] did you say about me you [{adjective1}] [{noun2}]? 
      I'll have you know I [{adjective2}] the top of my class in the [{proper_noun}], 
      and I've been involved [{adjective3}] raids on [{proper_noun2}],
      and I have over [{number}] confirmed [{verb}]. You are _____ to me\n''')


guess_num = 0 # set guessnum to 0 to trigger the loop
while guess_num != 7:
    goal_num = 7 # goal num is 7, but is a variable so it can be changed or implemented with random module
    # user input for the guess
    guess_num = int(input("Guess a number to reveal the blank! (Between 1 and 10): "))
    
    if guess_num < goal_num: # checks if guess is less than goal, if it is tell user higher
        print("Higher!")
    elif guess_num > goal_num: # checks if guess is greater than goal, if it is tell user lower
        print("Lower!")
    else: # user guessed number correctly, print everything out
        print("You guessed correctly, here is the full madlib:")
        print(f'''
        What the [{noun1}] did you say about me you [{adjective1}] [{noun2}]? 
        I'll have you know I [{adjective2}] the top of my class in the [{proper_noun}], 
        and I've been involved [{adjective3}] raids on [{proper_noun2}],
        and I have over [{number}] confirmed [{verb}]. You are nothing to me\n''')
        print("Congratulations on completing the game!")