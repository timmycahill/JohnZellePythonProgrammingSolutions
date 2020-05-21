# exercise2.py
#       A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
#   Write a program that accepts a quiz score as an input and uses a decision structure to calculate the
#   corresponding grade.

def main():
    # Introduction
    print("This program calculates a student's grade based on their quiz score.\n")

    try:
    # Read in score
        score = eval(input("Enter the quiz score: "))
        if type(score) == int:
            if score >= 0 and score <= 5:
                if score == 5:
                    grade = "A"
                elif score == 4:
                    grade = "B"
                elif score == 3:
                    grade = "C"
                elif score == 2:
                    grade = "D"
                else:
                    grade = "F"
                print("The student's grade is", grade)
            else:
                print("Score not in range.")
        else:
            print("Invalid score entered.")
    except:
        print("Invalid score entered.")
        
    
main()
