# exercise9.py
#       A formula for computing Easter in the years 1982-2048, inclusive, is as follows: let a = year % 19,
#   b = year % 4, c = year % 7, d = (19a + 24) % 30, e = (2b + 4c + 6d + 5) % 7. The date of easter is
#   March 22 + d + e (which could be in April). Write a program that inputs a year, verifies that it is in the
#   proper range, and then prints out the date of Easter that year.

def main():
    # Introduction
    print("This program calculates the date of Easter for a given year (1982-2048).\n")

    try:
        # Input year
        year = int(input("Enter the year: "))
        
        if year >= 1982 and year <= 2048:
            # Calculate Easter
            a = year % 19
            b = year % 4
            c = year % 7
            d = (19 * a + 24) % 30
            e = (2 * b + 4 * c + 6 * d + 5) % 7

            day = 22 + d + e
            if day <= 31:
                month = "March"
            else:
                month = "April"
                day -= 31
            
            # Print out results
            print("\nEaster day in {0} is {1} {2}.".format(year, month, day))
        else:
            print("\nError: Year not in range.")
    except:
        print("\nError: Invalid input.")

main()
