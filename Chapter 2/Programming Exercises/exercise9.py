# exercise9.py
#       Write a program that converts distances measured in kilometers to miles.
#   One kilometer is approximately 0.62 miles.

def main():
    print("This program converts kilometers to miles.\n")

    kilometers = eval(input("Enter the number of kilmoeters: "))
    miles = kilometers * 0.62
    print(kilometers, "kilometers is approximately", miles, "miles.")

main()
