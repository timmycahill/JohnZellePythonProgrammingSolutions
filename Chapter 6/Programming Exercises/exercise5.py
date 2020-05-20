# exercise5.py
#       Redo Programming Exercise 2 from Chapter 3. Use two functions - one to
#   compute the area of a pizza, and one to compute cost per square inch.

import math

def computeArea(radius):
    return math.pi * radius ** 2

def computeCostPerInch(price, area):
    return round(price / area, 2)

def main():
    print("This program calculates the cost per square inch of a circular pizza.\n")
    
    diameter = eval(input("Enter the diameter in inches: "))
    price = eval(input("Enter the price of the pizza: "))
    
    radius = diameter / 2
    area = computeArea(radius)
    costPerSI = computeCostPerInch(price, area)
    
    print("The cost per square inch is ${0}.".format(costPerSI))

main()
