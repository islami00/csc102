# break ends the current loop at that point and jumps to the following statement, useful replacement for skip

while True:
    line = input('>')
    if line == "Islam":
        break
    print(line)
print("Hi Islam!")
