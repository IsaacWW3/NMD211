# File: isaacWorcester_midterm.py
# Author: Isaac Worcester
# Date: 10/30/2024
# Section: 1
# E-mail: isaac.worcester@maine.edu
# Description:
# This program creates a dictionary that stores keys of the days and a list of values for the topic of the day. It then randomly
# selects the topic from the list. It uses a loop to do this for ever week, printing out the result for the weeks and days
# Collaboration:
# No one
import random

def listOfTopics():
    weekdays = {} # create the weekdays dictionary
    for i in range(7): # loops for 7 days
        dayOfWeek = input("Enter the day of the week: ") # input for the day of the week
       
        # this fills out the dictionary with the days of the week being the key and the input being a list of values
        weekdays[dayOfWeek] = input(f"Enter at least 4 content ideas for {dayOfWeek} seperated by commas: ").split(",")
    return weekdays # return the dictionary
        

def todaysPostTopic(theTopics, dayOfTheWeek): # this takes both the dictionary and the day of the week as an input
    TopicPick = random.choice(theTopics[dayOfTheWeek]) # this picks the topic from the dictionary list for that specific day
    return TopicPick # returns the picked topic

def monthPostTopic():
    topics = listOfTopics() # gets the dictionary generated from list of topics, and the day of the week
    
    weekIterator = 1 # week iterator intialized at 1
    
    for i in range(4): # loops 4 times for four weeks
        print(f"Week {weekIterator}: ") # prints the top of the string for formatting
        
        for day in topics: # for day in weekdays dictionary
            todaysPost = todaysPostTopic(topics, day) # this picks the topic and assigns it to todays post
            print(f"{day} Posting: {todaysPost}") # this prints out the day and the post for that day
        weekIterator  += 1 # incriment iterator for the week

monthPostTopic()