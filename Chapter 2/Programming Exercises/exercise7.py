# exercise7.py
#       Modify the futval.py program to prompt the user for yearly rate (rate)
#   and the number of times that the interest is compounded each year (periods).
#   To compute the value in ten years the program will loop 10 * periods and
#   accrue rate/period interest on each iteration.

def main():
    print("This program calculates the future value")
    print("of a 10 year investment.")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the yearly interest rate: "))
    periods = eval(input("Enter the number of time the investment is compounded per year: "))

    for i in range(10 * periods):
        principal = principal * (1 + (rate / periods))

    print("The value in 10 years is:", principal)

main()
