# exercise9.py
#       Write a program that counts the number of words in a sentence entered
#   by the user.

def main():
    # Introduction
    print("This program counts the number of words in a sentence entered " +
          "by the user.\n")

    sentence = input("Enter a sentence to be evaluated: ")

    wordCount = 0
    for word in sentence.split():
        wordCount += 1

    # Output results
    print("The sentence '{0}' has {1} words in it.".format(sentence, wordCount)) 

main()
