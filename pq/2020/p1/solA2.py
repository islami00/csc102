# import math module so sine works
import math
# fix print and string formatting from g to s for string and fix print, and convert from radians to degrees
# (done with inbuilt here)for comfort
x = 1;print("sin(%s)=%s" % (x, math.sin(math.radians(x))))
# Assign before call in c assignment
A = 3; B = 2; C = A + B;print(C)
# fix 9. to avoid such issues, but it isn't a major syntax error
C = 21.0; F = 9.0*(C/5.0) + 32; print(F)
# changed to list for mutability
t = [2, 4, 6, "temp.pdf"]; t[1] = 4;print(t)
