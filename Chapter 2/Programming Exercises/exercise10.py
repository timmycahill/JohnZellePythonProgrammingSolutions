# exercise10.py
#       Write a program to perform a unit conversion of your own chosing. Make
#   sure that the program prints an introduction explaining what it does.

def main():
    print("This program converts feet to inches.\n")

    feet = eval(input("Enter a number in feet: "))
    inches = feet * 12
    print(feet, "feet is", inches, "inches.")

main()
