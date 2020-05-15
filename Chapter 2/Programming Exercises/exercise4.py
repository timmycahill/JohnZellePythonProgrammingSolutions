# exercise4.py
#       Modify the convert.py program (Section 2.2) so that it computes and
#   prints a table of Celsius temperatures and the Fharenheit equivalents
#   every 10 degrees from 0C to 100C

def main():
    print("This program converts temperature from Celsius to Fahrenheit.\n")

    print("Celsius           Fahrenheit")
    print("--------------------------------------")
    for i in range(11):
        celsius = i * 10
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "               ", fahrenheit)

main()
