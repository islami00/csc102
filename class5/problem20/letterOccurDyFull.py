name = input("Enter name\n")
track = input("Enter letter to be counted\n")

count = 0
for i in name:
    if i == track:
        count += 1
print("The occurrence of", track, "in", name, "is", count)
