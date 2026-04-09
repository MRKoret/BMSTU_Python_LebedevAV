import turtle
import math


class CoordinateSystem:
    """Класс для управления координатной системой и масштабированием"""

    def __init__(self, x_min=-10, x_max=8, y_min=-4, y_max=4, width=700, height=500):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.width = width
        self.height = height

    def scale_point(self, x, y):
        """Преобразование математических координат в экранные"""
        x_scale = self.width / (self.x_max - self.x_min)
        y_scale = self.height / (self.y_max - self.y_min)

        x_scaled = (x - self.x_min) * x_scale - self.width / 2
        y_scaled = (y - self.y_min) * y_scale - self.height / 2
        return x_scaled, y_scaled


class AxisDrawer:
    """Класс для рисования осей координат"""

    def __init__(self, turtle_obj, coord_system):
        self.turtle = turtle_obj
        self.coord_system = coord_system

    def draw_axes(self):
        """Рисует оси координат, стрелки, подписи и деления"""
        self.turtle.penup()
        self._draw_x_axis()
        self._draw_y_axis()
        self._draw_axis_labels()
        self._draw_center_point()
        self._draw_ticks()
        self.turtle.hideturtle()

    def _draw_x_axis(self):
        """Рисует ось X со стрелкой"""
        start_x, start_y = self.coord_system.scale_point(self.coord_system.x_min, 0)
        end_x, end_y = self.coord_system.scale_point(self.coord_system.x_max, 0)

        self.turtle.goto(start_x, start_y)
        self.turtle.pendown()
        self.turtle.goto(end_x, end_y)

        # Стрелка для оси X
        self.turtle.penup()
        self.turtle.goto(end_x - 10, end_y + 5)
        self.turtle.pendown()
        self.turtle.goto(end_x, end_y)
        self.turtle.goto(end_x - 10, end_y - 5)
        self.turtle.penup()

    def _draw_y_axis(self):
        """Рисует ось Y со стрелкой"""
        start_x, start_y = self.coord_system.scale_point(0, self.coord_system.y_min)
        end_x, end_y = self.coord_system.scale_point(0, self.coord_system.y_max)

        self.turtle.goto(start_x, start_y)
        self.turtle.pendown()
        self.turtle.goto(end_x, end_y)

        # Стрелка для оси Y
        self.turtle.penup()
        self.turtle.goto(end_x - 5, end_y - 10)
        self.turtle.pendown()
        self.turtle.goto(end_x, end_y)
        self.turtle.goto(end_x + 5, end_y - 10)
        self.turtle.penup()

    def _draw_axis_labels(self):
        """Рисует подписи осей X и Y"""
        # Подпись для оси X
        label_x, label_y = self.coord_system.scale_point(self.coord_system.x_max - 0.5, -0.5)
        self.turtle.goto(label_x, label_y)
        self.turtle.write("X", align="center", font=("Arial", 12, "normal"))

        # Подпись для оси Y
        label_x, label_y = self.coord_system.scale_point(0.5, self.coord_system.y_max - 0.3)
        self.turtle.goto(label_x, label_y)
        self.turtle.write("Y", align="center", font=("Arial", 12, "normal"))

    def _draw_center_point(self):
        """Рисует точку 0 в центре координат"""
        zero_x, zero_y = self.coord_system.scale_point(0, 0)
        self.turtle.goto(zero_x + 5, zero_y - 15)
        self.turtle.write("0", align="left", font=("Arial", 10, "normal"))

    def _draw_ticks(self):
        """Рисует деления на осях"""
        # Деления на оси X
        for i in range(int(self.coord_system.x_min), int(self.coord_system.x_max) + 1):
            if i != 0:
                self._draw_x_tick(i)

        # Деления на оси Y
        for i in range(int(self.coord_system.y_min), int(self.coord_system.y_max) + 1):
            if i != 0:
                self._draw_y_tick(i)

    def _draw_x_tick(self, x_value):
        """Рисует деление на оси X"""
        x_pos, y_pos = self.coord_system.scale_point(x_value, 0)
        self.turtle.penup()
        self.turtle.goto(x_pos, y_pos - 5)
        self.turtle.pendown()
        self.turtle.goto(x_pos, y_pos + 5)
        self.turtle.penup()
        self.turtle.goto(x_pos, y_pos - 20)
        self.turtle.write(str(x_value), align="center", font=("Arial", 8, "normal"))

    def _draw_y_tick(self, y_value):
        """Рисует деление на оси Y"""
        x_pos, y_pos = self.coord_system.scale_point(0, y_value)
        self.turtle.penup()
        self.turtle.goto(x_pos - 5, y_pos)
        self.turtle.pendown()
        self.turtle.goto(x_pos + 5, y_pos)
        self.turtle.penup()
        self.turtle.goto(x_pos + 10, y_pos - 5)
        self.turtle.write(str(y_value), align="center", font=("Arial", 8, "normal"))


