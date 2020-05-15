# File: exercise7.py
#
# (Advanced) Modify the chaos program so that it accepts two inputs and
# then prints a table with two columns simliar to the one shown in Section
# 1.8. (Note: You will probably not be able to get the columns to line
# up as nicely as those in the example. Chapter 5 discusses how to print
# numbers with a fixed number of decimal places.)

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    print("input\t", x, "\t\t\t", y)
    print("-----------------------------------------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("\t", x, "\t", y)

main()
