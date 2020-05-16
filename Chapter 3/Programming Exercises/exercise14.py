# exercise14.py
#       Write a program that finds the average of a series of numbers entered by the user. As in the previous
#   problem, the program will first ask the user how many numbers there are. Note: The average should always be
#   a float, even if the user inputs are all ints.

def main():
    print("This program finds the average of a series of numbers.\n")

    numNums = eval(input("Enter the number of numbers to be averaged: "))

    sum = 0
    for i in range(numNums):
        num = eval(input("Enter a number: "))
        sum += num
    average = sum / numNums

    print("The average of the given numbers is", average)

main()
