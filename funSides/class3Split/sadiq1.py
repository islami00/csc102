# start
# since they said "number" i am assuming largest possible numeric set: floats
# inPrompt = "Input a number:"
while True:
    try:
        n = float(input("Input a number:"))
    except ValueError as error:
        print("Invalid input", error)

        # one arg to input() sacrifices too much, all comments show that parallel world
        # inPrompt = "Input a number:"  # the compromise
        # inPrompt: str = "Invalid input " + str(error) + "\n" + "Input a number:"  achieves same result with more code,
        # one prompt would be useful for many cases to reduce print()s
        continue
    else:
        if n <= 0:
            print("Note: Number must be greater than zero!")
            # inPrompt = "Input a number greater than zero:"
            continue
        else:
            print(n)
            break
# i wonder if i could add a condition to remove trailing zero of floats
