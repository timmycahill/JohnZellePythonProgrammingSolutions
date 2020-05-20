# exercise11.py
#       Write and test a function to meet this specification:
#
#           squareEach(nums): nums is a list of numbers. Modifies the list by
#                             squaring each entry.

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def main():
    # Introduction
    print("This program squares each number in a list of numbers.\n")

    # Read in some numbers
    nums = []
    for i in range(10):
        num = eval(input("Enter a number: "))
        nums.append(num)

    # Square each number
    squareEach(nums)

    # Output the results
    print("\nNew numbers:")
    for n in nums:
        print(n)

main()
