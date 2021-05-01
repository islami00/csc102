# QUESTION ONE
#
# The three basic constructs are:
# 1. Sequential
#   The commands in this construct are to be executed one by one, without skipping any.
#   .
#
# 2. Conditional
#   This is a programming construct wherein the commands or a group of code is executed based on a condition that
#   evaluates to true or false.
#
#   It can be one-way: wherein there is only one block of code that is run if the condition is true,
#   or two way: there is another block of code that is run if the condition is false,
#   or multi way: wherein conditions are nested in themselves,i.e if one evaluates to false or, test the other - a mix
#   of one-way and two-way.
#
#   It generally consists of conditional jumps or "skips" of a series of instructions in a program.

# 3. Iterative
#   This is a programming construct wherein a group of code is repeated due to a condition (boolean expression),
#   or over each instance of a changing variable known as an iterable or "iteration variable". This iterable could be
#   a container of multiple values e.g set, or a datatype that allows multiple sub-instances e.g a string.
#   Each time the code is run is called an iteration
#   Iterations is usually triggered by a boolean expression, which is a statement that evaluates to true or false.
#   It is a high level application of conditional programming to allow the same condition and code to be evaluated more
#   than once for similar items with less code.
#
#   This is also called "looping", and such sections of a program are called loops. They can be finite or infinite.
#   Finite loops run contain a known number of iterations, and are useful for data sets that are relatively
#   static. e.g for loop
#   Infinite loops run till a terminal value is entered in the loop, or till a condition is false, these are good for
#   error handling or generally, conditions where the data set is entered dynamically.
#   The number of iterations is unknown before execution.

# b)
r1 = float(input("Enter radius:"))
r2 = float(input("Enter radius:"))
r3 = float(input("Enter radius:"))

print("smallest:", min(r1, r2, r3))
print("biggest:", max(r1, r2, r3))


# QUESTION TWO
#
#