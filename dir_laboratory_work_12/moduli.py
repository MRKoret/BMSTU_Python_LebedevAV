"""
Модуль с математическими функциями
"""

#import ...

__all__ = ['add', 'multiply', 'subtract']

#Константы
_pi = 3.14159

#Функции
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        raise ValueError("Делитель равен 0")
    else:
        return a/b


if __name__ == "__main__":
    print(add(6, 9))
    print(multiply(5, 12))
    print(divide(10, 2))
    print(subtract(50, 9))
    print(_pi)
else:
    print("Модуль базовых функций импортирован")
    print("-------------------------------------------")