# 5 unknowns
# names are known
# user insert name
# display inserted names
# dictionary and key would do for this

# create dictionary for form
form = {
    "First Name": str,
    "Last Name": str,
    "Age": int,
    "Gender": str,
    "Height": str
}

# iterate through for input
for key, value in form.items():
    # error flag for age
    while value == int:
        try:
            form[key] = int(input("Enter " + key))
        except ValueError as error:
            print("Invalid " + key, error)
            continue
        # logic test for age ; this is impractical for age limit test cuz the person can't get older then and
        # there, a condition should exist to make it move on.
        else:
            if form[key] < 0:
                # a qn could be included here to ask if they've reached age limit, then a blanket or input prompt
                # depending
                print("Age must be non-Negative!")
            else:
                break
    # capture data
    else:
        form[key] = input("Enter " + key)

# print form
for key, value in form.items():
    print(key, ":", value)
# if the qn is being literal, remove the key and release only the value
# lesson: check while for else if you'll be testing an instance of a loop to avoid running twice and your test being
# void
