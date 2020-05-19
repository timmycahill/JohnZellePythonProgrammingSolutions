# exercise3.py
#       A certain CS professor gives 100-point exams that are graded on the
#   scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that
#   accepts an exam score as input and prints out the corresponding grade.

def main():
    # Introduction
    print("This program calculates an exam's letter grade given it's score.\n")

    # Create list of grades
    letterGrade = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]

    # Get exam score
    examScore = eval(input("Enter the exam score: "))

    # Print the results
    print("The student's letter grade is {0}.".format(letterGrade[examScore // 10]))

main()
