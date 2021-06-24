# used similar solution to him

fact = 1
number = int(input("Enter number"))

if number < 0:
    print("Undefined")
elif number == 1 or number == 0:
    print("1")
else:
    for i in range(2, number + 1):
        fact *= i
print(fact)
