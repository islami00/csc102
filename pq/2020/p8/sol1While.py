# convert [0,10,20..100] using formula : F = (9.0/5)*C + 32, and while and for then single input function
# while loop
Cels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
far = []
while i < len(Cels):
    C = Cels[i]
    F = (9.0 / 5) * C + 32
    i += 1
    far.append(F)
print(Cels, far)
