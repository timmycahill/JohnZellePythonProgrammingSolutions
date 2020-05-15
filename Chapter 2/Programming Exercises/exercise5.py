# exercise5.py
#       Modify the futval.py program (Section 2.7) so that the number of years
#   for the investment is also a user input. Make sure to change the final
#   message to reflect the correct number.

def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the life of the investment in years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is:", principal)

main()
