# exercise8.py
#       Solve Programming Exercise 17 from Chapter 3 using a function
#   nextGuess(guess, x) that returns the next guess.

import math

def nextGuess(guess, x):
    return (guess + (x / guess)) / 2

def main():
    print("This program approximates the square root of a given number.\n")

    x = eval(input("Enter a number to find the square root of: "))
    numGuesses = eval(input("Enter the number of guesses to make: "))

    guess = x / 2;
    for i in range(numGuesses):
        guess = nextGuess(guess, x)

    print("The estimated square root of", x, "is", guess)
    difference = abs(math.sqrt(x) - guess)
    print("The estimation is", difference, "away from math.sqrt(x)")


main()
