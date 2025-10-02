from math import *
from random import *

n=int(input("Введите кол-во элементов в массиве: "))
if n > 30:
    n=30
elif n < 5:
    n=5

mas=[]
pol=[]
for i in range(n):
    mas.append(uniform(-5,5))
    if mas[i] > 0:
        pol.append(mas[i])
sp=sum(pol)

max1=max(mas)

print(mas)
print(pol)
print("Общая сумма положительных элементов массива =" + "{0:7.2f}".format(sp))
# print("Произведение элементов, расположенных между max и min =" + "{0:7.2f}".format())