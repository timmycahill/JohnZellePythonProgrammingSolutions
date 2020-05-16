# exercise1.py
#       Write a program to calculate the volume and surface area of a sphere
#   from it's radius, given as input. Here are some formulas that might be
#   useful:
#       V = 4/3(pi)r^3
#       A = 4(pi)r^2

import math

def main():
    print("This program calculates the volume and surface area of a sphere " +
          "given its radius.\n")
    
    radius = eval(input("Enter the radius of the sphere: "))

    volume = 4 / 3 * math.pi * radius ** 3
    surfaceArea = 4 * math.pi * radius ** 2

    print("The volume of the sphere is", volume, "and the surface area is",
          surfaceArea)

main()
