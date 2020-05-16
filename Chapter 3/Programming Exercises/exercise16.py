# exercise16.py
#       A Fibonacci sequence is a sequence of numbers where each successive number is the sum of the previous
#   two. The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13,... Write a program that computes the
#   nth Fibonacci number where n is a value input by the user. For example, if n = 6, then the result is 8.

def main():
    print("This program calculates the nth Fibonacci number.\n")

    n = eval(input("Enter n: "))

    thisFib = 1
    fibOneBack = 1
    fibTwoBack = 1

    for i in range(2, n):
        thisFib = fibOneBack + fibTwoBack
        fibTwoBack = fibOneBack
        fibOneBack = thisFib

    print("The fibonacci number at position", n, "is", thisFib)

main()
