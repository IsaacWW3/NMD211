# File: isaacWorcester_savingPlan.py
# Author: Isaac Worcester
# Date: 9/11/2024
# Section: 1
# E-mail: isaac.worcester@maine.edu
# Description:
# This program takes two inputs, one for the amount wanted to save and one for the amount made per week, this then does some
# calculations to get the amount for the weekly goal, which is used to calculate the weekly save percentage, this program
# also uses a boolean variable and a while loop to make sure the user enters in a positive number
# Collaboration:
# No one

def weekly_savings(): # function delcared with weekly savings name
    bool = False # variable bool set to false to trigger loop
    while bool == False: # while loop with bool staying false
        save_goal = float(input("How much would you like to save over the next 12 months?: ")) # user input for save goal
        if save_goal < 0: # if checking if save goal is greater than 0 prints out error message and restarts loop
            print("Error: Cannot enter number less than 0") 
        else: # if the user input is > 0 then bool is true and loop stops
            bool = True

    bool = False # resuing bool variable and resetting it to false
    while bool == False:    
        weekly_earn = float(input("How much do you make per week?: ")) # user input for the weekly earning
        if weekly_earn < 0: 
            print("Error: Cannot enter number less than 0")
        else:
            bool = True
            

    weekly_goal = save_goal / 52 # calculates the weekly earnign goal by dividing the yearly save goal by 52
    save_percent = (weekly_goal / weekly_earn) * 100 # calculates the weekly save percentage by dividing the weekly goal by the weekly
    # earnings and multiplying it by 100

    # prints out the outputs in a nicely formatted string
    print(f"To make your earns goal of ${save_goal} over the next 12 months, you need to save ${weekly_goal:.2f} a week, which is {save_percent:.2f}% of your weely income")

weekly_savings() # function call