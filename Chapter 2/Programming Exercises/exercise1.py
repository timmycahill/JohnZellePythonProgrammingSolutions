# exercise1.py
#       A user-friendly program should print an introduction that tells
#   the user what the program does. Modify the convert.py program (Section 2.2)
#   to print an introduction.

def main():
    print("This program converts temperature from Celsius to Fahrenheit.\n")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
