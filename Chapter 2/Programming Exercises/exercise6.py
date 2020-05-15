# exercise6.py
#       Suppose you have an investment plan where you invest a certain fixed
#   amount every year. Modify futval.py to compute the total accumulation of
#   your investment. The inputs to the program will be the amount to invest
#   each year, the interest rate, and the number of years for the investment.

def main():
    print("This program calculates the future value")
    print("of an investment.")

    yearlyInvestment = eval(input("Enter the amount to invest yearly: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for the investment: "))
    investmentValue = 0
    
    for i in range(years):
        investmentValue += yearlyInvestment
        investmentValue = investmentValue * (1 + apr)

    print("The value in", years, "years is:", investmentValue)

main()
