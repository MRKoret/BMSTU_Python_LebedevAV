from math import *
x=float(input("Введите значение для x: "))
if x < -10:
    y = -3
    print(y)
if -10<=x<-8:
    y=-3
    print(y)
if x == -8 or x == 0:
    y =-3
    print(y)
if x == -3 or x==3:
    y=0
    print(y)
elif -8<x<-3:
    y = (3/5)*x + 9/5
    print(y)
elif -3<x<3 and x !=0:
    y = -sqrt(9-x**2)
    print(y)
elif x==5:
    y = 3
    print(y)
elif 3<x<5:
    y = x - 3
    print(y)
else:
    y = 3
    print(y)