from math import *

x=float(input("Введите значение для alpha: "))
y1 = cos(x)+sin(x)+cos(3*x)+sin(3*x)
y2 = 2*sqrt(2)*cos(x)*sin((pi/4)+2*x)

print("Результат первых вычислений: ", y1)
print("Результат вторых вычислений: ", y2)