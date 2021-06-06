spec = "Enter score or -1 to stop\n"
a = int(input(spec))
scores = []

while a != -1:
    scores.append(a)
    a = int(input(spec))
    continue
print(sum(scores))
print(sum(scores)/len(scores))
