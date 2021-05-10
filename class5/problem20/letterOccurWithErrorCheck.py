name = input("Enter name\n")
while True:
    track = input("Enter letter to be counted\n")
    if len(track) == 1:
        break
    else:
        print("Error! adhere to the following instruction!")
count = 0
for i in name:
    if i == track:
        count += 1
print("The occurrence of", track, "in", name, "is", count)
