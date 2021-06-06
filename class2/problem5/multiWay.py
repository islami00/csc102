# adding grades

score = int(input("enter your final score"))
# In class we used :
#
# elif score >=40 and score <45
#   print("Your grade is E")
# to test
if score >= 70:
    grade = 'A'
elif 60 <= score < 70:
    grade = 'B'
elif 50 <= score < 60:
    grade = 'C'
elif 45 <= score < 50:
    grade = 'D'
elif 40 <= score < 45:
    grade = 'E'
else:
    grade = 'F'

print("Your grade is", grade)

# what if the student gives an invalid response e.g score >100 or string
