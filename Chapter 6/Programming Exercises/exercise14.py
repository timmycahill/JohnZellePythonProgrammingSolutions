# exercise14.py
#       Use the functions from the previous three problems to implement a program that computes the sum of the
#   squares of numberse read from a file. Your program should prompt for a file name and print out the sum of
#   the squares of the values in the file. Hint: use readlines()

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    total = 0
    for n in nums:
        total += n
    return total

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])

def main():
    # Introduction
    print("This program reads in a file containing numbers and prints out the sum of the squares of those numbers.\n")

    # Prompt user for file name
    infileName = input("Enter the name of the file containing the numbers: ")
    infile = open(infileName, "r")

    # Place the numbers in a list
    strList = infile.readlines()

    # Convert strings to nums and calculate the sum of the squares
    toNumbers(strList)
    squareEach(strList)
    total = sumList(strList)

    # Output total
    print("\nThe sum of the squares of the numbers is {0}.".format(total))

main()
