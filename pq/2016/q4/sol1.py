import datetime

currentDate = str(datetime.datetime.today())
dDate = str(datetime.date(2016, 4, 23))

if dDate in currentDate:
    print("Sir, it is time to implement the module review")
