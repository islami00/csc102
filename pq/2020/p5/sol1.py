# with error check
grades = ["A", "B", "C", "D", "E", "F"]
wait = [5, 4, 3, 2, 1, 0]
# grade storer
lisOfG = list()
# grade capture by sentinel
while True:
    grade = input("Enter grade, or n to stop")
    if grade == "n":
        break
    else:
        for g in grades:
            if grade.upper() == g:
                grade = wait[grades.index(g)]
                lisOfG.append(grade)
                break
            elif grade.upper() > "F":
                grade = 0
                break
wSum = sum(lisOfG)
wAverage = wSum / len(lisOfG)
# scholarship is weight 4.5

if wAverage >= 4.5:
    msg = "Deserves scholarship"
else:
    msg = "Does not deserve scholarship"
print("Weighted sum is:", wSum, "\n", "The weighted average is:", round(wAverage,2), "\n", msg)
