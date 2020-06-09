# censor.py
# I want to put more effort into this exercise, but the more effort I put in the 
# more I see that this would be so much easier using regex.

def main():
	printIntroduction()
	infileName, outfileName, censorFileName = getInputs()
	censorFile(infileName, outfileName, censorFileName)

def printIntroduction():
	print("This program censors all four-letter words in a file.\n")

def getInputs():
	infileName = input("Enter the name of the file to censor: ")
	censorFileName = input("Enter the file name containing words to censor: ")
	outfileName = input("Enter the name of the file to write to: ")
	return infileName, outfileName, censorFileName

def censorFile(infileName, outfileName, censorFileName):
	infile = open(infileName, 'r')
	badWords = getBadWords(censorFileName)
	outfile = open(outfileName, 'w')

	lines = infile.readlines()
	for line in lines:
		print(censorLine(line, badWords), file=outfile)

	infile.close()
	outfile.close()

def getBadWords(censorFileName):
	censorFile = open(censorFileName, 'r')
	badWords = censorFile.readlines()
	for i in range(len(badWords)):
		badWords[i] = badWords[i][:-1]
	return badWords


def censorLine(line, badWords):
	words = line.split()
	newLine = ""
	for word in words:
		isBad = False
		hasPeriod = False
		hasComma = False
		hasApostrophe = False
		if word[-1] == '.':
			word = word[:-1]
			hasPeriod = True
		elif word[-1] == ',':
			word = word[:-1]
			hasComma = True
		elif word[-1] == "'":
			word = word[:-1]
			hasApostrophe = True
		for badWord in badWords:
			if word.upper() == badWord.upper():
				newLine += "*" * len(badWord)
				isBad = True
				break
		if not isBad:
			newLine += word
		if hasPeriod:
			newLine += '.'
		elif hasComma:
			newLine += ','
		elif hasApostrophe:
			newLine += "'"
		newLine += ' '
	newLine = newLine[:-1] + "\n"

	return newLine

if __name__ == '__main__':
	main()