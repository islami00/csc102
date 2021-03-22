# 3 unknowns
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
# we compare using if
# if ni<i being it's order> is greater than the other i, it is the largest
if n1 < n2 and n1 < n3:
    smallest = n1
elif n2 < n1 and n2 < n3:
    smallest = n2
# else the last number is the largest
else:
    smallest = n3
print(smallest, "is the smallest")
# i feel this can be applied in an array, looping and somehow adding the and(s) to test the numbers
# ctrl+shift+A if pycharm does sth unexpected due to us hitting an unknown command
