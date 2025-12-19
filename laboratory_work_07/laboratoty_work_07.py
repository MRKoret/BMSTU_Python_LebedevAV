import turtle
import math

# Настройки окна
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Координатная система с графиком")
screen.bgcolor("white")

# Создаем черепашку для осей
axes = turtle.Turtle()
axes.speed(0)
axes.pensize(1)
axes.color("black")

# Создаем черепашку для графика
graph = turtle.Turtle()
graph.speed(0)
graph.pensize(2)
graph.color("blue")

# Настройки масштабирования
x_min, x_max = -10, 8
y_min, y_max = -4, 4
width, height = 700, 500  # Размеры области рисования


# Функция для преобразования математических координат в экранные
def scale_point(x, y):
    # Преобразуем координаты так, чтобы (0,0) был в центре экрана
    x_scale = width / (x_max - x_min)
    y_scale = height / (y_max - y_min)

    x_scaled = (x - x_min) * x_scale - width / 2
    y_scaled = (y - y_min) * y_scale - height / 2
    return x_scaled, y_scaled


# Рисуем оси координат с центром в (0,0)
def draw_axes():
    # Поднимаем перо
    axes.penup()

    # Рисуем ось X (горизонтальная линия через y=0)
    # Начинаем от самой левой точки (x_min, 0) до самой правой (x_max, 0)
    start_x, start_y = scale_point(x_min, 0)
    end_x, end_y = scale_point(x_max, 0)

    axes.goto(start_x, start_y)
    axes.pendown()
    axes.goto(end_x, end_y)

    # Стрелка для оси X
    axes.penup()
    axes.goto(end_x - 10, end_y + 5)
    axes.pendown()
    axes.goto(end_x, end_y)
    axes.goto(end_x - 10, end_y - 5)

    # Рисуем ось Y (вертикальная линия через x=0)
    # Начинаем от самой нижней точки (0, y_min) до самой верхней (0, y_max)
    axes.penup()
    start_x, start_y = scale_point(0, y_min)
    end_x, end_y = scale_point(0, y_max)

    axes.goto(start_x, start_y)
    axes.pendown()
    axes.goto(end_x, end_y)

    # Стрелка для оси Y
    axes.penup()
    axes.goto(end_x - 5, end_y - 10)
    axes.pendown()
    axes.goto(end_x, end_y)
    axes.goto(end_x + 5, end_y - 10)

    # Подписи осей
    axes.penup()
    # Подпись для оси X
    label_x, label_y = scale_point(x_max - 0.5, -0.5)
    axes.goto(label_x, label_y)
    axes.write("X", align="center", font=("Arial", 12, "normal"))

    # Подпись для оси Y
    label_x, label_y = scale_point(0.5, y_max - 0.3)
    axes.goto(label_x, label_y)
    axes.write("Y", align="center", font=("Arial", 12, "normal"))

    # Только 0 в центре
    zero_x, zero_y = scale_point(0, 0)
    axes.penup()
    axes.goto(zero_x + 5, zero_y - 15)
    axes.write("0", align="left", font=("Arial", 10, "normal"))

    # Деления на осях
    # Деления на оси X (только целые числа)
    for i in range(int(x_min), int(x_max) + 1):
        if i != 0:  # Пропускаем 0, чтобы не задеть центр
            x_pos, y_pos = scale_point(i, 0)
            axes.penup()
            axes.goto(x_pos, y_pos - 5)
            axes.pendown()
            axes.goto(x_pos, y_pos + 5)
            axes.penup()
            axes.goto(x_pos, y_pos - 20)
            axes.write(str(i), align="center", font=("Arial", 8, "normal"))

    # Деления на оси Y (только целые числа)
    for i in range(int(y_min), int(y_max) + 1):
        if i != 0:  # Пропускаем 0, чтобы не задеть центр
            x_pos, y_pos = scale_point(0, i)
            axes.penup()
            axes.goto(x_pos - 5, y_pos)
            axes.pendown()
            axes.goto(x_pos + 5, y_pos)
            axes.penup()
            axes.goto(x_pos + 10, y_pos - 5)
            axes.write(str(i), align="center", font=("Arial", 8, "normal"))

    axes.hideturtle()


