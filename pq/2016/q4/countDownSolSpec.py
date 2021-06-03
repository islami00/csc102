# came from the "write a function" challenge on hackerrank
def is_leap(year):
    leap = False
    if (year % 4) == 0 and not (year % 100) == 0:
        leap = True
    elif (year % 400) == 0:
        leap = True
    else:
        leap = False
    return leap


getYear = int(input("Enter year:\n")) * (366 * 24 * 60)
getMonth = int(input("Enter month:\n"))
getDay = int(input("Enter day:\n")) * (24 * 60)
getHour = int(input("Enter hour:\n")) * 60
getMinute = int(input("Enter minute:\n"))
# could be more specific with months
if is_leap(getYear):
    feb = 29
else:
    feb = 28
# the above checks february's issue
# the below streamlines days of month
monthCons = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# there is a problem here cuz I am still searching for leap or not when he already told us!

for month in months:
    if getMonth == month:
        getMonth *= monthCons[months.index(month)] * 24 * 60

Time = getMinute + getHour + getDay + getMonth + getYear
yyyy = 2016 * (366 * 24 * 60)
mm = 12 * (30 * 24 * 60)
dd = 3 * (24 * 60)
hh = 13 * 60
MM = 13
final = yyyy + mm + dd + hh + MM

if Time >= final:
    print("sir, it is time for the review of the modules")