class FunctionPlotter:
    """Класс для построения графиков функций"""

    def __init__(self, turtle_obj, coord_system):
        self.turtle = turtle_obj
        self.coord_system = coord_system

    def draw_first_part(self):
        """Рисует первую часть графика: y = -3 для x <= -8"""
        self.turtle.penup()
        start_x, start_y = self.coord_system.scale_point(-10, -3)
        self.turtle.goto(start_x, start_y)
        self.turtle.pendown()

        for i in range(201):
            x = -10 + (i / 200.0) * 2
            if x <= -8:
                self._draw_point(x, -3)

    def draw_second_part(self):
        """Рисует вторую часть графика: y = (3/5)x + 9/5 для -8 < x < -3"""
        for i in range(201):
            x = -8 + (i / 200.0) * 5
            if x < -3:
                y = (3 / 5) * x + 9 / 5
                self._draw_point(x, y)

    def draw_third_part(self):
        """Рисует третью часть графика: y = -sqrt(9 - x^2) для -3 <= x < 3"""
        for i in range(401):
            x = -3 + (i / 400.0) * 6
            if x < 3:
                try:
                    y = -math.sqrt(9 - x ** 2)
                    self._draw_point(x, y)
                except ValueError:
                    continue

    def draw_fourth_part(self):
        """Рисует четвертую часть графика: y = x - 3 для 3 <= x <= 5"""
        for i in range(201):
            x = 3 + (i / 200.0) * 2
            if x <= 5:
                y = x - 3
                self._draw_point(x, y)

    def draw_fifth_part(self):
        """Рисует пятую часть графика: y = 3 для x >= 5"""
        self.turtle.penup()

        # Перемещаемся к точке (5, 3) - здесь разрыв
        x_scaled, y_scaled = self.coord_system.scale_point(5, 3)
        self.turtle.goto(x_scaled, y_scaled)
        self.turtle.pendown()

        # Рисуем горизонтальную линию
        for i in range(201):
            x_val = 5 + (i / 200.0) * 3
            if x_val <= self.coord_system.x_max:
                self._draw_point(x_val, 3)

    def _draw_point(self, x, y):
        """Рисует точку графика"""
        x_scaled, y_scaled = self.coord_system.scale_point(x, y)
        self.turtle.goto(x_scaled, y_scaled)

    def draw_full_graph(self):
        """Рисует весь график последовательно"""
        self.draw_first_part()
        self.draw_second_part()
        self.draw_third_part()
        self.draw_fourth_part()
        self.draw_fifth_part()
        self.turtle.hideturtle()


class GraphApp:
    """Главный класс приложения"""

    def __init__(self, screen_width=800, screen_height=600):
        self.screen = turtle.Screen()
        self.screen.setup(width=screen_width, height=screen_height)
        self.screen.title("Координатная система с графиком")
        self.screen.bgcolor("white")

        # Создаем объекты для рисования
        self.axes_turtle = turtle.Turtle()
        self.axes_turtle.speed(0)
        self.axes_turtle.pensize(1)
        self.axes_turtle.color("black")

        self.graph_turtle = turtle.Turtle()
        self.graph_turtle.speed(0)
        self.graph_turtle.pensize(2)
        self.graph_turtle.color("blue")

        # Создаем координатную систему
        self.coord_system = CoordinateSystem()

        # Создаем вспомогательные объекты
        self.axis_drawer = AxisDrawer(self.axes_turtle, self.coord_system)
        self.function_plotter = FunctionPlotter(self.graph_turtle, self.coord_system)

    def run(self):
        """Запускает отрисовку графика"""
        self.axis_drawer.draw_axes()
        self.function_plotter.draw_full_graph()
        turtle.done()


# Основная программа
if __name__ == "__main__":
    app = GraphApp()
    app.run()