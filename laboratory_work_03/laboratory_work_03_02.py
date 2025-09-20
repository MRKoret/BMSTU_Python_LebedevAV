from math import *
from random import *

r=float(input("Введите значение для R: "))
flag=False
for n in range (10):
    x= uniform(-r,r)
    y= uniform(-r,r)
    if x <-r or x > r or y < -r or y > r:
        flag = False
    elif (-r<=x<=0 and 0<=y<=r) or (0<=x<r/2 and -2*x<=y<=0) or (r/2<=x<r and 2*x-2*r<=y<=0):
        flag = True
    else:
        flag = False
    print("{0: 7.2f} {1: 7.2f}".format(x, y), end=" ")
    if flag:
        print("Да")
    else:
        print("Нет")