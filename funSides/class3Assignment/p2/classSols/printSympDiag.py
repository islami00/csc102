# sol 2 doesn't woork

s1 = input("Enter the first symptom:").lower()
s2 = input("Enter the second symptom:").lower()
s3 = input("Enter the third symptom:").lower()
# using a dict to store syns
# using set for dynamic check
syBook = {
    "Malaria": {"fever", "headache", "temperature"},
    "COVID-19": {"headache", "sore throat", "breathing challenge"},
    "Typhoid": {"fever", "cold", "headache"}
}

instructions = {
    "Malaria": "Go get some amartem",
    "COVID-19":"isolate yourself",
    "Typhoid": "get cleaner water"
}

# add another dict for diagnosis
for key, value in syBook.items():
    if syBook[key] == {s1, s2, s3}:
        print("you have",key, instructions[key])
        # give sth like print(syBook.diag)
        break
    elif key == list(syBook.keys())[-1]:
        print("Can't help you, sorry")
if {s1,s2,s3} in syBook.values():
    # this returns a regular list so it can be used for such checks instead of the previous vile method above
    print("Can't help you, sorry")