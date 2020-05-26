# exercise8.py
#       The greatest common divisor (GCD) of two values can be computed using Euclid's algorithm. Starting with
#   the values m and n, we repeatedly apply the formula: n, m = m, n % m until m is 0. At that point, n is the
#   GCD of the original m and n. Write a program that finds the GCD of two numbers using this algorithm.

###############################################
# findGCD(m, n)
#
# This function inputs two integers and outputs
# the greatest common divisor between them.
###############################################
def findGCD(m, n):
    while m != 0:
        n, m = m, n % m
    return n

def main():
    # Introduction
    print("This program calculats the greatest common divisor (GCD) for two numbers.\n")

    try:
        # Read in m and n
        m = int(input("Enter the first number: "))
        n = int(input("Enter the second number: "))

        # Calculate GCD
        gcd = findGCD(m, n)

        # Output GCD
        print("\nThe GCD for {0} and {1} is {2}.".format(m, n, gcd))

    except ValueError:
        print("\nError: You must enter an integer.")
    except:
        print("\nAn unknown error has occured.")

if __name__ == "__main__":
    main()
