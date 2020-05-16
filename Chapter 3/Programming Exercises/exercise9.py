# exercise9.py
#       Write a program to calculate the area of a triangle given the length of
#   its three sides a, b, and c using these formulas:
#           s = (a + b + c) / 2
#           A = sqrt(s(s - a)(s - b)(s - c))

import math

def main():
    print("This program calculates the area of a triangle given the length " +
          "of its three sides.\n")

    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval(input("Enter the length of side c: "))

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area of the triangle is", area)

main()
