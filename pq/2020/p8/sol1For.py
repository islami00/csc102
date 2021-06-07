# convert [0,10,20..100] using formula : F = (9.0/5)*C + 32, and while and for then single input function
# while loop
Cels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
far = []
for C in Cels:
    F = (9.0 / 5) * C + 32
    far.append(F)
print(Cels, far)
