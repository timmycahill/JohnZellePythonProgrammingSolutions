# exercise4.py
#       Write definitions for the following two functions:
#
#   sumN(n): returns the sum of the first n natural numbers.
#
#   sumNCubes(n): returns the sum of the cubes of the first n natural numbers.
#
#       Then use these functions in a program that prompts the user for n and
#   prints out the sum of the first n natural numbers and the sum of the cubes
#   of the first n natural numbers.

def sumN(n):
    total = 0
    for i in range(1, 1+n):
        total += i
    return total

def sumNCubes(n):
    total = 0
    for i in range(1, 1+n):
        total += i ** 3
    return total

def main():
    # Introduction
    print("This program calculates the sum of the first N natural numbers and " +
          "the sum of the cubes of the first N natural numbers.\n")

    # Get N from the user
    n = eval(input("Enter the value for N: "))

    # Calculate sums
    nSum = sumN(n)
    nCubeSum = sumNCubes(n)

    # Output results
    print("Sum of first N natural numbers:", nSum)
    print("Sum of cubes of first N natural numbers:", nCubeSum)

main()
