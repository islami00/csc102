
# list comprehension and f strings (yes, escape sequences are included):
ages=[int(input(f"Enter age #{i}: \n")) for i in range(1,6)]
print("The sum of the class age is:", sum(ages))
print("The average of the class age is:", sum(ages)/len(ages))