# exercise11.py
#       Write an interactive Python calculator program. The program should allow
#   the user to type a mathematical expression, and then print the value of the
#   expression. Include a loop so that the user can perform many calculations
#   (say, up to 100). Do not worry about quitting how to exit.

def main():
    print("This program is a very poor calculator.\n")

    for i in range(100):
        value = eval(input("Enter an expression to be calculated: "))
        print(value)

main()
