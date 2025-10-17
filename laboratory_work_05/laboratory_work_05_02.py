def input_matrix_dimensions():

    while True:
        try:
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            if rows > 0 and cols > 0:
                return rows, cols
            else:
                print("Размеры должны быть положительными числами.")
        except ValueError:
            print("Пожалуйста, введите целые числа.")


def input_matrix(rows, cols):

    matrix = []
    print(f"\nВведите элементы матрицы {rows}x{cols}:")
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Строка {i + 1} (через пробел): ")
                elements = list(map(int, row_input.split()))

                if len(elements) != cols:
                    print(f"Ошибка: нужно ввести ровно {cols} элементов")
                    continue

                matrix.append(elements)
                break
            except ValueError:
                print("Ошибка: введите целые числа, разделенные пробелами")

    return matrix


def print_matrix(matrix, title="Матрица"):

    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))
    print()


def count_columns_without_zeros(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    count = 0
    for j in range(cols):
        has_zero = False
        for i in range(rows):
            if matrix[i][j] == 0:
                has_zero = True
                break
        if not has_zero:
            count += 1

    return count


def calculate_row_characteristic(row):

    characteristic = 0
    for element in row:
        if element > 0 and element % 2 == 0:
            characteristic += element
    return characteristic


def sort_rows_by_characteristics(matrix):

    # Создаем список кортежей (характеристика, строка)
    rows_with_characteristics = []
    for row in matrix:
        characteristic = calculate_row_characteristic(row)
        rows_with_characteristics.append((characteristic, row))

    # Сортируем по характеристике
    rows_with_characteristics.sort(key=lambda x: x[0])

    # Формируем новую матрицу из отсортированных строк
    sorted_matrix = [row for _, row in rows_with_characteristics]

    return sorted_matrix


def print_row_characteristics(matrix):

    print("\nХарактеристики строк (сумма положительных четных элементов):")
    for i, row in enumerate(matrix):
        characteristic = calculate_row_characteristic(row)
        print(f"Строка {i + 1}: {characteristic}")


def main():

    # Ввод размеров матрицы
    rows, cols = input_matrix_dimensions()

    # Ввод матрицы пользователем
    matrix = input_matrix(rows, cols)

    # Вывод исходной матрицы
    print_matrix(matrix, "Исходная матрица")

    # 1. Определение количества столбцов без нулевых элементов
    columns_without_zeros = count_columns_without_zeros(matrix)
    print(f"1. Количество столбцов без нулевых элементов: {columns_without_zeros}")

    # Вывод характеристик строк
    print_row_characteristics(matrix)

    # 2. Сортировка строк по характеристикам
    sorted_matrix = sort_rows_by_characteristics(matrix)

    # Вывод отсортированной матрицы
    print_matrix(sorted_matrix, "Матрица после сортировки строк по характеристикам")

    # Вывод характеристик отсортированных строк
    print_row_characteristics(sorted_matrix)


if __name__ == "__main__":
    main()