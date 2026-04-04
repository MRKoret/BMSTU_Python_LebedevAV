from math import sqrt, pi, sin, cos

__all__ = ['calculate_z1', 'calculate_z2', 'PI', 'SQRT2']

# Константы
PI = pi
SQRT2 = sqrt(2)

def calculate_z1(alpha):
    return cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)

def calculate_z2(alpha):
    return 2 * SQRT2 * cos(alpha) * sin((PI / 4) + 2 * alpha)

def print_table(alpha, z1, z2):
    print("I alpha Z I")
    print(f"|{alpha:7.2f} {z1:7.2f}|")
    print(f"|{alpha:7.2f} {z2:7.2f}|")

def main():
    print("Запуск лабораторной работы №1...")
    alpha = float(input("Введите значение для alpha (в радианах): "))

    z1 = calculate_z1(alpha)
    z2 = calculate_z2(alpha)

    print_table(alpha, z1, z2)
    print("Конец вывода")
    print("-------------------------------------------")
if __name__ == "__main__":
    main()
else:
    print("Модуль лабораторной работы №1 импортирован")
    print("-------------------------------------------")
    main()