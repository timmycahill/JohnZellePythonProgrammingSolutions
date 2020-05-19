# exercise11.py
#       Write an imporved version of the Chaos program from Chapter 1 that
#   allows a user to input two initial values and the number of iterations and
#   then prints a nicely formatted table showing how the values change over
#   time.

def main():
    # Introduction
    print("This program illustrates a chaotic function.\n")

    # Get initial values and number of iterations
    value1, value2, numIter = eval(input("Enter two initial values and the " +
                                         "number of iterations: "))

    # Output header
    print("\nindex  {0:^8}     {1:^8}".format(value1, value2))
    print("----------------------------")

    # Calculate and print chaos values
    for i in range(numIter):
        value1 = 3.9 * value1 * (1 - value1)
        value2 = 3.9 * value2 * (1 - value2)
        print("{0:^5}  {1:^7f}     {2:^7f}".format(i + 1, value1, value2))

main() 
