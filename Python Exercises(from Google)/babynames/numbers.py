# Henry Yu
# Guess Number between 1 and 9

import sys
import re
import os
import random


def main():
    # if you want to use system arguments 
    args = sys.argv[1:]

    # generate random integer and guess
    target = random.randint(1,9)
    counter = 0
    guess = 0

    while guess != target and guess !="exit":

        # let the user guess
        guess =input("Guess a number from 1 to 9:")

        # exit if guest wants to exit 
        if guess == "exit":
            break

        guess = int(guess)
        
        counter = counter + 1

        # compare guess
        if guess > target:
            print("Your guess of %d was too high" %guess)
        elif guess < target:
            print("Your guess of %d was too low" %guess)
        else:
            print("Your guess of %d was correct" %guess)
            print("You got it on %d tries" %counter)
    

if __name__ == '__main__':
  main()
