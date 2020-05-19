# exercise2.py
#       A certain CS professor gives 5-point quizzes that are graded on the
#   scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz
#   score as an input an prints out the corresponding grade.

def main():
    # Introduction
    print("This program will print out a letter grade given a quiz score.\n")

    # Make list containing grades
    letterGrades = ["F", "F", "D", "C", "B", "A"]

    # Get quiz score
    numberGrade = eval(input("Enter the quiz score: "))

    # Return letter grade
    print("This student's grade is {0}.".format(letterGrades[numberGrade]))

main()
    
