# exercise3.py
#       Write a program that determines the molecular weight of a hydrocarbon
#   based on the number of hydrogen, carbon, and oxygen atoms. You should
#   use the following weights:
#       H: 1.0079
#       C: 12.011
#       O: 15.9994

def main():
    print("This program determines the molecular weight of a hydrocarbon " +
          "based on the number of hydrogen, carbon, and oxygen atoms.\n")

    hWeight = 1.0079
    cWeight = 12.011
    oWeight = 15.9994
    
    hCount = eval(input("Enter the number of hydrogen atoms: "))
    cCount = eval(input("Enter the number of carbon atoms: "))
    oCount = eval(input("Enter the number of oxygen atoms: "))

    totalWeight = hCount * hWeight + cCount * cWeight + oCount * oWeight

    print("The hydrocarbon's weight is", totalWeight)

main()
