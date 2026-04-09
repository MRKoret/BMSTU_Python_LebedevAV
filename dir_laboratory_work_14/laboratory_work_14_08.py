import tkinter as tk
from tkinter import messagebox
import math


# ===================== КЛАССЫ МАТЕМАТИЧЕСКИХ ФУНКЦИЙ =====================

class TaylorSeries:
    """
    Класс для вычисления e^(-x) через ряд Тейлора
    Ряд: Σ((-1)^n * x^n / n!)
    """

    def __init__(self, eps=1e-6, max_iter=1000):
        """
        Инициализация ряда Тейлора

        Args:
            eps: точность вычислений
            max_iter: максимальное количество итераций
        """
        self.eps = eps
        self.max_iter = max_iter

    def calculate(self, x):
        """
        Вычисляет значение e^(-x) через ряд Тейлора

        Args:
            x: аргумент функции

        Returns:
            значение функции
        """
        if x == 0:
            return 1.0

        term = 1.0  # Первый член ряда (n=0)
        total = term
        n = 1

        while abs(term) > self.eps:
            term = ((-1) ** n) * (x ** n) / math.factorial(n)
            total += term
            n += 1

            # Защита от бесконечного цикла
            if n > self.max_iter:
                break

        return total


class AnalyticFunction:
    """
    Класс для аналитической функции z(x) = e^(-x) + b
    """

    def __init__(self, b=0.0):
        """
        Инициализация аналитической функции

        Args:
            b: параметр смещения
        """
        self.b = b

    def set_offset(self, b):
        """Устанавливает смещение b"""
        self.b = b

    def calculate(self, x):
        """
        Вычисляет значение z(x) = e^(-x) + b

        Args:
            x: аргумент функции

        Returns:
            значение функции
        """
        return math.exp(-x) + self.b


class FunctionGraph:
    """
    Класс для представления графика функции
    """

    def __init__(self, func, color, name, formula):
        """
        Инициализация графика функции

        Args:
            func: объект функции с методом calculate()
            color: цвет графика
            name: название функции
            formula: формула для отображения
        """
        self.func = func
        self.color = color
        self.name = name
        self.formula = formula
        self.points = []

    def calculate_points(self, x_min, x_max, step):
        """
        Вычисляет точки для построения графика

        Args:
            x_min: минимальное значение X
            x_max: максимальное значение X
            step: шаг вычислений
        """
        self.points = []
        x = x_min

        while x <= x_max:
            try:
                y = self.func.calculate(x)
                self.points.append((x, y))
            except:
                pass
            x += step

    def draw(self, canvas, kx, ky, max_y, x_min, y_min):
        """
        Рисует график на canvas

        Args:
            canvas: объект Canvas
            kx: масштаб по X
            ky: масштаб по Y
            max_y: максимальная Y координата в пикселях
            x_min: минимальное значение X
            y_min: минимальное значение Y
        """
        pixel_points = []

        for x, y in self.points:
            x_pix = kx * (x - x_min)
            y_pix = max_y - ky * (y - y_min)
            pixel_points.append((x_pix, y_pix))

        if len(pixel_points) > 1:
            canvas.create_line(pixel_points, fill=self.color, width=2, smooth=True)

    def draw_legend(self, canvas, x_pos, y_pos):
        """
        Рисует легенду графика

        Args:
            canvas: объект Canvas
            x_pos: позиция по X
            y_pos: позиция по Y
        """
        canvas.create_text(x_pos, y_pos, text=self.formula,
                           fill=self.color, anchor=tk.W, font=("Arial", 10))


# ===================== КЛАСС ДЛЯ ПОСТРОЕНИЯ ОСЕЙ =====================

