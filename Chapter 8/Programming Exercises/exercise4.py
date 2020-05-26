# exercise4.py
#       The Syracuse (also called Collatz or Hailstone) sequence is generated by starting with a natural number
#   and repeatedly applying the following function until reaching 1:
#
#           syr(x) = x / 2      (if x is even)
#                    3x + 1     (if x is odd)
#
#       For example, the Syracuse sequence starting with 5 is: 5, 16, 8, 4, 2, 1. It is an open question in
#   mathematics whether this sequence will always go to 1 for every possible starting value.
#       Write a program that gets a starting value from the user and then prints the Syracuse sequence for that
#   starting value.

def syr(x):
    seq = [str(x)]
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        seq.append(str(x))
    return seq

def main():
    # Introduction
    print("This program calculates the Syracuse sequence for a given number.\n")

    try:
        # Read in starting number
        n = int(input("Enter the starting number: "))

        # Calculate sequence and turn into string
        seq = syr(n)
        seqStr = ", ".join(seq)
        
        # Print results
        print("\nThe Syracuse sequence for", n, "is " + seqStr + ".")
    except ValueError:
        print("\nError: Must enter an integer as starting number.")
    except:
        print("\nAn unknown error occured.")

main()
