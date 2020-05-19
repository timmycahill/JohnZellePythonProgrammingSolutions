# exercise13.py
#       Redo any of the previous programming problems to make them batch
#   oriented (using text files for input and output).
#
#       ***Chosing to reprogram exercise3.py using batch files***

def main():
    # Introduction
    print("This program calculates the letter grades for a list of exam scores.\n")

    # Get name of files to read from and write to
    infileName = input("Enter the name of the file to read from: ")
    outfileName = input("Enter the name of the file to write to: ")
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    
    # Create list of grades
    letterGradeList = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]

    # Determine exam score for each exam score and write it to the output file
    for line in infile:
        examScore = eval(line[0:-1])
        letterGrade = letterGradeList[examScore // 10]
        print(letterGrade, file=outfile)

    # Output confirmation message
    print("\nLetter grades successfully calculated and stored in {0}.".format(outfileName))
    
main()
