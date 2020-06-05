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
    credits = input("Enter the credits for the first course: ")

    while credits != "":
        gradePoint = input("Enter the grade point for the course: ")
        student.addGrade(float(gradePoint), int(credits))
        credits = input("Enter the credits for the next course <Enter to exit>: ")

    return student

def outputResults(student):
    print("\nThe student's final GPA is {0:0.2f}.".format(student.gpa()))

if __name__ == "__main__":
    main()
