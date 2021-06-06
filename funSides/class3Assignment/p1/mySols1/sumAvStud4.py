# approach two, dynamic entry, one by one using counter for logic test, and sum var for sum
# of course, there is compatibility issue in my code as it req a py version with delitem to work

ages = []
i = 0
s = 0
# error check one, good value input check, condition for age: must be a positive number <no age limit provided>
# there was problem converting this to a for loop as it only ran the specified no. of time, thus a while loop is best
# error check
# just realised i could use a variable to test the age then finally append it instead of appending directly
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
            s += ages[i]
            i += 1
            # tests for max input
        if i == 5:
            break
        else:
            continue
average = float(s / i)
print(s, average)
