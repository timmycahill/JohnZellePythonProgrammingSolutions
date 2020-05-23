# exercise12.py
#       Write a program that accepts a date in the form month/day/year and outputs whether or not the date is
#   valid. For example, 5/24/1962 is valid, but 9/31/2000 is not. (September has only 30 days.)

def isLeapYear(year):
    if year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):
        return 1
    else:
        return 0

def main():
    # Introduction
    print("This program determines if a given date is valid or not.\n")

    try:
        # Read in date
        date = input("Enter a date in the format mm/dd/yyyy: ")

        # Convert date to numbers
        dateParts = date.split("/")
        month = int(dateParts[0])
        day = int(dateParts[1])
        year = int(dateParts[2])

        # Check for valid month
        if month >= 1 and month <=12:
            # Check for valid day
            if day >= 1:
                if day <= 31 and (month == 1 or month == 3 or month == 5 or month == 7 or
                                           month == 8 or month == 10 or month == 12):
                    print("\n{0} is a valid date.".format(date))
                elif day <= 30 and (month == 4 or month == 6 or month == 9 or month == 11):
                    print("\n{0} is a valid date.".format(date))
                elif month == 2 and ((isLeapYear(year) == 1 and day <= 29) or (isLeapYear(year) == 0 and day <= 28)):
                    print("\n{0} is a valid date.".format(date))
                else:
                    print("\n{0} is not a valid date.".format(date))
        else:
            print("\n{0} is not a valid date.".format(date))
    except:
        print("\n{0} is not a valid date.".format(date))    

if __name__ == '__main__':
    main()
