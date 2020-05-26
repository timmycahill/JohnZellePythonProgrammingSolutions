# exercise7.py
#       The Goldbach conjecture asserts that every even number is the sum of two prime numbers. Write a program
#   that gets a number from the user, checks to make sure that it is even, and then finds two prime numbers that
#   add up to the number.

# import isPrime(n) function and getPrimeNumbers(n) functions
import exercise6


################################################
# findPrimePair(n)
#
# This function returns a list containing two
# prime numbers that add up to n.
################################################
def findPrimePair(n):
    # Get list of prime numbers less than or equal to n
    primeNumbers = exercise6.getPrimeNumbers(n)

    for prime1 in primeNumbers:
        i = len(primeNumbers) - 1
        while prime1 + primeNumbers[i] <= n:
            if prime1 + primeNumbers[i] == n:
                return [prime1, primeNumbers[i]]
            i -= 1
    return "There was no prime number pair."

def main():
    # Introduction
    print("This program reads in an even number and returns two prime numbers that add up to it.\n")

    try:
        # Read in number
        n = int(input("Enter an even number: "))

        # Check if n is even
        if n % 2 != 0:
            print("\n{0} is not an even number.".format(n))
        else:
            # Find prime pair
            primePair = findPrimePair(n)
            print("\n{0} and {1} add up to {2}.".format(primePair[0], primePair[1], n))
            
    except ValueError:
        print("\nError: Must enter an integer.")
    except:
        print("\nAn unknown error occured.")

if __name__ == "__main__":
    main()
