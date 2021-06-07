Cels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
far = []
cF = dict()
# a dictionary is a compact way of making a 2d list
for C in Cels:
    cF[C] = cF.get(C, (9.0 / 5) * C + 32)

for k, v in cF.items():
    print(str(k) + "C", str(v) + "F")
