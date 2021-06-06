name = input("Enter name:\n")
age = int(input("Enter age:\n"))
price = float(input("Enter price:\n"))
discAmount = 0.5 * price

print("Name:", name)
print("age:", age)
if age >= 65:
    print("Amount paid:", discAmount)
else:
    print("Amount paid:", price)
