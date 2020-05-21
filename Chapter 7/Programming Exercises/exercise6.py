# exercise6.py
#       The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a penalty
#   of $200 for any speed over 90 mph. Write a program that accepts a speed limit and a clocked speed and either
#   prints a message indicating the speed was legal or prints the amount of the fine, if the speed was illegal.

def main():
    # Introduction
    print("This program determines if a driver is speeding and calculates the price of the ticket if they are.\n")

    try:
        # Read in driver speed
        speedLimit = eval(input("Enter the speed limit: "))
        clockedSpeed = eval(input("Enter the clocked speed: "))

        if speedLimit <= 0:
            print("Speed limit must be greater than 0.")
        elif type(speedLimit) != int:
            print("Speed limit must be an integer.")
        elif clockedSpeed <= 0:
            print("Clocked speed must be greater than 0.")
        elif type(clockedSpeed) != int:
            print("Clocked speed must be an integer.")
        else:
            baseFine = 50
            finePerMPH = 5
            over90Fine = 200
            
            clockedSpeed = int(clockedSpeed)  
            if clockedSpeed <= speedLimit:
                print("\nThe driver's speed was legal.")
            else:
                fine = baseFine + ((clockedSpeed - speedLimit) * finePerMPH)
                if clockedSpeed > 90:
                    fine += over90Fine
                print("The driver was speeding and their fine is ${0:.2f}.".format(fine))  
    except:
        print("Invalid input.")

main()
