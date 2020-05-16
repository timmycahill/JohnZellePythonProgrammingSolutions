# exercise2.py
#       Write a program that calculates the cost per square inch of a circular
#   pizza, given it's diameter and price. The formula for area is:
#       A = (pi)r^2

import math

def main():
    print("This program calculates the cost per square inch of a circular pizza.\n")
    
    diameter = eval(input("Enter the diameter in inches: "))
    price = eval(input("Enter the price of the pizza: "))
    
    radius = diameter / 2
    area = math.pi * radius ** 2
    costPerSI = round(price / area, 2)

    print("The cost per square inch is", costPerSI)

main()