class CoordinateAxes:
    """
    Класс для построения координатных осей с разметкой
    """

    def __init__(self, canvas, x_min, x_max, y_min, y_max, step, max_x, max_y, kx, ky):
        """
        Инициализация осей координат

        Args:
            canvas: объект Canvas
            x_min, x_max: границы по X
            y_min, y_max: границы по Y
            step: шаг разметки
            max_x, max_y: размеры canvas в пикселях
            kx, ky: масштабные коэффициенты
        """
        self.canvas = canvas
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.step = step
        self.max_x = max_x
        self.max_y = max_y
        self.kx = kx
        self.ky = ky

    def draw(self):
        """Рисует координатные оси с разметкой"""
        # Прямоугольник графика
        self.canvas.create_rectangle(5, 5, self.max_x - 5, self.max_y - 5,
                                     fill="white", outline="green", width=2)

        # Разметка по оси Y (слева и справа)
        self._draw_y_axis_marks()

        # Разметка по оси X (сверху и снизу)
        self._draw_x_axis_marks()

    def _draw_y_axis_marks(self):
        """Рисует разметку по оси Y"""
        y = self.y_min
        y_pix = self.max_y
        draw_text = False

        while y < self.y_max:
            text_y = str(round(y, 2))

            # Метка слева
            self.canvas.create_line(0, y_pix, 10, y_pix, fill='black', width=2)
            if draw_text:
                self.canvas.create_text(15, y_pix, text=text_y, anchor=tk.W)

            # Метка справа
            self.canvas.create_line(self.max_x - 10, y_pix, self.max_x, y_pix,
                                    fill='black', width=2)
            if draw_text:
                self.canvas.create_text(self.max_x - 15, y_pix, text=text_y,
                                        anchor=tk.E)

            y += self.step
            y_pix -= self.step * self.ky
            draw_text = not draw_text

    def _draw_x_axis_marks(self):
        """Рисует разметку по оси X"""
        x = self.x_min
        x_pix = 0
        draw_text = False

        while x < self.x_max:
            text_x = str(round(x, 2))

            # Метка сверху
            self.canvas.create_line(x_pix, 0, x_pix, 10, fill='black', width=2)
            if draw_text:
                self.canvas.create_text(x_pix, 15, text=text_x, anchor=tk.N)

            # Метка снизу
            self.canvas.create_line(x_pix, self.max_y - 10, x_pix, self.max_y,
                                    fill='black', width=2)
            if draw_text:
                self.canvas.create_text(x_pix, self.max_y - 15, text=text_x,
                                        anchor=tk.S)

            x += self.step
            x_pix += self.step * self.kx
            draw_text = not draw_text


# ===================== КЛАСС ГРАФИЧЕСКОГО ИНТЕРФЕЙСА =====================

