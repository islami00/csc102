def capt(name, std_id, dpt, cgpa, age, hobby):
    return {"name": name, "StudentID": std_id, "Department": dpt, "CGPA": cgpa, "Age": age, "Hobby": hobby}


# this was all they wanted, sth that captures those details in that order, and i've given em that. Left to them
# to do as they wish with it

capt(str(input("Enter name")), int(input("Enter studentID")), str(input("Enter Department")),
     float(input("Enter CGPA")), int(input("Enter Age")), str(input("Enter Hobby")))
