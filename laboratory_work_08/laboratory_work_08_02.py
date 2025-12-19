import tkinter as tk
from tkinter import messagebox
import math


# Функция для вычисления ряда Тейлора (y(x))
def y_taylor(x, eps=1e-6):
    """
    Вычисляет e^{-x} через ряд Тейлора: Σ((-1)^n * x^n / n!)
    """
    if x == 0:
        return 1.0

    term = 1.0  # Первый член ряда (n=0): (-1)^0 * x^0 / 0! = 1
    total = term
    n = 1

    while abs(term) > eps:
        term = ((-1) ** n) * (x ** n) / math.factorial(n)
        total += term
        n += 1

        # Защита от бесконечного цикла
        if n > 1000:
            break

    return total


# Функция для вычисления аналитической формы (z(x))
def z_analytic(x, b):
    """Вычисляет e^{-x} + b"""
    return math.exp(-x) + b


# Основной класс приложения
class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графики функций")

        # Глобальные переменные
        self.Kp = 0.7  # 70% от размера экрана
        self.MaxX = int(root.winfo_screenwidth() * self.Kp)
        self.MaxY = int(root.winfo_screenheight() * self.Kp)

        # Начальные параметры графика
        self.Xmin = -5.0
        self.Xmax = 5.0
        self.Ymin = -2.0
        self.Ymax = 8.0
        self.dX = 1.0  # Шаг меток
        self.dY = 0.0  # Смещение (b)

        # Масштабные коэффициенты
        self.Kx = self.MaxX / abs(self.Xmax - self.Xmin)
        self.Ky = self.MaxY / abs(self.Ymax - self.Ymin)

        # Идентификаторы линий курсора
        self.ID1 = 0
        self.ID2 = 0

        # Создаем интерфейс
        self.create_widgets()

        # Привязка события закрытия окна
        self.root.protocol('WM_DELETE_WINDOW', self.window_deleted)
        self.root.resizable(False, False)

    def create_widgets(self):
        # Создаем Canvas (полотно)
        self.cv = tk.Canvas(self.root, width=self.MaxX, height=self.MaxY, bg="white")
        self.cv.grid(row=0, columnspan=9)
        self.cv.bind('<Button-1>', self.showXY)

        # Метки и поля ввода
        self.create_input_fields()

        # Кнопки
        self.create_buttons()

    def create_input_fields(self):
        # Координаты мыши
        self.lbl_mouse_x = tk.Label(self.root, text="X:", width=10, fg="blue", font=("Arial", 12))
        self.lbl_mouse_x.grid(row=1, column=0, sticky='e')
        self.ent_mouse_x = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_mouse_x.grid(row=1, column=1, sticky='w')
        self.ent_mouse_x.insert(0, "0.00")

        self.lbl_mouse_y = tk.Label(self.root, text="Y:", width=10, fg="blue", font=("Arial", 12))
        self.lbl_mouse_y.grid(row=2, column=0, sticky='e')
        self.ent_mouse_y = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_mouse_y.grid(row=2, column=1, sticky='w')
        self.ent_mouse_y.insert(0, "0.00")

        # Границы графика
        self.lbl_xmin = tk.Label(self.root, text="Xmin:", width=10, fg="blue", font=("Arial", 12))
        self.lbl_xmin.grid(row=1, column=2, sticky='e')
        self.ent_xmin = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_xmin.grid(row=1, column=3)
        self.ent_xmin.insert(0, str(self.Xmin))

        self.lbl_xmax = tk.Label(self.root, text="Xmax:", width=10, fg="blue", font=("Arial", 12))
        self.lbl_xmax.grid(row=1, column=4, sticky='e')
        self.ent_xmax = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_xmax.grid(row=1, column=5)
        self.ent_xmax.insert(0, str(self.Xmax))

        self.lbl_ymin = tk.Label(self.root, text="Ymin:", width=10, fg="blue", font=("Arial", 12))
        self.lbl_ymin.grid(row=2, column=2, sticky='e')
        self.ent_ymin = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_ymin.grid(row=2, column=3)
        self.ent_ymin.insert(0, str(self.Ymin))

        self.lbl_ymax = tk.Label(self.root, text="Ymax:", width=10, fg="blue", font=("Arial", 12))
        self.lbl_ymax.grid(row=2, column=4, sticky='e')
        self.ent_ymax = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_ymax.grid(row=2, column=5)
        self.ent_ymax.insert(0, str(self.Ymax))

        # Шаг меток и смещение
        self.lbl_step = tk.Label(self.root, text="Шаг меток:", width=10, fg="blue", font=("Arial", 12))
        self.lbl_step.grid(row=1, column=6, sticky='e')
        self.ent_step = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_step.grid(row=1, column=7)
        self.ent_step.insert(0, str(self.dX))

        self.lbl_offset = tk.Label(self.root, text="Смещение (b):", width=10, fg="blue", font=("Arial", 12))
        self.lbl_offset.grid(row=2, column=6, sticky='e')
        self.ent_offset = tk.Entry(self.root, width=8, font=("Arial", 12))
        self.ent_offset.grid(row=2, column=7)
        self.ent_offset.insert(0, str(self.dY))

    def create_buttons(self):
        # Кнопка "Рисовать"
        self.btn_draw = tk.Button(self.root, width=20, bg="#ccc", text="Рисовать")
        self.btn_draw.grid(row=1, column=8)
        self.btn_draw.bind("<Button-1>", self.draw_graphs)

        # Кнопка "Выход"
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

            # Обновление глобальных переменных
            self.Xmin = tmp_xmin
            self.Xmax = tmp_xmax
            self.Ymin = tmp_ymin
            self.Ymax = tmp_ymax
            self.dX = tmp_step
            self.dY = tmp_offset

            # Пересчет масштабных коэффициентов
            self.Kx = self.MaxX / abs(self.Xmax - self.Xmin)
            self.Ky = self.MaxY / abs(self.Ymax - self.Ymin)

            return True

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")
            return False

    def plot_axes(self):
        """Рисование координатных осей с разметкой"""
        # Прямоугольник графика
        self.cv.create_rectangle(5, 5, self.MaxX - 5, self.MaxY - 5,
                                 fill="white", outline="green", width=2)

        # Разметка по оси Y (слева и справа)
        y = self.Ymin
        y_pix = self.MaxY
        draw_text = False

        while y < self.Ymax:
            text_y = str(round(y, 2))

            # Метка слева
            self.cv.create_line(0, y_pix, 10, y_pix, fill='black', width=2)
            if draw_text:
                self.cv.create_text(15, y_pix, text=text_y, anchor=tk.W)

            # Метка справа
            self.cv.create_line(self.MaxX - 10, y_pix, self.MaxX, y_pix, fill='black', width=2)
            if draw_text:
                self.cv.create_text(self.MaxX - 15, y_pix, text=text_y, anchor=tk.E)

            y += self.dX
            y_pix -= self.dX * self.Ky
            draw_text = not draw_text

        # Разметка по оси X (сверху и снизу)
        x = self.Xmin
        x_pix = 0
        draw_text = False

        while x < self.Xmax:
            text_x = str(round(x, 2))

            # Метка сверху
            self.cv.create_line(x_pix, 0, x_pix, 10, fill='black', width=2)
            if draw_text:
                self.cv.create_text(x_pix, 15, text=text_x, anchor=tk.N)

            # Метка снизу
            self.cv.create_line(x_pix, self.MaxY - 10, x_pix, self.MaxY, fill='black', width=2)
            if draw_text:
                self.cv.create_text(x_pix, self.MaxY - 15, text=text_x, anchor=tk.S)

            x += self.dX
            x_pix += self.dX * self.Kx
            draw_text = not draw_text

    def calculate_function_y(self):
        """Вычисление значений функции y(x) - ряд Тейлора"""
        points = []
        x = self.Xmin
        step = 1 / self.Kx  # Шаг в пользовательских единицах для плавного графика

        while x <= self.Xmax:
            try:
                y = y_taylor(x)
                points.append((x, y))
            except:
                # Если вычисление невозможно, пропускаем точку
                pass
            x += step

        return points

    def calculate_function_z(self):
        """Вычисление значений функции z(x) - аналитическая форма"""
        points = []
        x = self.Xmin
        step = 1 / self.Kx  # Шаг в пользовательских единицах для плавного графика

        while x <= self.Xmax:
            try:
                y = z_analytic(x, self.dY)
                points.append((x, y))
            except:
                # Если вычисление невозможно, пропускаем точку
                pass
            x += step

        return points

    def draw_function(self, points, color):
        """Рисование графика функции"""
        pixel_points = []

        for x, y in points:
            # Преобразование координат в пикселы
            x_pix = self.Kx * (x - self.Xmin)
            y_pix = self.MaxY - self.Ky * (y - self.Ymin)
            pixel_points.append((x_pix, y_pix))

        # Рисование линии
        if len(pixel_points) > 1:
            self.cv.create_line(pixel_points, fill=color, width=2, smooth=True)

    def draw_graphs(self, event=None):
        """Основная функция рисования графиков"""
        # Очистка полотна
        self.cv.delete("all")

        # Получение данных
        if not self.get_data():
            return

        # Рисование осей
        self.plot_axes()

        # Вычисление и рисование графиков
        points_y = self.calculate_function_y()
        points_z = self.calculate_function_z()

        self.draw_function(points_y, 'blue')
        self.draw_function(points_z, 'red')

        # Добавление легенды
        self.cv.create_text(self.MaxX - 100, 30,
                            text="y(x) = Σ((-1)ⁿ·xⁿ/n!)",
                            fill='blue', anchor=tk.W, font=("Arial", 10))
        self.cv.create_text(self.MaxX - 100, 50,
                            text=f"z(x) = e^(-x) + {self.dY:.2f}",
                            fill='red', anchor=tk.W, font=("Arial", 10))

        # Добавление заголовка
        self.cv.create_text(self.MaxX / 2, 20,
                            text="Графики функций",
                            fill='black', font=("Arial", 14, "bold"))

    def showXY(self, event):
        """Отображение координат мыши"""
        x_pix = event.x
        y_pix = event.y

        # Преобразование в пользовательские координаты
        x_user = self.Xmin + x_pix / self.Kx
        y_user = self.Ymin + (self.MaxY - y_pix) / self.Ky

        # Обновление полей ввода
        self.ent_mouse_x.delete(0, tk.END)
        self.ent_mouse_y.delete(0, tk.END)
        self.ent_mouse_x.insert(0, f"{x_user:.2f}")
        self.ent_mouse_y.insert(0, f"{y_user:.2f}")

        # Удаление старых линий курсора
        self.cv.delete(self.ID1)
        self.cv.delete(self.ID2)

        # Рисование новых линий курсора
        self.ID1 = self.cv.create_line(0, y_pix, self.MaxX, y_pix,
                                       dash=(3, 5), fill='gray')
        self.ID2 = self.cv.create_line(x_pix, 0, x_pix, self.MaxY,
                                       dash=(3, 5), fill='gray')

    def final(self, event=None):
        """Завершение работы"""
        self.window_deleted()

    def window_deleted(self):
        """Обработка закрытия окна"""
        if messagebox.askyesno("Выход", "Завершить работу?"):
            self.root.destroy()


# Основная программа
def main():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()