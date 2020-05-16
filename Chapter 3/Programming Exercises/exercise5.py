# exercise5.py
#       The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost
#   of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for
#   overhead. Write a program that calculates the cost of an order.

def main():
    print("This program will calculate the cost of a coffee order for the " +
          "Konditorei coffee shop.\n")

    pricePerPound = 10.50
    shippingPerPound = 0.86
    shippingOverhead = 1.50

    pounds = eval(input("Enter the amount of coffee you would like to order " +
                        "in pounds: "))

    totalPrice = pounds * (pricePerPound + shippingPerPound) + shippingOverhead

    print("The price for your order is $", totalPrice)

main()
