# exercise10.py
#       Write a program that calculates the average word length in a sentence
#   entered by the user.

def main():
    # Introduction
    print("This program counts the number of words in a sentence entered " +
          "by the user.\n")

    sentence = input("Enter a sentence to be evaluated: ")

    wordCount = 0
    charCount = 0
    for word in sentence.split():
        wordCount += 1
        charCount += len(word)
    averageLength = charCount / wordCount

    # Output results
    print("The average length of words in the sentence is {0}.".format(averageLength)) 

main()
