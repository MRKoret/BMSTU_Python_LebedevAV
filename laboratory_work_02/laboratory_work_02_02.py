R = float(input("Введите значение для радиуса R: "))
x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))

if -R<=x<=0 and 0<=y<=R:
    print("Внутри")
elif 0<=x<R/2 and -2*x<=y<=0:
    print("Внутри")
elif R/2<=x<R and 2*x-2*R<=y<=0:
    print("Внутри")
else:
    print("Снаружи")