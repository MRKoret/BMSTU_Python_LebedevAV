# 1. Удалить из текста программы инструкции по импорту неиспользуемых библиотек.
# 2. Исправить текст программы в соответствии с требованиями Руководства по стилю кода Python
# (https://peps.python.org/pep-0008/).
# 3. Исправить отчет в соответствии с методическими указаниями в шаблоне отчета
# (см. файл template_laboratory_report_00.ott).

# from math import * Для решения данной задачи библеотека math не нужна
from random import *

r=float(input("Введите значение для R: "))
flag=False
print("I   X   I   Y   I Попадание I")
for n in range (10):
    x= uniform(-r,r)
    y= uniform(-r,r)
    if x <-r or x > r or y < -r or y > r:
        flag = False
    elif (-r<=x<=0 and 0<=y<=r) or (0<=x<=r/2 and -2*x+r<=y<=0) or (r/2<=x<=    r and 2*x-2*r<=y<=0):
        flag = True
    else:
        flag = False
    print("{0: 7.2f} {1: 7.2f}".format(x, y), end="      ")
    if flag:
        print("Да")
    else:
        print("Нет")
    print("I-------I-------I-----------I")