# exercise14.py
#       Word count. A common utility on Unix/Linux systems is a small program
#   called "wc." This program analyzes a file to determine the number of lines,
#   words, and characters contained therein. Write your own version of wc. The
#   program should accept a file name as input and then print three numbers
#   showing the count of lines, words, and characters in the file.

def main():
    # Introduction
    print("This program will count the number of lines, words, and characters" +
          "in a file.\n")

    # Get file name
    infileName = input("Enter the name of the file to be analyzed: ")

    # Analyze file
    infile = open(infileName, "r")
    lineCount, wordCount, charCount = 0, 0, 0
    for line in infile:
        # Increment line count
        lineCount += 1
        for word in line.split():
            # Increment word count
            wordCount += 1
            for ch in word:
                # Increment char count
                charCount += 1
            # Increment charCount for space in between words
            charCount += 1
        # Decrement charCount for phantom space counted after last word in line
        charCount -= 1

    # Output results
    print("\nLine Count:", lineCount)
    print("Word Count:", wordCount)
    print("Character Count:", charCount)

main()
        
