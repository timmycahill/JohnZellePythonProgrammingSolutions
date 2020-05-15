# exercise8.py
#       Write a program that converts temperatures from Fahrenheit to Celsius

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5/9 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Celsius.")

main()
