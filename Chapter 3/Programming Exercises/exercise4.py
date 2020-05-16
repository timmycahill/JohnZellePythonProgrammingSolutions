# exercise4.py
#       Write a program that determines the distance of a lightning strike
#   based on the time elapsed between the flash and the sound of thunder. The
#   speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.

def main():
    print("This program determines the distance of a lightning strike.\n")

    speedOfSound = 1100
    feetPerMile = 5280
    
    timeElapsed = eval(input("Enter the number of seconds between the flash " +
                             "and sound of thunder: "))

    distance = (timeElapsed * speedOfSound) / feetPerMile

    print("The lightning strike was", distance, "miles away.")

main()
