f_hand = open("./Months and days of the year", "a")  # append mode
daysOfWeek = ["\n", "\nSunday\n", "Monday\n", "Tuesday\n", "Wednesday\n", "Thursday\n", "Friday\n", "Saturday"]
f_hand.writelines(daysOfWeek)
f_hand.close()
