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
    # capture data
    form[key] = input("Enter " + key)
# clear screen
print("\n"*8)
# print form
for key, value in form.items():
    print(key, ":", value)

# if the qn is being literal, remove the key and release only the value
# lesson: check while for else if you'll be testing an instance of a loop to avoid running twice and your test being
# void
