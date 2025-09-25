from math import *

R = float(input("Введите значение для радиуса R: "))
x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))

if -R<=x<=0 and 0<=y<=sqrt(R**2 - x**2):
    print("Точка внутри")
elif 0<=x<=R/2 and -2*x+R<=y<=0:
    print("Точка внутри")
elif R/2<=x<=R and 2*x-2*R<=y<=0:
    print("Точка внутри")
else:
    print("Точка снаружи")