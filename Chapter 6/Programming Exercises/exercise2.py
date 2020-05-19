# exercise2.py
#       Write a program to print the lyrics for ten verses of "The Ants Go
#   Marching." A couple of sample verses are given below. You may choose your
#   own activity for the little one in each verse, but be sure to choose
#   something that makes the rhyme work (or almost work).

def numByNum(num):
    print("The ants go marching {0} by {0}, hurrah! hurrah!".format(num))

def rhymeVerse(num, rhyme):
    print("The ants go marching {0} by {0},".format(num))
    print("The little one stops to {0},".format(rhyme))
    print("And they all go marching down...")
    print("Into the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")

def antsGoMarching(num, rhyme):
    numByNum(num)
    numByNum(num)
    rhymeVerse(num, rhyme)

def main():
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten"]
    rhymes = ["suck his thumb", "tie his shoe", "take a knee", "touch the floor",
              "turn and hide", "wipe his kicks", "point to heaven",
              "eat a grape", "drink some wine", "start again"]

    for i in range(len(nums)):
        antsGoMarching(nums[i], rhymes[i])
        print()

main()
    
