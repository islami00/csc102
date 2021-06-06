scores = open("files/Students_Scores.txt", "r")
s = 0
count = 0
for score in scores:
    s += int(score)
    count += 1
average = s / count
output = open("files/students_average.txt", "w")
outText = "The sum is: " + str(average) + "\n" + "The average is: " + str(s)
output.write(outText)
