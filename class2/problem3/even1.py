# determine if a number is even or odd
# modulus is the best for testing this
n1 = int(input("Enter a number: "))
if (n1 % 2) == 0:
    print(n1, "is an even number")
else:
    print(n1, "is odd")
