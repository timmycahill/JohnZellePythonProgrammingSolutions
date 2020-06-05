# student.py
#   Program to find student with highest GPA

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
        

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        self.hours += credits
        self.qpoints += gradePoint

    def addLetterGrade(self, grade, credits):
        self.hours += credits
        self.qpoints += credits * self.convertGrade(grade)

    def convertGrade(self, grade):
        if grade.upper() == "A":
            return 4.0
        elif grade.upper() == "A-":
            return 3.67
        elif grade.upper() == "B+":
            return 3.33
        elif grade.upper() == "B":
            return 3.0
        elif grade.upper() == "B-":
            return 2.67
        elif grade.upper() == "C+":
            return 2.33
        elif grade.upper() == "C":
            return 2.0
        elif grade.upper() == "C-":
            return 1.67
        elif grade.upper() == "D+":
            return 1.33
        elif grade.upper() == "D":
            return 1.0
        else:
            return 0.0
