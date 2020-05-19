# exercise6.py
#       Expand your solution to the previous problem to allow the calculation of
#   a complete name such as "John Marvin Zelle" or "John Jacob Jingleheimer
#   Smith." The total value is just the sum of the numeric values of all the
#   names.

def main():
    # Introduction
    print("This program calculates the numeric value of a name.\n")

    # Read in name
    name = input("Enter the name to be evaluated: ")

    # Calculate numeric value
    value = 0
    # Split up name into individual words
    for word in name.split():
        for ch in word:
            # Make ch upper for consistency
            # -64 from ch numeric value to start with A = 1
            value += (ord(ch.upper()) - 64)

    # Print numeric value to screen
    print("The numeric value of {0} is {1}.".format(name, value))

main()
