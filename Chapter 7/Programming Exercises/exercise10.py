# exercise10.py
#       The formula for Easter in the previous problem works for every year in the range 1990-2099 except for 1954,
#   1982, 2049, and 2076. For these 4 years it produces a date that is one week too late. Modify the above program
#   to work for the entire range 1900-2099.

def main():
    # Introduction
    print("This program calculates the date of Easter for a given year (1982-2048).\n")

    try:
        # Input year
        year = int(input("Enter the year: "))
        
        if year >= 1900 and year <= 2099:
            # Calculate Easter
            a = year % 19
            b = year % 4
            c = year % 7
            d = (19 * a + 24) % 30
            e = (2 * b + 4 * c + 6 * d + 5) % 7

            day = 22 + d + e

            # Determine if year is one of the off years
            offYears = [1954, 1982, 2049, 2076]
            for offYear in offYears:
                if year == offYear:
                    day -= 7
            
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
