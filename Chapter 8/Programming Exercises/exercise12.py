# exercise12.py
#       Modify the previous problem to input from a file.

def main():
    # Introduction
    print("This program computes the running totals for cooling and heating degree-days.\n")

    try:
        # Read in file
        infileName = input("Enter the file name containing the data: ")
        infile = open(infileName, "r")
        
        # Read in a sequence of average daily temps
        temps = infile.readlines()

        coolingTotal = 0
        heatingTotal = 0
        for temp in temps:
            t = eval(temp)
            if t < 60:
                heatingTotal += 60 - t
            elif t > 80:
                coolingTotal += t - 80
        
        # Print totals
        print("\nHeating degree-days:", heatingTotal)
        print("Cooling degree-days:", coolingTotal)
    except FileNotFoundError:
        print("\nError: File not found.")
    except:
        print("\nAn unknown error has occurred.")

if __name__ == "__main__":
    main()
