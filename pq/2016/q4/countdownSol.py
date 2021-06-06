getYear = int(input("Enter year:\n")) * (366 * 24 * 60)
getMonth = int(input("Enter month:\n")) * (30 * 24 * 60)
getDay = int(input("Enter day:\n")) * (24 * 60)
getHour = int(input("Enter hour:\n")) * 60
getMinute = int(input("Enter minute:\n"))
# could be more specific with months

Time = getMinute + getHour + getDay + getMonth + getYear

yyyy = 2016 * (366 * 24 * 60)
mm = 12 * (30 * 24 * 60)
dd = 3 * (24 * 60)
hh = 13 * 60
MM = 13
final = yyyy + mm + dd + hh + MM

if Time >= final:
    print("sir, it is time for the review of the modules")