# Рисуем первую часть графика: y = -3 для x <= -8
def draw_first_part():
    graph.penup()

    # Начинаем с точки (-10, -3)
    start_x, start_y = scale_point(-10, -3)
    graph.goto(start_x, start_y)
    graph.pendown()

    # Рисуем горизонтальную линию до x = -8
    # Используем 200 точек для плавности
    for i in range(201):
        x = -10 + (i / 200.0) * 2  # От -10 до -8
        if x <= -8:
            x_scaled, y_scaled = scale_point(x, -3)
            graph.goto(x_scaled, y_scaled)


# Рисуем вторую часть графика: y = (3/5)x + 9/5 для -8 < x < -3
def draw_second_part():
    # Продолжаем рисовать (перо уже опущено)

    # Рисуем линейную функцию от x = -8 до x = -3
    # Используем 200 точек для плавности
    for i in range(201):
        x = -8 + (i / 200.0) * 5  # От -8 до -3
        if x < -3:  # Строго меньше -3
            y = (3 / 5) * x + 9 / 5  # y = 0.6*x + 1.8
            x_scaled, y_scaled = scale_point(x, y)
            graph.goto(x_scaled, y_scaled)


# Рисуем третью часть графика: y = -sqrt(9 - x^2) для -3 <= x < 3
def draw_third_part():
    # Проверяем значение в точке x = -3
    # Из второй части: при x → -3⁻, y = (3/5)*(-3) + 9/5 = -9/5 + 9/5 = 0
    # Из третьей части: при x = -3, y = -sqrt(9 - 9) = 0
    # Значения совпадают, график непрерывен

    # Рисуем нижнюю половину окружности от x = -3 до x = 3
    # Используем 400 точек для плавности
    for i in range(401):
        x = -3 + (i / 400.0) * 6  # От -3 до 3
        if x < 3:  # Строго меньше 3
            # Вычисляем y = -sqrt(9 - x^2)
            try:
                y = -math.sqrt(9 - x ** 2)
                x_scaled, y_scaled = scale_point(x, y)
                graph.goto(x_scaled, y_scaled)
            except ValueError:
                # Пропускаем точки, где 9 - x^2 < 0
                continue


# Рисуем четвертую часть графика: y = x - 3 для 3 <= x < 5
def draw_fourth_part():
    # Проверяем значение в точке x = 3
    # Из третьей части: при x → 3⁻, y = -sqrt(9 - 9) = 0
    # Из четвертой части: при x = 3, y = 3 - 3 = 0
    # Значения совпадают, график непрерывен

    # Рисуем линейную функцию от x = 3 до x = 5
    # Используем 200 точек для плавности
    for i in range(201):
        x = 3 + (i / 200.0) * 2  # От 3 до 5
        if x < 5:  # Строго меньше 5
            y = x - 3
            x_scaled, y_scaled = scale_point(x, y)
            graph.goto(x_scaled, y_scaled)


# Рисуем пятую часть графика: y = 3 для x >= 3 (начиная с x = 3)
def draw_fifth_part():
    # Сначала поднимаем перо и перемещаемся к точке (3, 0)
    graph.penup()
    x, y = scale_point(3, 0)
    graph.goto(x, y)
    graph.pendown()

    # Теперь рисуем горизонтальную линию y = 3 от x = 3 до x = 8
    # Используем 200 точек для плавности
    for i in range(201):
        x_val = 3 + (i / 200.0) * 5  # От 3 до 8
        if x_val <= x_max:  # Не выходим за пределы графика
            x_scaled, y_scaled = scale_point(x_val, 3)
            graph.goto(x_scaled, y_scaled)


# Основная программа
draw_axes()  # Убрал draw_grid() - убираем сетку

# Рисуем график по частям
draw_first_part()
draw_second_part()
draw_third_part()
draw_fourth_part()
draw_fifth_part()

graph.hideturtle()

# Завершаем программу
turtle.done()