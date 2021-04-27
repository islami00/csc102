# using filter X lambda
rate = 500

while True:
    currency = input("Enter the currency with $ for dollar, and # for naira, and '.' before cents or kobo\n")
    if "$" in currency:
        currency = ''.join((filter(lambda x:x.isdigit() or x == '.',currency)))  # join it takes an iterable and filter returns "iterable" type
        print(currency)
        converted = 500 * float(currency)
        print("Your Naira equivalent is:", "#"+str(converted))
        break
    if "#" in currency:
        currency =  ''.join((filter(lambda x:x.isdigit() or x == '.',currency)))
        converted = float(currency) / 500
        print("Your Dollar equivalent is:", "$"+str(converted))
        break
    else:
        print("Error! adhere to the following specification:")
