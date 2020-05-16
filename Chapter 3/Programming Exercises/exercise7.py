# exercise7.py
#       Write a program that accepts two points (see previous problem) and
#   determines the distance between them.

import math

def main():
    print("This program determines the distance between two points.\n")

    x1 = eval(input("Enter x1: "))
    y1 = eval(input("Enter y1: "))
    x2 = eval(input("Enter x2: "))
    y2 = eval(input("Enter y2: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("The distance between the two points is", distance)

main()
