# gpasort.py
#	 A program to sort student information into GPA order.

from gpa import Student, makeStudent

def readStudents(filename):
	infile = open(filename, 'r')
	students = []
	for line in infile:
		students.append(makeStudent(line))
	infile.close()
	return students

def writeStudents(students, filename):
	outfile = open(filename, 'w')
	for s in students:
		print("{0}\t{1}\t{2}".
				 format(s.getName(), s.getHours(), s.getQPoints()),
			  file=outfile)
	outfile.close()

def main():
	print("This program sorts student grade information by GPA")
	filename = input("Enter the name of the data file: ")
	data = readStudents(filename)

	#####################################################################
	#              Modified code starts
	#####################################################################

	gpaList = []
	for datum in data:
		gpaList.append((datum.gpa(), datum))
	gpaList.sort()
	sortedStudents = []
	for i in range(len(gpaList)):
		gpa, student = gpaList[i]
		sortedStudents.append(student)

	filename = input("Enter a name for the output file: ")
	writeStudents(sortedStudents, filename)

	#####################################################################
	#              Modified code ends
	#####################################################################
	
	print("The data has been written to", filename)
	
if __name__ == '__main__':
	main()