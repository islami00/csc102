def facto(number):
    number = int(number)
    if number <= 1:
        return 1
    else:
        return number * facto(number - 1)

# note: f strings don't allow escape sequences in substrings


print(f"{facto(input('Enter a number:'))} is the factorial")
