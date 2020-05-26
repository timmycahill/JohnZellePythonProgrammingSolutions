# exercise6.py
#       Modify the previous problem to find every prime number less than or equal to n.

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

################################################
# getPrimeNumbers(n)
#
# This function returns a list of all the prime
# numbers less than or equal to n.
################################################
def getPrimeNumbers(n):
    primeNumbers = []

    while n > 1:
        if isPrime(n):
            primeNumbers.append(n)
        n -= 1
    return primeNumbers
    

def main():
    # Introduction
    print("This program determines every prime number less than or equal to 'n'.\n")

    try:
        # Read in number
        n = int(input("Enter a value for n: "))

        # Calculate prime numbers
        primeNumbers = getPrimeNumbers(n)

        # Output results
        if len(primeNumbers) < 1:
            print("\nThere are no prime numbers.")
        else:
            for i in range(len(primeNumbers)):
                primeNumbers[i] = str(primeNumbers[i])
            primeStr = ", ".join(primeNumbers)
            print("\nThe prime numbers less than or equal to {0} are {1}.".format(n, primeStr))
        
    except ValueError:
        print("Error: Must enter an integer.")
    except:
        print("An unknown error has occured.")
        
        
if __name__ == "__main__":
    main()
