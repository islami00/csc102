# with error check
grades = ["A", "B", "C", "D", "E", "F"]
wait = [5, 4, 3, 2, 1, 0]
# grade storer
listOfGrs = list()
# grade capture by sentinel
while True:
    grade = input("Enter grade, or n to stop")
    if grade == "n":
        break
    else:
        # convert letter to weight
        for g in grades:
            if grade.upper() == g:
                grade = wait[grades.index(g)]
                listOfGrs.append(grade)
                break
    continue

wSum = sum(listOfGrs)
wAverage = wSum / len(listOfGrs)
# scholarship is weight 4.5

if wAverage >= 4.5:
    msg = "\nDeserves scholarship"
else:
    msg = "\nDoes not deserve scholarship"
print("Weighted sum is:", wSum,"\nThe weighted average is:", round(wAverage, 2), msg)
