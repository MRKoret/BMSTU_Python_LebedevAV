import turtle
import random
import math

# Настройки
R = 200  # Радиус
NUM_POINTS = 100  # Количество испытаний

# Настройка окна turtle
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Метод Монте-Карло для вычисления площади")
screen.bgcolor("white")

# Создание черепашки для рисования
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Создаем отдельную черепашку для точек (чтобы они рисовались быстрее)
points_turtle = turtle.Turtle()
points_turtle.speed(0)
points_turtle.hideturtle()


# Функция для проверки попадания точки в заштрихованную область
def is_in_shaded_area(x, y):
    if -R <= x <= 0:
        # Первая область: четверть круга
        return 0 <= y <= math.sqrt(R ** 2 - x ** 2)
    elif 0 <= x <= R / 2:
        # Вторая область: треугольник
        return -2 * x <= y <= 0
    elif R / 2 <= x <= R:
        # Третья область: треугольник
        return 2 * x - 2 * R <= y <= 0
    return False


# Функция для вычисления реальной площади (геометрически)
def calculate_real_area(R):
    # Площадь четверти круга
    circle_area = (math.pi * R ** 2) / 4

    # Площадь второго треугольника
    triangle2_area = (R / 2 * R) / 2

    # Площадь третьего треугольника
    triangle3_area = (R / 2 * R) / 2

    return circle_area + triangle2_area + triangle3_area


# Рисуем оси координат с подписями
def draw_axes():
    t.penup()
    t.color("black")
    t.pensize(1)

    # Ось X
    t.goto(-R - 50, 0)
    t.pendown()
    t.goto(R + 50, 0)
    t.penup()

    # Подпись оси X
    t.goto(R + 60, -20)
    t.write("x", align="center", font=("Arial", 14, "bold"))

    # Ось Y
    t.goto(0, -R - 50)
    t.pendown()
    t.goto(0, R + 50)
    t.penup()

    # Подпись оси Y
    t.goto(-20, R + 60)
    t.write("y", align="center", font=("Arial", 14, "bold"))

    # Отметки на оси X с подписями
    positions = [(-R, "-r"), (-R / 2, "-r/2"), (0, "0"), (R / 2, "r/2"), (R, "r")]

    for pos, label in positions:
        t.goto(pos, -5)
        t.pendown()
        t.goto(pos, 5)
        t.penup()
        t.goto(pos, -20)
        t.write(label, align="center", font=("Arial", 10))

    # Отметки на оси Y с подписями
    positions = [(-R, "-r"), (-R / 2, "-r/2"), (0, "0"), (R / 2, "r/2"), (R, "r")]

    for pos, label in positions:
        t.goto(-5, pos)
        t.pendown()
        t.goto(5, pos)
        t.penup()
        t.goto(-25, pos - 5)
        t.write(label, align="center", font=("Arial", 10))


# Рисуем первый промежуток
def draw_first_interval():
    t.penup()
    t.color("blue")
    t.pensize(3)

    # Полуокружность
    t.goto(-R, 0)
    t.pendown()
    for x in range(-R, 1):
        y = math.sqrt(R ** 2 - x ** 2) if R ** 2 - x ** 2 >= 0 else 0
        t.goto(x, y)

    t.penup()
    t.goto(0, R)
    t.pendown()
    t.goto(0, 0)

    t.penup()
    t.goto(-R, 0)
    t.pendown()
    t.goto(0, 0)
    t.penup()


# Рисуем второй промежуток
def draw_second_interval():
    t.goto(0, 0)
    t.color("red")
    t.pensize(3)
    t.pendown()

    # Верхняя граница: y = -2*x
    t.goto(R / 2, -R)

    t.penup()
    t.goto(R / 2, 0)
    t.pendown()
    t.goto(0, 0)

    t.penup()
    t.goto(R / 2, -R)
    t.pendown()
    t.goto(R / 2, 0)
    t.penup()


# Рисуем третий промежуток
def draw_third_interval():
    t.goto(R / 2, -R)
    t.color("green")
    t.pensize(3)
    t.pendown()

    # Верхняя граница: y = 2*x - 2*r
    t.goto(R, 0)

    t.penup()
    t.goto(R, 0)
    t.pendown()
    t.goto(R / 2, 0)

    t.penup()
    t.goto(R / 2, 0)
    t.pendown()
    t.goto(R / 2, -R)
    t.penup()


# Метод Монте-Карло с мгновенным отображением точек
def monte_carlo_simulation(num_points):
    points_in = 0
    points = []

    min_x, max_x = -R, R
    min_y, max_y = -R, R

    print(f"Генерируем {num_points} точек...")

    for i in range(num_points):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)

        if is_in_shaded_area(x, y):
            points_in += 1
            # Определяем цвет точки в зависимости от области
            if -R <= x <= 0 and 0 <= y <= math.sqrt(R ** 2 - x ** 2):
                color = "blue"
            elif 0 <= x <= R / 2 and -2 * x <= y <= 0:
                color = "red"
            elif R / 2 <= x <= R and 2 * x - 2 * R <= y <= 0:
                color = "green"
        else:
            color = "gray"

        points.append((x, y, color))

        # Мгновенное отображение точки
        points_turtle.penup()
        points_turtle.goto(x, y)
        points_turtle.dot(4, color)

        # Обновляем экран после каждых 10 точек для скорости
        if i % 10 == 0:
            screen.update()

    rect_area = (max_x - min_x) * (max_y - min_y)
    estimated_area = (points_in / num_points) * rect_area

    return estimated_area, points


