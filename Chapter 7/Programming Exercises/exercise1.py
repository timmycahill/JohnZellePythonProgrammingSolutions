# exercise1.py
#       Many companies pay time-and-a-half for any hours worked above 40 in a given week. Write a program to
#   input the number of hours worked and the hourly rate and calcualte the total wages for the week.

def main():
    # Introduction
    print("This program calculates an employee's weekly pay.\n")

    try:
        # Input hours and pay rate
        hoursWorked = eval(input("Enter the number of hours worked: "))
        hourlyRate = eval(input("Enter the hourly rate: $"))

        # Calculate wages
        if hoursWorked < 0:
            print("\nHours worked cannot be negative.")
        elif hourlyRate < 0:
            print("\nHourly rate cannot be negative.")
        else:
            if hoursWorked <= 40:
                weeklyPay = hoursWorked * hourlyRate
            else:
                weeklyPay = 40 * hourlyRate
                weeklyPay += (hoursWorked - 40) * (hourlyRate * 1.5)
            print("\nThe weekly pay for this employee is ${0:.2f}.".format(weeklyPay))
    except:
        print("\nInvalid input. Please use numbers as your inputs.")
        
main()
