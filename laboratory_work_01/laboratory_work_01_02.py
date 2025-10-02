# 1. Ограничить импортируемые функции только теми, что указаны в тексте программы и отчете.
# 2. Исправить текст программы в соответствии с требованиями Руководства по стилю кода Python
# (https://peps.python.org/pep-0008/).
from math import sqrt, pi, sin, cos # для решения данной задачи требуется только функции корня, числа пи, синуса и косинуса


alpha = float(input("Введите значение для alpha: "))

z1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)
z2 = 2 * sqrt(2) * cos(alpha) * sin((pi / 4) + 2 * alpha)

print("I    Alpha     Z     I")
print("I{0: 7.2f}  {1: 7.2f}    I".format(alpha, z1))
print("I{0: 7.2f}  {1: 7.2f}    I".format(alpha, z2))