# Рисуем легенду
def draw_legend():
    t.penup()

    # Заголовок легенды
    t.goto(-R - 50, R + 100)
    t.color("black")
    t.write("ОПИСАНИЕ ГРАФИКА:", align="left", font=("Arial", 12, "bold"))

    # Первый промежуток
    t.goto(-R - 50, R + 80)
    t.color("blue")
    t.goto(-R - 50, R + 65)

    # Второй промежуток
    t.goto(-R - 50, R + 50)
    t.color("red")
    t.goto(-R - 50, R + 35)

    # Третий промежуток
    t.goto(-R - 50, R + 20)
    t.color("green")
    t.goto(-R - 50, R + 5)

    # Обозначение точек
    t.goto(-R - 50, -R - 80)
    t.color("black")
    t.write("ОБОЗНАЧЕНИЕ ТОЧЕК:", align="left", font=("Arial", 10, "bold"))

    t.goto(-R - 50, -R - 95)
    t.dot(4, "blue")
    t.goto(-R - 30, -R - 100)
    t.write(" - в полуокружности", align="left", font=("Arial", 10, "normal"))

    t.goto(-R - 50, -R - 110)
    t.dot(4, "red")
    t.goto(-R - 30, -R - 115)
    t.write(" - в треугольнике 1", align="left", font=("Arial", 10, "normal"))

    t.goto(-R - 50, -R - 125)
    t.dot(4, "green")
    t.goto(-R - 30, -R - 130)
    t.write(" - в треугольнике 2", align="left", font=("Arial", 10, "normal"))

    t.goto(-R - 50, -R - 140)
    t.dot(4, "gray")
    t.goto(-R - 30, -R - 145)
    t.write(" - снаружи области", align="left", font=("Arial", 10, "normal"))


# Основная программа
def main():
    # Выключаем автоматическое обновление для ускорения
    screen.tracer(0)

    # Рисуем оси с подписями
    draw_axes()

    # Рисуем все три промежутка
    draw_first_interval()
    draw_second_interval()
    draw_third_interval()

    # Обновляем экран
    screen.update()

    # Вычисляем реальную площадь
    real_area = calculate_real_area(R)

    # Выполняем метод Монте-Карло
    print(f"Радиус R = {R}")
    print(f"Количество испытаний: {NUM_POINTS}")

    # Включаем обновление для точек
    screen.tracer(1, 5)  # Обновляем каждые 5 операций

    print("\nНачинаем моделирование методом Монте-Карло...")
    estimated_area, points = monte_carlo_simulation(NUM_POINTS)

    # Рисуем легенду
    draw_legend()

    # Вычисляем точность
    error = abs(estimated_area - real_area)
    accuracy_percent = (1 - error / real_area) * 100

    # Вывод результатов
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 50)
    print(f"Реальная площадь (геометрически): {real_area:.2f}")
    print(f"Оценка площади (Монте-Карло): {estimated_area:.2f}")
    print(f"Абсолютная погрешность: {error:.2f}")
    print(f"Относительная погрешность: {error / real_area * 100:.2f}%")
    print(f"Точность вычислений: {accuracy_percent:.2f}%")

    # Статистика
    points_inside = int((estimated_area / (4 * R * R)) * NUM_POINTS)
    print(f"\nТочки внутри области: {points_inside}")
    print(f"Точки снаружи области: {NUM_POINTS - points_inside}")

    # Добавляем статистику на график
    t.penup()
    t.goto(R - 150, -R - 60)
    t.color("black")
    t.write(f"Реальная площадь: {real_area:.2f}", align="left", font=("Arial", 9, "normal"))

    t.goto(R - 150, -R - 75)
    t.write(f"Оценка МК: {estimated_area:.2f}", align="left", font=("Arial", 9, "normal"))

    t.goto(R - 150, -R - 90)
    t.write(f"Точность: {accuracy_percent:.1f}%", align="left", font=("Arial", 9, "normal"))

    t.goto(R - 150, -R - 105)
    t.write(f"Испытаний: {NUM_POINTS}", align="left", font=("Arial", 9, "normal"))

    # Обновляем экран
    screen.update()

    # Сохраняем изображение
    canvas = screen.getcanvas()
    canvas.postscript(file="monte_carlo_figure.ps", colormode='color')
    print("\nИзображение сохранено как 'monte_carlo_figure.ps'")

    # Оставляем окно открытым
    print("\nДля выхода нажмите на окно...")
    screen.exitonclick()


if __name__ == "__main__":
    main()