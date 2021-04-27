rate = 500
while True:
    currency = input("Enter the currency with $ for dollar, and # for naira, and '.' before cents or kobo\n")
    if "$" in currency:
        currency = ''.join(i for i in currency if (i.isdigit() or i == '.'))
        # join converts the iterable to a string, each element seperated by ''
        converted = 500 * float(currency)
        print("Your Naira equivalent is:", "#" + str(converted))
        break
    if "#" in currency:
        currency = ''.join(i for i in currency if (i.isdigit() or i == '.'))
        converted = float(currency) / 500
        print("Your Dollar equivalent is:", "$" + str(converted))
        break
    else:
        print("Error! adhere to the following specification:")
