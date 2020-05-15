# File: exercise5.py
#
# Modify the chaos program so that the number of values to print is
# determined by the user. You will have to add a line near the top of
# the program to get another value from the user.
#       n = eval(input("How many numbers should I print? "))
# Then you will need to change the loop to use n instead of a specific number.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()
