# exercise1.py
#       As discussed in the chapter, string formatting could be used to
#   simplify the dateconvert2.py program. Go back and redo this program
#   making use of the string-formatting method.

def main():
    # get the day month and year
    day, month, year = eval(input("Enter the day, month, and year numbers: "))

    # Old code: date1 = str(month)+"/"+str(day)+"/"+str(year)
    date1 = "{0}/{1}/{2}".format(month, day, year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    # Old code: date2 = monthStr+" " + str(day) + ", " + str(year)
    date2 = "{0} {1}, {2}".format(monthStr, day, year)

    # Old code: print("The date is", date1, "or", date2+".")
    print("The date is {0} or {1}.".format(date1, date2))

main()
