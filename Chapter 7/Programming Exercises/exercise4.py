# exercise4.py
#       A certain college classifies students according to credits earned. A student with less than 7 credits
#   is a Freshman. At least 7 credits are required to be a Sophomore, 16 to be a Junior, and 26 to be classified
#   as a Senior. Write a program that calculates class standing from the number of credits earned.

def main():
    print("This program determins a students class standing based on their credits earned.\n")

    try:
        creditsEarned = eval(input("Enter credits earned: "))
        if type(creditsEarned) == int:
            if creditsEarned >= 0:
                if creditsEarned < 7:
                    classStanding = "Freshman"
                elif creditsEarned < 16:
                    classStanding = "Sophomore"
                elif creditsEarned < 26:
                    classStanding = "Junior"
                else:
                    classStanding = "Senior"
                print("The student is a", classStanding)
            else:
                print("Invalid input. Credits earned cannot be less than 0.")
        else:
            print("Invalid input. Credits earned must be an integer.")
    except:
        print("Invalid input.")

main()
