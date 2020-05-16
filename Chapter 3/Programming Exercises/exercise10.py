# exercise10.py
#       Write a program to determine the length of a ladder required to reach
#   a given height when leaned against a house. The height and angle of the
#   ladder are given as inputs. To compute length use:
#           length = height / sin(angle)

import math

def main():
    print("This program determines the required length of a ladder to reach "
          "a given height when leaned against a house.\n")

    height = eval(input("Enter the desired height: "))
    angle = eval(input("Enter the angle of the ladder: "))

    length = height / math.sin(angle)

    print("The required ladder length is", length)

main()
