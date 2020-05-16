# exercise13.py
#       Write a program to sum a series of numbers entered by the user. The
#   program should first prompt the user for how many numbers are to be summed.
#   It should then input each of the numbers and print a total sum.

def main():
    print("This program calculates the sum of a series of numbers.\n")

    numNums = eval(input("How many numbers would you like to add? "))

    sum = 0
    for i in range(numNums):
        num = eval(input("Enter a number to add: "))
        sum += num

    print("The sum of the given numbers is", sum)

main()
