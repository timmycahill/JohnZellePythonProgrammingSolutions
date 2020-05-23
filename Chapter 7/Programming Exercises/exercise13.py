# exercise13.py
#       The days of the year are often numbered from 1 through 365 (or 366). This number can be computed in three
#   steps using int arithmetic:
#           (a) dayNum = 31(month - 1) + day
#           (b) if the month is after February subtract (4(month) + 23) // 10
#           (c) if it's a leap year and after February 29, add 1
#
#       Write a program that accepts a date as month/day/year, verifies that it is a valid date (see previous
#   problem), and then calculates the corresponding day number.

def isLeapYear(year):
    if year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):
        return 1
    else:
        return 0

def isValidDate(month, day, year):
        # Check for valid month
        if month >= 1 and month <=12:
            # Check for valid day
            if day >= 1:
                if day <= 31 and (month == 1 or month == 3 or month == 5 or month == 7 or
                                           month == 8 or month == 10 or month == 12):
                    return 1
                elif day <= 30 and (month == 4 or month == 6 or month == 9 or month == 11):
                    return 1 
                elif month == 2 and ((isLeapYear(year) == 1 and day <= 29) or (isLeapYear(year) == 0 and day <= 28)):
                    return 1
                else:
                    return 0
        else:
            return 0

def main():
    # Introduction
    print("This program calculates the day number based on the date.\n")

    try:
        # Read in date
        date = input("Enter a date in the format mm/dd/yyyy: ")
        
        # Verify date
        dateParts = date.split("/")
        month = int(dateParts[0])
        day = int(dateParts[1])
        year = int(dateParts[2])
        
        if isValidDate(month, day, year) == 1:
            dayNum = 31 * (month - 1) + day
            if month > 2:
                dayNum -= (4 * month + 23) // 10
            if isLeapYear(year) == 1 and (month > 2 or (month == 2 and day == 29)):
                    dayNum += 1
            print("\nThe day number is", dayNum)
            
        else:
            print("\nDate is invalid.")
    except:
        print("\nAn unknown error has occurred. Please restart the program and try again.")


if __name__ == '__main__':
    main()
