# exercise5.py
#       The body mass index (BMI) is calculated as a person's weight (in pounds) times 720, divided by the square
#   of the person's height (in inches). A BMI in the range 19-25, inclusive, is considered healthy. Write a program
#   that calculates a person's BMI and prints a message telling whether they are above, within, or below the
#   healthy range.

def main():
    # Introduction
    print("This program calculates a person's BMI.\n")

    try:
        # Get person's weight and height
        weight = eval(input("Enter your weight (pounds): "))
        height = eval(input("Enter your height (inches): "))

        if not weight > 0:
            print("Invalid input. Weight must be greater than 0.")
        elif not height > 0:
            print("Invalid input. Height must be greater than 0.")
        else:
            # Calculate BMI
            bmi = int((weight * 720) / (height ** 2))

            # Output results
            if bmi < 19:
                print("\nYour BMI is {0}, below the healthy range.".format(bmi))
            elif bmi > 25:
                print("\nYour BMI is {0}, above the healthy range.".format(bmi))
            else:
                print("\nYour BMI is {0}, within the healthy range.".format(bmi))
    except:
        print("Invalid input")

main()
