# exercise7.py
#       Write a function to compute the nth Fibonacci number. Use your function
#   to solve Programming Exercise 16 from Chapter 3.

def fibonacci(n):
    thisFib = 1
    fibOneBack = 1
    fibTwoBack = 1

    for i in range(2, n):
        thisFib = fibOneBack + fibTwoBack
        fibTwoBack = fibOneBack
        fibOneBack = thisFib

    return thisFib

def main():
    # Introduction
    print("This program calculates the nth Fibonacci number.\n")

    # Get n from the user
    n = eval(input("Enter n: "))

    # Calculate Fibonacci number for n
    fib = fibonacci(n)

    # Output results
    print("The fibonacci number at position", n, "is", fib)

main()
