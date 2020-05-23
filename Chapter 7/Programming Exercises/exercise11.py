# exercise11.py
#       A year is a leap year if it is divisible by 4, unless it is a century year that is not divisible by 400.
#   (1800 and 1900 are not leap years while 1600 and 2000 are.) Write a program that calculates whether a year
#   is a leap year.

def main():
    # Introduction
    print("This program determines if a year is a leap year or not.\n")

    try:
        # Read in year
        year = int(input("Enter the year: "))

        # Determine if year is leap year and output results
        if year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):
            print("\n{0} is a leap year.".format(year))
        else:
            print("\n{0} is not a leap year.".format(year))
    except:
        print("Error: Invalid input.")

main()
