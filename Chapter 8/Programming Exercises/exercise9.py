# exercise9.py
#       Write a program that computes the fuel efficiency of a multi-leg journey. The program will first prompt
#   for the starting odometer reading and then get information about a series of legs. For each leg, the user
#   enters the current odometer reading and the amount of gas used (separated by a space). The user signals the
#   end of the trip with a blank line. The program should print out the miles per gallon achieved on each leg and
#   the total MPG for the trip.

def main():
    # Introduction
    print("This program computes the fuel efficiency of a multi-leg journey.\n")
    try:
        # Read in legs
        legs = []

        # Get the starting odometer reading
        odometerStart = eval(input("Enter the starting odometer reading: "))

        # Get the odomoeter and miles for the rest of the trip
        leg = input("Enter the first leg (\"[odometer reading] [amt gas used]\"): ")
        while leg != "":
            legs.append(leg)
            leg = input("Enter the next leg (\"[odometer reading] [amt gas used]\"): ")

        # Compute efficiency for each leg
        totalMiles = 0
        totalGallons = 0
        lastReading = odometerStart
        legEfficiency = []
        
        for leg in legs:
            parts = leg.split()
            for i in range(len(parts)):
                parts[i] = eval(parts[i])
            legEfficiency.append((parts[0] - lastReading) / parts[1])
            totalMiles += parts[0] - lastReading
            totalGallons += parts[1]
            lastReading = parts[0]


        # Calculate total efficiency for the trip
        totalEfficiency = totalMiles / totalGallons

        # Output results
        print("Trip Efficiency:")
        for i in range(len(legEfficiency)):
            print("\t{0}: {1:0.2f} MPG".format(i + 1, legEfficiency[i]))
        print("Total Efficiency: {0:0.2f} MPG".format(totalEfficiency))
        
    except:
        print("An unknown error has occurred.")

if __name__ == "__main__":
    main()
