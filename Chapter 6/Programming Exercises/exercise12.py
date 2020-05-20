# exercise12.py
#       Write and test a function to meet this specification:
#
#           sumList(nums): nums is a list of numbers. Returns the sum of the numbers in the list.

def sumList(nums):
    total = 0
    for n in nums:
        total += n
    return total

def main():
    # Introduction
    print("This program sums a list of numbers.\n")

    # Read in some numbers
    nums = []
    for i in range(10):
        num = eval(input("Enter a number: "))
        nums.append(num)

    # Square each number
    total = sumList(nums)

    # Output the results
    print("\nThe sum of the numbers in the list is {0}.".format(total))

main()
