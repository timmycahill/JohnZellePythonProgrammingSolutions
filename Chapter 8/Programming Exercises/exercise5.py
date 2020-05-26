# exercise5.py
#       A positive whole number n > 2 is prime if no number between 2 and sqrt(n) (inclusive) evenly divides n.
#   Write a program that accepts a value of n as input and determines if the value is prime. If n is not prime,
#   your program should quit as soon as it finds a value that evenly divides n.

import math

################################################
# isPrime(n)
#
# This function determines if a number is prime.
# Returns boolean value.
################################################
def isPrime(n):
    div = int(math.sqrt(n))

    while div >= 2 and div <= math.sqrt(n):
        if n % div == 0:
            return False
        div -= 1
    return True

def main():
    # Introduction
    print("This program determines if a number is prime.\n")

    try:
        # Read in number
        n = int(input("Enter a number: "))

        # Determine if n is prime
        prime = isPrime(n)

        # Output results
        if prime:
            print("\n{0} is prime.".format(n))
        else:
            print("\n{0} is not prime.".format(n))
    except ValueError:
        print("Error: Must enter an integer.")
    except:
        print("An unknown error has occured.")
        
        
main()
