n = int(input("Enter number of numbers:"))

for count in range(n):
    no = int(input("Enter a number"))
    factorial = 1
    if no == 1 or no == 0:
        factorial = 1
    else:
        while no != 1:
            factorial *= no
            no -= 1
    print(factorial)
