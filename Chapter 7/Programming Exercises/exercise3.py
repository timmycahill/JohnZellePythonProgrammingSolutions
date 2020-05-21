# exercise3.py
#       A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C,
#   60-69:D, <60:F. Write a program that accepts an exam score as input and uses a decision structure to calculate
#   the corresponding grade.

def main():
    # Introduction
    print("This program calculates a students grade given their exam score.\n")

    try:
        # Read in exam score
        score = eval(input("Enter the exam score: "))

        if score >= 0 and score <= 100:
            if score < 60:
                grade = "F"
            elif score < 70:
                grade = "D"
            elif score < 80:
                grade = "C"
            elif score < 90:
                grade = "B"
            else:
                grade = "A"
            print("The exam grade is", grade)
        else:
            print("Invalid score entered. Not in range.")
    except:
        print("Invalid score entered.")

main()
            
                
