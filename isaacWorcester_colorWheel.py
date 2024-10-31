# File: isaacWorcester_colorWheel.py
# Author: Isaac Worcester
# Date: 9/18/2024
# Section: 1
# E-mail: isaac.worcester@maine.edu
# Description:
# This program takes two inputs for color, and then evaluates them to see if they are equal. if not then it moves on to the alteranitve
# and evaluates through multiple if/elif/else chains to see if they are specific color matches. when it finds a match it tells the
# resulting color and prompts the user for a third color if they so choose, which then tells them the resulting tertiary color
# if the user enters an invalid input, the program will take the inputs and then let the user know they have entered an invalid input
# Collaboration:
# No one


color1 = input("Enter a primary color: ") # input for color 1
color2 = input("Enter a second primary color: ") # input for color 2

# makes the inputs lowercase so user can use capital letters and get same result and checks if they are equal
if color1.lower() == color2.lower(): 
    print(f"You've entered the same color twice, your color is {color1}")
else: # checks if it is literally anything other than equal
    # the below checks if color1 is red OR yellow, and if color2 is yellow OR red, that way the user can enter the color
    # in either order and get the same result
    if (color1.lower() == 'red' or color1.lower() == 'yellow') and (color2.lower() == 'yellow' or color2.lower() =='red'):
        print("Your color is orange")
        # new variable to ask if user would like to enter a third color with y or n answer (variable will be reused)
        thirdColorAnswer = input("Would you like to enter a third color? (y/n): ")
        if thirdColorAnswer.lower() == 'y':
            # if yes, takes new input for color 3
            color3 = input("Enter another primary color: ")
            # if the third color is yellow, you get amber
            if color3.lower() == 'yellow':
                print("Your color is amber")
            # if third color is red, you get vermillion
            elif color3.lower() == 'red':
                print("Your color is vermillion")
            # literally anything else results in brown
            else:
                print("Your color is brown")
        # if user enters anything other than yes, just terminate the program
        else:
            print("You have terminated the program")
    # After this point, I have no comments as it is the same code just different color combinations
    elif (color1.lower() == 'red' or color1.lower() == 'blue') and (color2.lower() == 'blue' or color2.lower() == 'red'):
        print("Your color is purple")
        thirdColorAnswer = input("Would you like to enter a third color? (y/n): ")
        if thirdColorAnswer.lower() == 'y':
            color3 = input("Enter another primary color: ")
            if color3.lower() == 'blue':
                print("Your color is violet")
            elif color3.lower() == 'red':
                print("Your color is magenta")
            else:
                print("Your color is brown")
        else:
            print("You have terminated the program")
    elif (color1.lower() == 'blue' or color1.lower() == 'yellow') and (color2.lower() == 'yellow' or color2.lower() == 'blue'):
        print("Your color is green")
        thirdColorAnswer = input("Would you like to enter a third color? (y/n): ")
        if thirdColorAnswer.lower() == 'y':
            color3 = input("Enter another primary color: ")
            if color3.lower() == 'yellow':
                print("Your color is chartreuse")
            elif color3.lower() == 'blue':
                print("Your color is teal")
            else:
                print("Your color is brown")
        else:
            print("You have terminated the program.")
    # this else is for if the user does not enter any valid color combination
    else:
        print("Error: Please enter valid color combination")
                