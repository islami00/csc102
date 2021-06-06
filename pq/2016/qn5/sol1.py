fullName = input("Enter name: Format is firstName LastName\n")
name = fullName.split()
fname = name[0]
lastName = name[1]

for a in lastName:
    print(a)

print("Length of the last name:",len(lastName))
print(lastName.upper())
nFullName = fullName.replace(lastName, fname)
print(nFullName)
