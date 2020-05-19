# randomScoreGenerator.py
#       This program creates a file containing 20 random scores between 0-100
#   for input into exercise 13.

def main():
    # Introduction
    print("This program generates random scores for use in exercise 13.\n")

    # Get seed value, number of scores, and output file name
    seed = eval(input("Enter random number seed: "))
    numScores = eval(input("Enter the number of scores to be stored: "))
    outfileName = input("Enter a file to write the scores to: ")

    # Generate scores and save stores in outfile
    outfile = open(outfileName, "w")
    for i in range(numScores):
        score = (seed * 777) % 101
        seed = (seed * 7834) % 10000
        print(score, file=outfile)

    # Print confirmation message
    print("\nScores generated and stored in {0}.".format(outfileName))

main()
