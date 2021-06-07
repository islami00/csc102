# Name
# StudentID
# Department
# CGPA
# Age
# Hobby
# nb: *args is a variable used to check the number of arguments in a function. Useful for the below
# also, **kwargs is also used to store key/value pairs of arguments , note: with either specified, you can run function
# with any number of variables
def capt(name=str(), std_id=int(), dpt=str(), cgpa=float(), age=int(), hobby=str(), *args, **kwargs):
    if len(kwargs) == 0 and len(args) == 0:
        name = input("Enter Name:")
        std_id = int(input("Enter Id:"))
        dpt = input("Enter Department:")
        cgpa = float(input("Enter CGPA:"))
        age = int(input("Enter Age:"))
        hobby = input("Enter hobby:")
        return {"name": name, "StudentID": std_id, "Department": dpt, "CGPA": cgpa, "Age": age, "Hobby": hobby}
    elif len(args) == 7:
        return {"name": name, "StudentID": std_id, "Department": dpt, "CGPA": cgpa, "Age": age, "Hobby": hobby}
    else:
        return "Insufficient Details, check source code"


# Now, the function is both static and dynamic as it can accept both no arguments for input and all for parsing

print(capt())
print(capt("Salim", 201103018, "Computer science", 5.0, 21, "Coding"))

# I WANT THIS TO WORK BASED ON THE NUMBER OF ARGUMENTS PASSED, TO SIMPY PRINT IF 5 ARGS AND DO NOTHING IF NOT UPTO FIVE
# AND ASK FOR INPUT IF NONE.
