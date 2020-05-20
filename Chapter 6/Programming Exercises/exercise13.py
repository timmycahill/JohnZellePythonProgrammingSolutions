# exercise13.py
#       Write and test a function to meet this specification:
#
#           toNumbers(strList): strList is a list of strings, each of which represents a number. Modfies each
#                               entry in the list by converting it to a number.

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])

def printDataTypes(dataList):
    for datum in dataList:
        print("{0} data type: {1}".format(datum, type(datum)))

def main():
    # Introduction
    print("This program convert a list of strings to a list of numbers.")

    # Get strings from user
    strList = []
    for i in range(10):
        string = input("Enter a number: ")
        strList.append(string)

    # Print data types before conversion
    print("\nOld Data Types:")
    printDataTypes(strList)

    # Convert strings to nums
    toNumbers(strList)

    # Print new data types
    print("\nNew Data Types:")
    printDataTypes(strList)

main()
