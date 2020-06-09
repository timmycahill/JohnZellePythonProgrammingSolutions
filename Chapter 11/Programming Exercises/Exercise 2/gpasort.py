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

	###########################################
	#       Modified Content Start
	###########################################
	print("Sorting Options:")
	print("\t1. GPA")
	print("\t2. Name")
	print("\t3. Credits")
	selection = eval(input("Enter your selection: "))
	while selection != 1 and selection != 2 and selection != 3:
		selection = eval(input("Invalid selection. Please choose a valid option: "))
	if selection == 1:
		data.sort(key=Student.gpa)
	elif selection == 2:
		data.sort(key=Student.getName)
	else:
		data.sort(key=Student.getHours)
	###########################################
	#       Modified Content End
	###########################################

	filename = input("Enter a name for the output file: ")
	writeStudents(data, filename)
	print("The data has been written to", filename)
	
if __name__ == '__main__':
	main()