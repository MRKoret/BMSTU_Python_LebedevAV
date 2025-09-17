from math import *

x=float(input("Введите значение для x: "))

if x <= -8:
    y = -3
elif -8 < x < -3:
    y = (3 / 5) * x + 9 / 5
if x == -3 or x==3:
    y=0
elif -3<x<3:
    y = -sqrt(9-x**2)
elif 3 < x < 5:
    y = x - 3
elif x==5:
    y = 3
else:
    y = 3

print("X = {0:.2f} Y = {1:.2f}".format(x, y))