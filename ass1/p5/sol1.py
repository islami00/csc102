# a break command terminates the loop it is directly inside, and moves to the code right after the loop
# a continue command terminates the current iteration of the loop it is directly inside and starts the
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