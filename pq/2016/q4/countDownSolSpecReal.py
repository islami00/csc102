getYear = int(input("Enter year:\n")) * (366 * 24 * 60)
getMonth = int(input("Enter month:\n"))
getDay = int(input("Enter day:\n")) * (24 * 60)
getHour = int(input("Enter hour:\n")) * 60
getMinute = int(input("Enter minute:\n"))

# for the days in the month
monthCons = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for month in months:
    if getMonth == month:
        getMonth *= monthCons[months.index(month)] * 24 * 60
# current time
Time = getMinute + getHour + getDay + getMonth + getYear

# due time
yyyy = 2016 * (366 * 24 * 60)
mm = 12 * (31 * 24 * 60)
dd = 3 * (24 * 60)
hh = 13 * 60
MM = 13
final = yyyy + mm + dd + hh + MM

if Time >= final:
    print("Sir, it is time for the review of the modules")
