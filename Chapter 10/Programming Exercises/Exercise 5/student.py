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
