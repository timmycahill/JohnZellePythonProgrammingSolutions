# exercise11.py
#       Write a program to find the sum of the first n natural numbers, where
#   the value of n is provided by the user.

def main():
    print("This program calculates the sum of the first n natural numbers.\n")

    n = eval(input("Enter a value for n: "))

    sum = 0
    for i in range(1, n + 1):
        sum += i

    print("The sum of the first", n, "natural numbers is", sum)

main()
