# sentinel value is zero

score = int(input("Enter the student score:"))
add = 0
count = 0

while score != 0:
    add += score
    count += 1
    score = int(input("Enter the student score:"))

print("The sum of the students is ", add)
print("The average call is ", add / count)

# can use a list for this, but it honestly doesnt matter
