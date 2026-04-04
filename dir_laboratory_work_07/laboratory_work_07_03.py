import turtle
import math

# Настройки
DX = 3  # Шаг
TOLERANCE = 0.0003  # Точность
X_MIN = -10  # Минимальное значение x
X_MAX = 10  # Максимальное значение x
SCALE = 20  # Масштаб для отображения

# Настройка окна
screen = turtle.Screen()
screen.setup(900, 700)
screen.title("График функции e^(-x) через ряд с точностью 0.0003")
screen.bgcolor("white")

# Создание черепашек
t = turtle.Turtle()  # Для осей и графика
t.speed(0)
t.hideturtle()


# Функция вычисления e^(-x) через ряд
def compute_exp_minus_x_by_series(x, tolerance=TOLERANCE):
    """
    Вычисляет e^(-x) через ряд:
    e^(-x) = Σ (-1)^n * x^n / n! = 1 - x + x²/2! - x³/3! + ...
    """
    result = 0.0
    term = 1.0  # Первый член ряда при n=0: (-1)^0 * x^0 / 0! = 1
    n = 0
    factorial = 1  # 0! = 1

    # Максимальное количество итераций для защиты от бесконечного цикла
    max_iterations = 100

    while abs(term) >= tolerance and n < max_iterations:
        result += term
        n += 1
        factorial *= n  # Вычисляем n!
        term = ((-1) ** n) * (x ** n) / factorial

    # Добавляем последний член, если он был пропущен из-за условия while
    if abs(term) < tolerance:
        result += term

    # Выводим информацию о количестве итераций (для отладки)
    if x == 0 or x == 1 or x == 2:
        print(f"x = {x}: использовано {n + 1} членов ряда, результат = {result:.6f}")

    return result


# Рисуем оси координат
def draw_axes():
    t.penup()
    t.color("black")
    t.pensize(1)

    # Ось X
    t.goto(-400, 0)
    t.pendown()
    t.goto(400, 0)
    t.penup()

    # Стрелка оси X
    t.goto(400, 0)
    t.pendown()
    t.goto(390, -10)
    t.goto(400, 0)
    t.goto(390, 10)
    t.penup()

    # Подпись оси X
    t.goto(420, -20)
    t.write("x", align="center", font=("Arial", 14, "bold"))

    # Ось Y
    t.goto(0, -300)
    t.pendown()
    t.goto(0, 300)
    t.penup()

    # Стрелка оси Y
    t.goto(0, 300)
    t.pendown()
    t.goto(-10, 290)
    t.goto(0, 300)
    t.goto(10, 290)
    t.penup()

    # Подпись оси Y
    t.goto(-20, 320)
    t.write("y", align="center", font=("Arial", 14, "bold"))

    # Разметка оси X
    for x in range(-8, 9, 2):  # От -8 до 8 с шагом 2
        screen_x = x * SCALE
        t.goto(screen_x, -5)
        t.pendown()
        t.goto(screen_x, 5)
        t.penup()
        t.goto(screen_x, -20)
        t.write(f"{x}", align="center", font=("Arial", 10))

    # Разметка оси Y
    for y in range(-10, 11, 2):  # От -10 до 10 с шагом 2
        screen_y = y * SCALE
        t.goto(-5, screen_y)
        t.pendown()
        t.goto(5, screen_y)
        t.penup()
        t.goto(-25, screen_y - 5)
        t.write(f"{y}", align="center", font=("Arial", 10))


