import re

rate = 500
while True:
    currency = input("Enter the currency with $ for dollar, and # for naira, and '.' before cents or kobo\n")
    if "$" in currency:
        currency = re.sub("[^\d.]", "", currency)  # match all that are not numeric decimals or "."
        converted = 500 * float(currency)
        print("Your Naira equivalent is:", "#"+str(converted))
        break
    if "#" in currency:
        currency = re.sub("[^\d.]","",currency)
        converted = float(currency) / 500
        print("Your Dollar equivalent is:", "$"+str(converted))
        break
    else:
        print("Error! adhere to the following specification:")
