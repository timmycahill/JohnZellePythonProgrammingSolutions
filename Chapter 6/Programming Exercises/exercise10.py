# exercise10.py
#       Do Programming Exercise 5 from Chapter 5 using a function acronym(phrase)
#   that returns an acronym for a phrase supplied as a string.
#
#       *** I am assuming they meant exercise 4 ***

def acronym(phrase):
    acronym = ""
    for word in phrase.split():
        acronym += word[0].upper()
    return acronym
    
def main():
    # Introduction
    print("This program will create an acronym given a phrase.\n")
    
    # Read in phrase
    phrase = input("Enter a phrase: ")
    
    # Create acronym from phrase
    newAcronym = acronym(phrase)

    # Print acronym to screen
    print("The acronym for '{0}' is '{1}'.".format(phrase, newAcronym))

main()
