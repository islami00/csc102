no = []
# this is really an empty list, and this emptiness does not count as an element
# no python element can be dynamically created by index. rather, by appending
while True:
    try:
        maxNo = int(input("How many numbers?"))
    except ValueError as error:
        print("Invalid Input!", error)
    else:
        if maxNo < 0:
            print("The amount of numbers must be non-negative!")
            continue
        else:
            break
while True:
    try:
        no.append(int(input("Enter a number:")))
    except ValueError as error:
        print("Invalid Input!", error)
        continue
    if len(no) == maxNo:
        break

smallest = None
for n in no:
    # yup, for loop goes once before checking it's actual condition.
    if smallest is None:
        smallest = n

    elif n < smallest:
        smallest = n

print(smallest)

# this is one approach, taking the no.s one by one

# another approach would be taking a list directly as input, yet another would be taking it from file.
