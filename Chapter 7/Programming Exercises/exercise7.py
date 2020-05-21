# exercise7.py
#       A babysitter charges $2.50 an hour until 9:00 PM when the rate drops to $1.75 an hour (the children are in
#   bed). Write a program that accepts a starting time and ending time in hours and minutes and calculates the total
#   babysitting bill. You may assume that the starting and ending times are in a single 24-hour period. Partial
#   hours should be appropriately prorated.

def convertTimeString(time):
    hour = int(time[ : time.find(":")])
    minute = int(time[time.find(":") + 1 : time.find(" ")])
    period = time[time.find(" ") + 1 : ]
    return [hour, minute, period]

def main():
    # Introduction
    print("This program calculates a babysitters bill.\n")

    try:
        # Read in starting time and ending time
        startTime = input("Enter the start time (i.e. 9:00 PM): ")
        endTime = input("Enter the end time: ")

        # Convert strings to hours, minutes and period(AM/PM)
        startTimeList = convertTimeString(startTime)
        startHour = startTimeList[0]
        startMin = startTimeList[1]
        startPeriod = startTimeList[2].upper()
        endTimeList = convertTimeString(endTime)
        endHour = endTimeList[0]
        endMin = endTimeList[1]
        endPeriod = endTimeList[2].upper()

        if ((startPeriod == "AM" or startPeriod == "PM") and (endPeriod == "AM" or endPeriod == "PM")):
            if (startHour > 0 and startHour <= 12 and endHour > 0 and endHour <= 12):
                if (startMin >= 0 and startMin < 60 and endMin >= 0 and endMin < 60):
                    # Adjust time for PM
                    if startPeriod == "PM":
                        startHour += 12
                    if endPeriod == "PM":
                        endHour += 12

                    # Adjust end time if shift starts before and ends after midnight
                    if startHour > endHour:
                        endHour += 24

                    # Variable List
                    regularRate = 2.5
                    lowRate = 1.75
                    lowRateHour = 21
                    lowRateMin = 0
                    lowRateHoursWorked = 0;
                    regularHoursWorked = 0;

                    # Calculate hours worked                 
                    if endHour >= lowRateHour:
                        lowRateHoursWorked = endHour - lowRateHour + (endMin / 60)
                    if startHour < lowRateHour:
                        regularHoursWorked = lowRateHour - startHour + ((lowRateMin - startMin) / 60)
                        
                    bill = (regularHoursWorked * regularRate) + (lowRateHoursWorked * lowRate)

                    # Output results
                    print("\nThe bill for the night is ${0:.2f}.".format(bill))
            else:
                print("\nError: Invalid hour entered.")
        else:
            print("\nError: Invalid period entered.")    
    except:
        print("\nAn unknown error occurred.")

main()
