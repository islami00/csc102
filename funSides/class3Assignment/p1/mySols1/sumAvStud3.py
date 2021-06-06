# approach two, dynamic entry, one by one using counter for logic test
# of course, there is compatibility issue in my code as it req this py version to work.

ages = []
i = 0

# error check one, good value input check, condition for age: must be a positive number <no age limit provided>
while True:
    try:
        ages.append(int(input("Enter age:")))
    except ValueError as error:
        print("Invalid Input!", error)
        continue
    # got confused here, so code got tacky...tests for age logic error
    else:
        if ages[i] < 0:
            print("The age must be non-negative!")
            ages.__delitem__(i)
            continue
        else:
            i += 1
    # tests for max input
        if i == 5:
            break
        else:
            continue

totalAge = sum(ages)
average = float(totalAge / i)
print(totalAge, average)
