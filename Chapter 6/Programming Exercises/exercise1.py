# exercise1.py
#       Write a program to print the lyrics of the song "Old MacDonald." Your
#   program should print the lyrics for five different animals, similar to the
#   example verse below.

def singVerse(animal, sound):
    introOutro()
    print("And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a {0}, {0} here and a {0}, {0} there.".format(sound))
    print("Here a {0}, there a {0}, everywhere a {0}, {0}.".format(sound))
    introOutro()

def introOutro():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def main():
    singVerse("cow", "moo")
    print()
    singVerse("pig", "oink")
    print()
    singVerse("duck", "quack")
    print()
    singVerse("chicken", "cluck")
    print()
    singVerse("horse", "neigh")

main()
