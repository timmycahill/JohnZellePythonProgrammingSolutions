# exercise2.py
#       The National Weather Service computes the windchill index using the following formula:
#
#                   35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
#
#   where T is the temperature in degrees Fahrenheit, and V is the wind speed in miles per hour.
#       Write a program that prints a nicely formatted table of windchill values. Rows should represent wind
#   speed for 0 to 50 in 5 mph increments, and the columns represent temperatures from -20 to +60 in 10-degree
#   increments. Note: the formula only applies for wind speeds in excess of 3 miles per hour.

def calculateWindchill(t, v):
    return 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)

def printTable(temperatures, windSpeeds):
    print("Temperature in F(x) vs Wind Speed in MPH(y)\n")
    print("         ", end="")
    for t in temperatures:
        print("{0:^9.2f}".format(t), end="")
    print()
    
    for v in windSpeeds:
        print("         ", end="")
        for i in temperatures:
            print("---------", end="")
        print()

        print("{0:^9.2f}".format(v) , end="")
        for t in temperatures:
            print("|{0:^8.2f}".format(calculateWindchill(t, v)), end="")
        print("|")
    print("         ", end="")
    for i in temperatures:
        print("---------", end="")
    print()
    

def main():
    # Introduction
    print("This program calculates the wind chill index.\n")

    # Create and fill lists for storing wind speed and temp values
    windSpeeds = []
    temperatures = []

    for i in range(0, 51, 5):
        windSpeeds.append(i)

    for i in range(-20, 61, 10):
        temperatures.append(i)

    # Print Table  
    printTable(temperatures, windSpeeds)

main()
