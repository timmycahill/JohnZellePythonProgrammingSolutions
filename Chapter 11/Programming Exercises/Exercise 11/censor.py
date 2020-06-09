# censor.py

def main():
	printIntroduction()
	infileName, outfileName = getInputs()
	censorFile(infileName, outfileName)

def printIntroduction():
	print("This program censors all four-letter words in a file.\n")

def getInputs():
	infileName = input("Enter the name of the file to censor: ")
	outfileName = input("Enter the name of the file to write to: ")
	return infileName, outfileName

def censorFile(infileName, outfileName):
	infile = open(infileName, 'r')
	outfile = open(outfileName, 'w')

	lines = infile.readlines()
	for line in lines:
		print(censorLine(line), file=outfile)

	infile.close()
	outfile.close()

def censorLine(line):
	words = line.split()
	newLine = ""
	for word in words:
		if len(word) == 4:
			newLine += "****"
		else:
			newLine += word
		newLine += " "
	newLine = newLine[:-1] + "\n"

	return newLine

if __name__ == '__main__':
	main()