# exercise15.py
#       Write a program that approximates the value of pi by summing the terms of this series:
#           4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
#       The program should prompt the user for n, the number of terms to sum, and then output the sum of the
#   first n terms of the series. Have your program subtract the approximation from the value of math.pi
#   to see how accurate it is.

import math

def main():
    print("This program approximates the value of pi.\n")

    n = eval(input("Enter the number of terms to sum in the approximation: "))
    pi = 0
    denom = 1
    for i in range(0, n, 2):
        pi += 4/denom
        denom += 4

    denom = 3
    for i in range(1, n, 2):
        pi -= 4/denom
        denom += 4
    
    print("The approximation of pi with", n, "terms is", pi)

    difference = abs(math.pi - pi)

    print("The approximation is", difference, "away from the math.pi value")

main()
