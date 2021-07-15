name = input("Enter name\n").upper()
track = input("Enter letter to be counted\n").upper()

count = 0
for i in name:
    if i == track:
        count += 1
print("The occurrence of", track, "in", name, "is", count)
