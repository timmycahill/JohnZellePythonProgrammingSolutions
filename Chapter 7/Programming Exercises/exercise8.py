# exercise8.py
#       A person is eligible to be a US senator if they are at least 30 years old and have been a US citizen for
#   at least 9 years. To be a US representative these numbers are 25 and 7, respectively. Write a program that
#   accepts a person's age and years of citizenship as input and outputs their eligibility for the Senate and House.

def main():
    # Introduction
    print("This program determines a person's eligibility to be a US senator or representative.\n")

    try:
        # Input age and years of citizenship
        age = int(input("Enter your age: "))
        yearsOfCit = int(input("Enter the number of years you have been a citizen: "))

        if age >= 30 and yearsOfCit >= 9:
            print("You can be a US senator and US representative.")
        elif age > 25 and yearsOfCit >= 7:
            print("You can be a US representative.")
        else:
            print("You cannot be a US senator or representative.")  
    except:
        print("Invalid input.")
        
main()
