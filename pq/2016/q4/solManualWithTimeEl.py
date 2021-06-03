todayDate = input("Enter today's date, Format: dd-MM-yyyy\n")
todayTime = input("Enter the time, Format: hh:mm AM/PM\n")
today = (todayDate, todayTime,)
# simple error check for single-digit months, same can be done for single-digit days too
dDate = "23-04-2016", "23-4-2016"
# time module added
date = [(a, "5:27 AM") for a in dDate]
if today in date:
    print("sir, it is time to implement the module")
