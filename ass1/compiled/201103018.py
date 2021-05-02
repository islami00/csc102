# #QUESTION ONE
# #A)
# # The three basic constructs are:
# # 1. Sequential
# #   The commands in this construct are executed one by one, without skipping any.
# #   .e.g:
# n = 5
# print(n)
# #  the program outputs 5 as it assigns n then prints it
# #2. Conditional
# #  This is a programming construct wherein the commands or groups of code are executed based on a condition that
# #  evaluates to true or false (boolean expression). e.g
# a = 5
# print("B")
# if a < 2:
#     print(a)
# if 2 < a:
#     print(2)
# #  It can be one-way: wherein there is only one block of code that is run if the condition is true (like the example
# #  above which gives B then 2 as 2<5)
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
# #  This is a programming construct wherein a group of code is repeated. It involves a boolean expression,
# #  that is usually tested on each instance of a changing variable known as an iterable or "iteration variable".
# #  This iterable could be a container of multiple values e.g set, or a datatype that allows multiple sub-instances
# #  e.g a string. Each time the code is run is called an iteration.
# #  It is a high level application of conditional programming to allow the same condition and code to be evaluated more
# #  than once for similar items with less code.
#
# #  This is also called "looping", and such sections of a program are called loops. They can be finite or infinite.
# #  Finite loops run for a known number of iterations, and are useful for data sets that are relatively
# #  static. e.g: for loop:
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
# #B)
r1 = float(input("Enter radius:"))
r2 = float(input("Enter radius:"))
r3 = float(input("Enter radius:"))

print("smallest radius:", min(r1, r2, r3))
print("biggest radius:", max(r1, r2, r3))

# # QUESTION TWO
def my_function(v=5):
    v + 10
    return v + 10
my_function()
print(my_function())
# changed the first, third and last line.
# on the first: The "==" was changed to "=" for assignment,
# then a colon was added after the bracket to complete the declaration
# on the third: the return was indented and made to return the increment, fixing the indentation syntax error, and the
# logic error that is v not being incremented.
# on the last: the function was called in directly in print as v is not a global variable.

# # QUESTION THREE
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if (i % 5 != 0) and (i % 3 != 0):
        print(i)

#  # QUESTION FOUR

# wordings
specs = "Enter the amount of cash with: $ for dollar, and # for naira.\n"
DotWarning = "\nError! one too many decimal points!\n" \
             "NOTE: You can enter coin values separately in the next prompt after cash instead of entering them" \
             " as decimal\n"
SpecWarning = "Error! adhere to the following specification:"


# input formatting
def cur_format(money):
    a = ''.join((filter(lambda x: x.isdigit() or x == '.', money)))
    if a == "" or a == ".":
        return 0
    else:
        return a


rate = 500

# program instance
while True:
    currency = input(specs)
    if currency.count(".") > 1:
        print(DotWarning)
    elif ('$' in currency) and ('#' in currency):
        print(SpecWarning)
    elif '$' in currency:
        cur_den = input("Enter the amount of cents:")
        cur_den = float(cur_format(cur_den))
        currency = float(cur_format(currency))
        cur_den /= 100.0
        converted = (currency + cur_den) * rate
        print("Your Naira equivalent is:", "#{:,.2f}".format(converted))  # format does rounding
        break
    elif '#' in currency:
        cur_den = input("Enter the amount of Kobo:")
        cur_den = float(cur_format(cur_den))
        currency = float(cur_format(currency))
        cur_den /= 100.0
        converted = (currency + cur_den) / rate
        print("Your Dollar equivalent is:", "${:,.2f}".format(converted))
        break
    else:
        print(SpecWarning)

#  # QUESTION FIVE
# The break command terminates the loop it is directly inside, and moves to the code right after the loop
# The continue command terminates the current iteration of the loop it is directly inside and starts the
# next iteration, or exits the loop if it is at the last iteration

for val in "string":
    if val == "i":
        break
    print(val)
print("The end")

# sample output:
# s
# t
# r
# The end

for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")

# sample output:
# s
# t
# r
# n
# g
# The end
