# input full name
fullName = input("Enter your full name\nFormat: First,Last").strip()
# print first name
firstName = ""
for i in fullName:
    if i == " ":
        firstName = fullName[0:fullName.index(i)]
        break
print(firstName)
# last n letter picker


def last_n_of_name(name, name_index, char_no):
    name = list(name.split())
    neededName = name[name_index]
    return neededName[(len(neededName) - char_no):len(neededName)]


# print last 3 characters of last name
print(last_n_of_name(fullName, 1, 3))

# concat last 2 char of first and last names
lF = last_n_of_name(fullName, 0, 2)
lL = last_n_of_name(fullName, 1, 2)
print(lF + lL)
