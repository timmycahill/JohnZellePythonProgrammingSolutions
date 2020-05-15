# File: exercise3.py
#
# Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the
# logistic function. Your modified line of code should look like this:
#       x = 2.0 * x * (1 - x)
# Run the program for various input values and compare the results to those
# obtained from the original program. Write a short paragraph describing
# any differences that you notice in the behavior of the two versions.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()


# The updated algorithm is much more predictable. Given the numbers I inputted,
# the program started around 0.3 on the first iteration and about halfway through
# the rest of the iterations the program had reached 0.5 and remained there for
# the remaining iterations.
