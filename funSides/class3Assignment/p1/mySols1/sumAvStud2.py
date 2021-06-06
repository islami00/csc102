# approach two, dynamic entry, one by one
# of course, there is compatibility issue in my code as it req this py version to work.

ages = []

# error check one, good value input check, condition for age: must be a positive number <no age limit provided>
while True:
    try:
        ages.append(int(input("Enter age:")))
    except ValueError as error:
        print("Invalid Input!", error)
        continue
    # got confused here, so code got tacky...tests for age logic error
    else:
        for n in ages:
            if n < 0:
                print("The age must be non-negative!")
                # i am leaving this here cuz i want to remember delitem
                ages.__delitem__(ages.index(n))
                break
            else:
                continue
    # tests for max input
    if len(ages) == 5:
        break
    else:
        continue

totalAge = sum(ages)
average = float(totalAge / len(ages))
print(totalAge, average)
