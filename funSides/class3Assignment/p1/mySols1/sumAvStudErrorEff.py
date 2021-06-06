# going by the logic that the most efficient has least chars and vars <note i eliminated the counter that was used
# for error checking logical in while

# shortest with error checking

# approach two, dynamic entry, one by one
# little compatibility issue.

ages = []

# error check one, good value input check, condition for age: must be a positive number <no age limit provided>
while len(ages) < 5:
    try:
        age = int(input("Enter age:"))
    except ValueError as error:
        print("Invalid Input!", error)
        continue
    else:
        # logic age test
        if age < 0:
            print("The age must be non-negative!")
            continue
        else:
            ages.append(age)
    # can't test be at while?

# left this as is, cuz it is more readable
totalAge = sum(ages)
average = float(totalAge / len(ages))
print(totalAge, average)
