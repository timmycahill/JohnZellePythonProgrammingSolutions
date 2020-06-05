# gpa.py

from student import Student

def main():
    printIntroduction()
    student = getInputs()
    outputResults(student)

def printIntroduction():
    print("This program calculates a students GPA.\n")

def getInputs():
    name = input("Enter the student's name: ")
    student = Student(name, 0, 0)
    grade = input("Enter the grade for the first course: ")

    while grade != "":
        while not isValid(grade) and grade != "":
            grade = input("Invalid grade entered. Please try again (<Enter> to exit): ")
        if grade == "":
            break
        
        credits = int(input("Enter the credits for the course: "))       
        student.addLetterGrade(grade, credits)
        grade = input("Enter the grade for the next course (<Enter> to exit): ")

    return student

def isValid(grade):
    grade = grade.upper()
    if (grade == "A" or grade == "A-" or grade == "B+" or grade == "B" or grade == "B-" or grade == "C+"
        or grade == "C" or grade == "C-" or grade == "D+" or grade == "D" or grade == "F"):
         return True
    return False

def outputResults(student):
    print("\n{0}'s final GPA is {1:0.2f}.".format(student.getName(), student.gpa()))

if __name__ == "__main__":
    main()
