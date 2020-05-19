# exercise4.py
#       An acronym is a word formed by taking the first letters of the words
#   in a phrase and making a word from them. For example, RAM is an acronym
#   for "random access memory." Write a program that allows the user to type
#   in a phrase and then outputs the acronym for that phrase. Note: the
#   acronym should be all uppercase, even if the words in the phrase are not
#   capitalized.

def main():
    # Introduction
    print("This program will create an acronym given a phrase.\n")
    
    # Read in phrase
    phrase = input("Enter a phrase: ")
    
    # For each word
        # Read in the first letter and add it to a string and make it uppercase
    acronym = ""
    for word in phrase.split():
        acronym += word[0].upper()

    # Print acronym to screen
    print("The acronym for '{0}' is '{1}'.".format(phrase, acronym))

main()
