scores = open("files/Students_Scores.txt", "r")
scores = list(map(int, list(scores)))
output = open("files/students_average.txt", "w")
outText = "The sum is: " + str(sum(scores)) + "\n" + "The average is: " + str(sum(scores) / len(scores))
output.write(outText)
#  learned two things: 1. int ignores whitespace at end of line. Opened File is consumed after accessed
