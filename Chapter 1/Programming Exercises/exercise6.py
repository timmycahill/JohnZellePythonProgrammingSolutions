# File: exercise6.py
#
# The calculation performed in the chaos program can be written in a number
# of ways that are algebraically equivalent. Write a version of the program
# for each of the following ways of doing the computation. Have your
# modified programs print out 100 iterations of the function and compare
# the results when run on the same input.
#       (a) 3.9 * x * (1 - x)
#       (b) 3.9 * (x - x * x)
#       (c) 3.9 * x - 3.9 * x * x
# Explain the results of this experiment. Hint: See discussion question number
# 4, above.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    z = y = x
    for i in range(100):
        x = 3.9 * x * (1 - x)
        y = 3.9 * (y - y * y)
        z = 3.9 * z - 3.9 * z * z
        print("(a)", x, "(b)", y, "(c)", z)

main()

# Because numbers are stored as approximations instead of exact values
# in the computer, this leads to very small differences in results depending
# on how those results are achieved. In the beginning of the program, the
# 3 of these equations yield very similar results which are slightly off.
# As the loop continues to run, these slight differences grow and by the end
# of the program none of the answers are close. They have all gone their own way.
