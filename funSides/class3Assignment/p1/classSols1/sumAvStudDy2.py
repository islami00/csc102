ages = []

for c in range(5):
    age = int(input("Enter age:"))
    ages.append(age)
print("The sum of the class age is:", sum(ages))
print("The average of the class age is:", sum(ages)/len(ages))
