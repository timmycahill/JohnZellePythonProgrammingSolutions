# exercise12.py
#       Write an improved version of the future value program from Chapter 2.
#   Your program will prompt the user for the amount of the investment, the
#   annualized interest rate, and the number of years of the investment. The
#   program will then output a nicely formatted table that tracks the value of
#   the investment year by year.

def main():
    # Introduction
    print("This program will calculate the future value of an investment.\n")
    
    # Get investment amount, interest rate, and # years of the investment
    principal = eval(input("Enter the inital investment amount: "))
    interestRate = eval(input("Enter the annual interest rate: "))
    numYears = eval(input("Enter the number of years for the investment: "))

    # Print table to screen
    print("\nYear     Value")
    print("----------------")
    print("{0:^5}   ${1:3.2f}".format(0, principal))
    for year in range(numYears):
        principal = principal * (1 + interestRate)
        print("{0:^5}   ${1:3.2f}".format(year + 1, principal))

main()
