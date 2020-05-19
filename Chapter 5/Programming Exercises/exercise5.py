# exercise5.py
#       Numerologists claim to be able to determine a person's character traits
#   based on the "numeric value" of a name. The value of a name is determined
#   by summing up the values of the letters of the name where "a" is 1, "b" is
#   2, "c" is 3 etc. up to "z" being 26. For example, the name "Zelle" would
#   have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very
#   auspicious number, by the way). Write a program that calculates the
#   numeric value of a single name provided as input.

def main():
    # Introduction
    print("This program calculates the numeric value of a name.\n")

    # Read in name
    name = input("Enter the name to be evaluated: ")

    # Calculate numeric value
    value = 0
    for ch in name:
        # Make ch upper for consistency
        # -64 from ch numeric value to start with A = 1
        value += (ord(ch.upper()) - 64)

    # Print numeric value to screen
    print("The numeric value of {0} is {1}.".format(name, value))

main()