# Рисуем график, вычисленный через ряд
def draw_series_graph():
    print("Рисуем график e^(-x) через ряд с точностью 0.0003...")

    t.penup()
    t.color("blue")
    t.pensize(3)  # Более толстая линия для лучшей видимости

    first_point = True
    points_drawn = 0

    # Перебираем значения x с шагом DX/SCALE для плавности
    step = DX / SCALE
    x = X_MIN

    # Создаем список точек для более плавного рисования
    points = []

    while x <= X_MAX:
        try:
            # Вычисляем значение через ряд
            y_series = compute_exp_minus_x_by_series(x)

            # Преобразуем в экранные координаты
            screen_x = x * SCALE
            screen_y = y_series * SCALE

            # Сохраняем точку
            points.append((screen_x, screen_y))

            # Обновляем x
            x += step
            points_drawn += 1

        except (OverflowError, ValueError):
            # Пропускаем точки, где ряд расходится
            x += step
            continue

    # Рисуем все точки
    for i, (screen_x, screen_y) in enumerate(points):
        # Если точка в пределах экрана
        if -400 <= screen_x <= 400 and -300 <= screen_y <= 300:
            if first_point:
                t.goto(screen_x, screen_y)
                t.pendown()
                first_point = False
            else:
                t.goto(screen_x, screen_y)

    t.penup()
    print(f"Нарисовано {points_drawn} точек графика")


# Рисуем легенду и информацию
def draw_info():
    t.penup()

    # Заголовок
    t.goto(-420, 320)
    t.color("black")
    t.write("ГРАФИК ФУНКЦИИ e^(-x)", align="left", font=("Arial", 12, "bold"))

    # Формула ряда
    t.goto(-420, 300)
    t.color("darkblue")
    t.write("Ряд: e^(-x) = 1 - x + x²/2! - x³/3! + ...", align="left", font=("Arial", 10))

    # Информация о параметрах
    t.goto(-420, 280)
    t.color("black")
    t.write("ПАРАМЕТРЫ:", align="left", font=("Arial", 10, "bold"))

    t.goto(-420, 265)
    t.color("black")
    t.write(f"Точность вычислений: {TOLERANCE}", align="left", font=("Arial", 9))

    t.goto(-420, 250)
    t.color("black")
    t.write(f"Шаг dx: {DX}", align="left", font=("Arial", 9))

    t.goto(-420, 235)
    t.color("black")
    t.write(f"Диапазон x: [{X_MIN}, {X_MAX}]", align="left", font=("Arial", 9))

    t.goto(-420, 220)
    t.color("black")
    t.write(f"Масштаб: 1:20", align="left", font=("Arial", 9))

    # Примеры вычислений
    t.goto(-420, 200)
    t.color("black")
    t.write("ПРИМЕРЫ ВЫЧИСЛЕНИЙ:", align="left", font=("Arial", 10, "bold"))

    # Вычисляем значения в ключевых точках
    test_points = [-2, -1, 0, 1, 2, 3]
    y_pos = 185

    for x in test_points:
        try:
            y_val = compute_exp_minus_x_by_series(x)
            t.goto(-420, y_pos)
            t.color("darkgreen")
            t.write(f"e^(-{abs(x)}) ≈ {y_val:.6f}", align="left", font=("Arial", 8))
            y_pos -= 15
        except:
            y_pos -= 15


# Основная функция
def main():
    # Отключаем автоматическое обновление для скорости
    screen.tracer(0)

    # Рисуем оси
    draw_axes()

    # Рисуем график через ряд
    draw_series_graph()

    # Рисуем информацию
    draw_info()

    # Включаем обновление
    screen.tracer(1)
    screen.update()

    # Сохраняем изображение
    canvas = screen.getcanvas()
    canvas.postscript(file="exp_minus_x_series_graph.ps", colormode='color')
    print("\nИзображение сохранено как 'exp_minus_x_series_graph.ps'")

    # Дополнительная информация в консоли
    print("\n" + "=" * 50)
    print("ИНФОРМАЦИЯ О ВЫЧИСЛЕНИЯХ:")
    print("=" * 50)
    print(f"Функция: e^(-x)")
    print(f"Ряд: 1 - x + x²/2! - x³/3! + x⁴/4! - ...")
    print(f"Точность: {TOLERANCE}")
    print(f"Диапазон x: от {X_MIN} до {X_MAX}")
    print(f"Шаг: {DX}")

    # Оставляем окно открытым
    print("\nДля выхода нажмите на окно...")
    screen.exitonclick()


if __name__ == "__main__":
    main()