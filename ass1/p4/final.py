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
