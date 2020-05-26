# exercise3.py
#       Write a program that uses a while loop to determine how long it takes for an investment to double at a
#   given interest rate, and the ouput is the number of years it takes an investment to double. Note: the amount
#   of the initial investment does not matter; you can use $1.

def main():
    # Introduction
    print("This program calculates how long it takes an investment to double for a given interest rate.\n")

    # Read in interest rate
    apr = eval(input("Enter the interest rate: "))

    principal = 1.0

    # Calcualte number of years
    years = 0
    while principal < 2.0:
        principal *= (1 + apr)
        years += 1

    # Output number of years
    print("\nIt will take your investment", years, "years to double.")

main()
