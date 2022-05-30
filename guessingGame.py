import random

number = random.randint(1,9)
chances = 0

while chances < 5:
    guess = int(input("Enter your Guess :- "))

    if guess == number:
        print("Congratulations , your guess was correct")
    elif guess < number:
        print("Incorrect , try a number higher than "+str(guess))
    else :
        print("Incorrect , try a number lower than "+str(guess))
   
    chances = chances+1
    
if not chances < 5:
    print("You Lost")