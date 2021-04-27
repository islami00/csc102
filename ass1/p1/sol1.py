# The three basic constructs are:
# 1. Iterative
#   This is a programming construct where in a group of code is executed continuously over the instances of
#   a changing variable known as an iterable , this iterable could be a container of multiple data types e.g set, or a
#   datatype that allows multiple sub-instances e.g a string. It is usually triggered by a boolean condition, which is
#   an expression that uses the iterable this is a high level application of the conditional programming to
#   allow the same condition to be evaluated more than once for different items without having to start
#   a new instance of the program.
#   Iterative programs consist of constructs called "loops" which perform the function above, and can be either infinite
#   or finite. Finite loops run for a predetermined number of times and are useful for data sets that do not change
#   infinite loops run till a terminal value is entered in the loop, or till a condition is false, these are good for
#   error handling or generally, conditions where the data set is entered dynamically.
#     .
# 2. Conditional
#   This is a programming construct wherein a group of code is executed when a boolean expression evaluates to true
#   or not executed at all. i.e the code runs when a condition is met.
#   It can be one-way: where in there is only one block of code that is run if the condition is true,
#   or two way: where in there is another block of code that is run if the condition is false,
#   or multi way:
#   wherein conditions are nested in themselves,i.e if one evaluates to false or
#   true(but usually false), test the other - a mix of one-way and two-way. It consists of conditional jumps or "skips"
#   of a series of instructions in a program.
# 3. Sequential
#   This is linear programming, i.e The program written evaluates step by step, without skipping any steps
#   .
#

r1 = float(input())
r2 = float(input())
r3 = float(input())

print("smallest:", min(r1, r2, r3))
print("biggest:", max(r1, r2, r3))
