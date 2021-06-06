scores = open("files/Students_Scores.txt", "r")
sumScores = 0
count = 0
for score in scores:
    sumScores += int(score.strip())
    count += 1
average = sumScores / count
output = open("files/students_average.txt", "w")
outText = "The sum is: " + str(average) + "\n" + "The average is: " + str(sumScores)
output.write(outText)
