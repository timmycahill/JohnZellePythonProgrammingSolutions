# exercise11.py
#       Heating and cooling degree-days are measures used by utility companies to estimate energy requirements. If
#   the average temperature for a day is below 60, then the number of degrees below 60 is added to the heating
#   degree-days. If the temperature is above 80, the amount over 80 is added to the cooling degree days. Write a
#   program that accepts a sequence of average daily temps and computes the running total of cooling and heating
#   degree-days. The program should print these two totals after all the data has been processed.

def main():
    # Introduction
    print("This program computes the running totals for cooling and heating degree-days.\n")
        
    # Read in a sequence of average daily temps
    temp = input("Enter the average daily temp (<Enter> to finish): ")

    coolingTotal = 0
    heatingTotal = 0
    while temp != "":
        # Compute running total of cooling and heating degree-days
        temp = eval(temp)
        if temp < 60:
            heatingTotal += 60 - temp
        elif temp > 80:
            coolingTotal += temp - 80

        # Read in next value
        temp = input("Enter the average daily temp (<Enter> to finish): ")   
    
    # Print totals
    print("\nHeating degree-days:", heatingTotal)
    print("Cooling degree-days:", coolingTotal)

if __name__ == "__main__":
    main()
