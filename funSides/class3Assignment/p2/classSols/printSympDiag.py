# sol 2 doesn't woork

s1 = input("Enter the first symptom:")
s2 = input("Enter the second symptom:")
s3 = input("Enter the third symptom:")
# using a dict to store syns
# using set for dynamic check
syBook = {
    "Malaria": {"fever", "headache", "temperature"},
    "COVID - 19": {"Headache", "Sore throat", "breathing challenge"},
    "Typhoid": {"fever", "cold", "headache"}
}

# add another dict for diagnosis
for key, value in syBook.items():

    if syBook[key] is {s1, s2, s3}:
        print(syBook[key])
        # give sth like print(syBook.diag)
else:
    "Cant help you, sorry"
