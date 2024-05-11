#Anoushka Saha
#Higher or Lower
#May 11th, 2024
#Day 14 Project

#Import art, accounts, random, and os modules
import random
import art
import accounts
import os

#Display logo
print(art.logo)

#Set score
score = 0

#Random number to pick account A
numA = random.randint(1,50)

while True:
    #Random number to pick account B
    numB = random.randint(1,50)

    #First account
    print("Compare A: " + accounts.data[numA]['name'] + ", a " + accounts.data[numA]['description'] + " from " 
        + accounts.data[numA]['country'])

    #Print vs logo
    print(art.vs)

    #Second account
    print("Against B: " + accounts.data[numB]['name'] + ", a " + accounts.data[numB]['description'] + " from " 
        + accounts.data[numB]['country'])

    #Generate correct answer
    if accounts.data[numA]['follower_count'] > accounts.data[numB]['follower_count']:
        correct_ans = "A"
        numA = numB
    else:
        correct_ans = "B"

    #Ask for user answer:
    user_ans = input("who has more followers? A or B?: ")

    #Check answer
    if user_ans == correct_ans:
        score = score + 1
        print("You're right! Your score is: " + str(score))
        os.system('cls')
    else:
        print("Sorry that's incorrect")
        print("Final score is: " + str(score))
        break