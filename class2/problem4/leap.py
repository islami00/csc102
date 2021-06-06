# write a program to determine if a year is a leap year
# using the assumption that leap years happen every four years
year = int(input("Enter the year: "))

if (year % 4) == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")