class GraphApp:
    """Основной класс приложения"""

    def __init__(self, root):
        self.root = root
        self.root.title("Графики функций")

        # Параметры окна
        self.Kp = 0.7  # 70% от размера экрана
        self.MaxX = int(root.winfo_screenwidth() * self.Kp)
        self.MaxY = int(root.winfo_screenheight() * self.Kp)

        # Границы графика
        self.Xmin = -5.0
        self.Xmax = 5.0
        self.Ymin = -2.0
        self.Ymax = 8.0
        self.step = 1.0  # Шаг меток
        self.offset = 0.0  # Смещение (b)

        # Масштабные коэффициенты
        self.Kx = self.MaxX / abs(self.Xmax - self.Xmin)
        self.Ky = self.MaxY / abs(self.Ymax - self.Ymin)

        # Идентификаторы линий курсора
        self.cursor_line_x = 0
        self.cursor_line_y = 0

        # Создание математических объектов
        self.taylor_series = TaylorSeries()
        self.analytic_func = AnalyticFunction(b=self.offset)

        # Создание объектов графиков
        self.graph_y = FunctionGraph(
            self.taylor_series,
            'blue',
            "y(x)",
            "y(x) = Σ((-1)ⁿ·xⁿ/n!)"
        )

        self.graph_z = FunctionGraph(
            self.analytic_func,
            'red',
            "z(x)",
            f"z(x) = e^(-x) + {self.offset:.2f}"
        )

        # Создание интерфейса
        self.create_widgets()

        # Привязка событий
        self.root.protocol('WM_DELETE_WINDOW', self.window_deleted)
        self.root.resizable(False, False)

    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Canvas для рисования
        self.canvas = tk.Canvas(self.root, width=self.MaxX, height=self.MaxY, bg="white")
        self.canvas.grid(row=0, columnspan=9)
        self.canvas.bind('<Button-1>', self.show_xy)

        # Поля ввода
        self.create_input_fields()

        # Кнопки
        self.create_buttons()

    def create_input_fields(self):
        """Создание полей ввода"""
        # Координаты мыши
        self.lbl_mouse_x = tk.Label(self.root, text="X:", width=10,
                                    fg="blue", font=("Arial", 12))
        self.lbl_mouse_x.grid(row=1, column=0, sticky='e')
        self.ent_mouse_x = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_mouse_x.grid(row=1, column=1, sticky='w')
        self.ent_mouse_x.insert(0, "0.00")

        self.lbl_mouse_y = tk.Label(self.root, text="Y:", width=10,
                                    fg="blue", font=("Arial", 12))
        self.lbl_mouse_y.grid(row=2, column=0, sticky='e')
        self.ent_mouse_y = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_mouse_y.grid(row=2, column=1, sticky='w')
        self.ent_mouse_y.insert(0, "0.00")

        # Границы графика
        self.lbl_xmin = tk.Label(self.root, text="Xmin:", width=10,
                                 fg="blue", font=("Arial", 12))
        self.lbl_xmin.grid(row=1, column=2, sticky='e')
        self.ent_xmin = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_xmin.grid(row=1, column=3)
        self.ent_xmin.insert(0, str(self.Xmin))

        self.lbl_xmax = tk.Label(self.root, text="Xmax:", width=10,
                                 fg="blue", font=("Arial", 12))
        self.lbl_xmax.grid(row=1, column=4, sticky='e')
        self.ent_xmax = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_xmax.grid(row=1, column=5)
        self.ent_xmax.insert(0, str(self.Xmax))

        self.lbl_ymin = tk.Label(self.root, text="Ymin:", width=10,
                                 fg="blue", font=("Arial", 12))
        self.lbl_ymin.grid(row=2, column=2, sticky='e')
        self.ent_ymin = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_ymin.grid(row=2, column=3)
        self.ent_ymin.insert(0, str(self.Ymin))

        self.lbl_ymax = tk.Label(self.root, text="Ymax:", width=10,
                                 fg="blue", font=("Arial", 12))
        self.lbl_ymax.grid(row=2, column=4, sticky='e')
        self.ent_ymax = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_ymax.grid(row=2, column=5)
        self.ent_ymax.insert(0, str(self.Ymax))

        # Шаг меток и смещение
        self.lbl_step = tk.Label(self.root, text="Шаг меток:", width=10,
                                 fg="blue", font=("Arial", 12))
        self.lbl_step.grid(row=1, column=6, sticky='e')
        self.ent_step = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_step.grid(row=1, column=7)
        self.ent_step.insert(0, str(self.step))

        self.lbl_offset = tk.Label(self.root, text="Смещение (b):", width=10,
                                   fg="blue", font=("Arial", 12))
        self.lbl_offset.grid(row=2, column=6, sticky='e')
        self.ent_offset = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_offset.grid(row=2, column=7)
        self.ent_offset.insert(0, str(self.offset))

    def create_buttons(self):
        """Создание кнопок"""
        self.btn_draw = tk.Button(self.root, width=20, bg="#ccc", text="Рисовать")
        self.btn_draw.grid(row=1, column=8)
        self.btn_draw.bind("<Button-1>", self.draw_graphs)

        self.btn_exit = tk.Button(self.root, width=20, bg="#ccc", text="Выход")
        self.btn_exit.grid(row=2, column=8)
        self.btn_exit.bind("<Button-1>", self.final)

    def get_data(self):
        """Получение данных из полей ввода"""
        try:
            tmp_xmin = float(self.ent_xmin.get())
            tmp_xmax = float(self.ent_xmax.get())
            tmp_ymin = float(self.ent_ymin.get())
            tmp_ymax = float(self.ent_ymax.get())
            tmp_step = float(self.ent_step.get())
            tmp_offset = float(self.ent_offset.get())

            # Проверка корректности данных
            if (tmp_xmin >= tmp_xmax) or (tmp_ymin >= tmp_ymax) or (tmp_step <= 0):
                messagebox.showwarning(
                    title="Ошибка задания границ",
                    message="Должны выполняться неравенства:\n"
                            "Xmax > Xmin;\n"
                            "Ymax > Ymin;\n"
                            "Шаг меток > 0"
                )
                return False

            # Обновление переменных
            self.Xmin = tmp_xmin
            self.Xmax = tmp_xmax
            self.Ymin = tmp_ymin
            self.Ymax = tmp_ymax
            self.step = tmp_step
            self.offset = tmp_offset

            # Обновление смещения в аналитической функции
            self.analytic_func.set_offset(self.offset)

            # Обновление формулы в легенде
            self.graph_z.formula = f"z(x) = e^(-x) + {self.offset:.2f}"

            # Пересчет масштабных коэффициентов
            self.Kx = self.MaxX / abs(self.Xmax - self.Xmin)
            self.Ky = self.MaxY / abs(self.Ymax - self.Ymin)

            return True

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")
            return False

    def calculate_all_functions(self):
        """Вычисляет точки для всех функций"""
        step = 1 / self.Kx  # Шаг для плавного графика

        self.graph_y.calculate_points(self.Xmin, self.Xmax, step)
        self.graph_z.calculate_points(self.Xmin, self.Xmax, step)

    def draw_graphs(self, event=None):
        """Основная функция рисования графиков"""
        # Очистка полотна
        self.canvas.delete("all")

        # Получение данных
        if not self.get_data():
            return

        # Создание и рисование осей координат
        axes = CoordinateAxes(
            self.canvas, self.Xmin, self.Xmax, self.Ymin, self.Ymax,
            self.step, self.MaxX, self.MaxY, self.Kx, self.Ky
        )
        axes.draw()

        # Вычисление точек функций
        self.calculate_all_functions()

        # Рисование графиков
        self.graph_y.draw(self.canvas, self.Kx, self.Ky, self.MaxY, self.Xmin, self.Ymin)
        self.graph_z.draw(self.canvas, self.Kx, self.Ky, self.MaxY, self.Xmin, self.Ymin)

        # Добавление легенды
        self.graph_y.draw_legend(self.canvas, self.MaxX - 100, 30)
        self.graph_z.draw_legend(self.canvas, self.MaxX - 100, 50)

        # Заголовок
        self.canvas.create_text(self.MaxX / 2, 20,
                                text="Графики функций",
                                fill='black', font=("Arial", 14, "bold"))

    def show_xy(self, event):
        """Отображение координат мыши"""
        x_pix = event.x
        y_pix = event.y

        # Преобразование в пользовательские координаты
        x_user = self.Xmin + x_pix / self.Kx
        y_user = self.Ymin + (self.MaxY - y_pix) / self.Ky

        # Обновление полей
        self.ent_mouse_x.delete(0, tk.END)
        self.ent_mouse_y.delete(0, tk.END)
        self.ent_mouse_x.insert(0, f"{x_user:.2f}")
        self.ent_mouse_y.insert(0, f"{y_user:.2f}")

        # Удаление старых линий
        self.canvas.delete(self.cursor_line_x)
        self.canvas.delete(self.cursor_line_y)

        # Рисование новых линий курсора
        self.cursor_line_x = self.canvas.create_line(0, y_pix, self.MaxX, y_pix,
                                                     dash=(3, 5), fill='gray')
        self.cursor_line_y = self.canvas.create_line(x_pix, 0, x_pix, self.MaxY,
                                                     dash=(3, 5), fill='gray')

    def final(self, event=None):
        """Завершение работы"""
        self.window_deleted()

    def window_deleted(self):
        """Обработка закрытия окна"""
        if messagebox.askyesno("Выход", "Завершить работу?"):
            self.root.destroy()


# ===================== ЗАПУСК ПРОГРАММЫ =====================

def main():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()