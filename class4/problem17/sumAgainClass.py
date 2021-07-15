# You ar presented with the scores of 4 students in your department. Among the task that is expected of you on the
# student scores are as follows:
#1. get score  from students
number = 4
scores = [int(input("Enter a number: ")) for x in range(number)]
# 2. compute sum
sum_Scores = sum(scores)
# 3. compute average
avg_scores = sum_Scores/len(scores)