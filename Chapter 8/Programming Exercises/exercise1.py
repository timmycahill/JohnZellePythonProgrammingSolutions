# exercise1.py
#       The Fibonacci sequence starts 1,1,2,3,5,8,... Each number in the
#   sequence (after the first 2) is the sum of the previous two. Write
#   a program that computes and outputs the nth Fibonacci number, where
#   n is a value entered by the user.

def main():
    # Introduction
    print("This program calculates the nth fibonacci number.\n")

    try:
        # Read in n
        n = int(input("Enter a value for n: "))

        if (n == 1 or n == 2):
            print("\nFibonacci Number: 1")
        elif n > 2:
            previous1 = 1
            previous2 = 1

            for i in range(n - 2):
                fib = previous1 + previous2
                previous2 = previous1
                previous1 = fib

            print("\nFibonacci Number:", fib)

        else:
            print("\nError: Invalid number entered.")
        
    except:
        print("\nError: An unknown error occurred.")

main()
