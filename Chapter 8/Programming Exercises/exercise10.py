# exercise10.py
#       Modify the previous program to get its input from a file.

def main():
    # Introduction
    print("This program computes the fuel efficiency of a multi-leg journey.\n")
    try:
        # Read in legs
        legs = []

        # Read in file
        infileName = input("Enter the file name containing the trip information: ")
        infile = open(infileName, "r")

        # Read first odometer reading
        odometerStart = int(infile.readline())

        # Read in the rest of the trip information
        legs = infile.readlines()
        

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
