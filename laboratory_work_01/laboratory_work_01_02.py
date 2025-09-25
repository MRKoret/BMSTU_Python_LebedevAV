from math import *

x=float(input("Введите значение для alpha: "))
y1 = cos(x)+sin(x)+cos(3*x)+sin(3*x)
y2 = 2*sqrt(2)*cos(x)*sin((pi/4)+2*x)

print("I    X         Z     I")
print("I{0: 7.2f}  {1: 7.2f}    I".format(x, y1))
print("I{0: 7.2f}  {1: 7.2f}    I".format(x, y2))