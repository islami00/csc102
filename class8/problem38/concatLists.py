computer = list()
software = list()
# append is a method used to add values to the list object
computer.append("Aisha")
computer.append("James")
software.append("Chichi")
software.append("Ola")

concat = software + computer
# this is strictly ordered and not commutative i.e list(A) + list(b) != list(b) + list(a)

print(concat)

# all list methods: methods = dir(list)
