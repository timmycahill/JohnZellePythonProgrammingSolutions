# exercise9.py
#       Do Programming Exercise 3 from Chapter 5 using a function grade(score)
#   that returns the letter grade for a score.

def grade(score):
    letterGrade = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    return letterGrade[score // 10]
    
def main():
    # Introduction
    print("This program calculates an exam's letter grade given it's score.\n")

    # Get exam score
    examScore = eval(input("Enter the exam score: "))

    # Determine letter grade
    letterGrade = grade(examScore)

    # Print the results
    print("The student's letter grade is {0}.".format(letterGrade))

main()
