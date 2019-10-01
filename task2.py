from math import sqrt

x1 = input("Введіть значення x1")
x2 = input("Введіть значення x2")
x3 = input("Введіть значення x3")
print("x1="+x1)
x1=float(x1)
print("x2="+x2)
x2=float(x2)
print("x3="+x3)
x3=float(x3)
a = x1
b = x2
c = x3
dist1=sqrt((x2-x1)**2)
dist2=sqrt((x3-x1)**2)
if dist1>dist2:
    print("c ближче до а, ніж b")
if dist2>dist1:
    print("b ближче до а, ніж c")
if dist1==dist2:
    print("c на такій же відстані до а, як і b")