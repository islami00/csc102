# #QUESTION ONE
# #B)
# # The three basic constructs are:
# # 1. Sequential
# #   The commands in this construct are to be executed one by one, without skipping any.
# #   .e.g:
# n = 5
# print(n)
# #  the program outputs 5 as it assigns n then prints it
# #2. Conditional
# #  This is a programming construct wherein the commands or a group of code is executed based on a condition that
# #  evaluates to true or false. e.g
# a = 5
# print("B")
# if a < 2:
#     print(a)
# if 2 < a:
#     print(2)
# #  It can be one-way: wherein there is only one block of code that is run if the condition is true (like the example
# #  above which gives B then 2 as 5<2)
# #  or two way: either of two blocks of code are run depending on the condition resolving to true or false,e.g:
# if 1 > 2:
#     print(1)
# else:
#     print(2)
# #  this outputs 2 as the previous condition was not met
#
# #  or multi way: wherein conditions are nested in themselves,i.e if one evaluates to false, test the other - a mix
# #  of one-way and two-way.
# if 1 > 2:
#     print(1)
# elif 2 > 3:
#     print(2)
# else:
#     print(99)
# #  This outputs 99 as none of the previous conditions were met.
#
# #3. Iterative
# #  This is a programming construct wherein a group of code is repeated due to a condition (boolean expression),
# #  that is usually tested on each instance of a changing variable known as an iterable or "iteration variable".
# #  This iterable could be a container of multiple values e.g set, or a datatype that allows multiple sub-instances
# #  e.g a string. Each time the code is run is called an iteration
# #  An iteration is usually triggered by a boolean expression, which is a statement that evaluates to true or false.
# #  It is a high level application of conditional programming to allow the same condition and code to be evaluated more
# #  than once for similar items with less code.
#
# #  This is also called "looping", and such sections of a program are called loops. They can be finite or infinite.
# #  Finite loops run contain a known number of iterations, and are useful for data sets that are relatively
# #  static. e.g for loop:
# for x in "strng":
#     print(x) # this prints each letter of strng on separate lines
# #  Infinite loops run till a terminal value is entered in the loop, or till a condition is false, these are good for
# #  error handling or generally, conditions where the data set is entered dynamically.
# #  The number of iterations is unknown before execution.
# #  e.g: while loop:
# i = 0
# while i < 4:
#     print(i)
#     i+=1  # iterable being changed
# # this gives 0-3 on separate lines
#
# #b)
r1 = float(input("Enter radius:"))
r2 = float(input("Enter radius:"))
r3 = float(input("Enter radius:"))

print("smallest:", min(r1, r2, r3))
print("biggest:", max(r1, r2, r3))

# QUESTION TWO

