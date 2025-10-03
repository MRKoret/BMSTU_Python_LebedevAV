import random


def main():
    # Ввод количества элементов
    n = int(input("Введите количество элементов массива (n): "))

    # Создание массива из n вещественных чисел
    arr = []
    for i in range(n):
        arr.append(random.uniform(-10, 10))

    print("Исходный массив:")
    for i in range(n):
        print(f"{arr[i]:8.3f}", end=" ")
    print()

    # 1. Сумма положительных элементов
    sum_positive = 0.0
    for num in arr:
        if num > 0:
            sum_positive += num

    # 2. Произведение элементов между максимальным по модулю и минимальным по модулю элементами
    # Находим индексы максимального и минимального по модулю элементов
    max_abs_index = 0
    min_abs_index = 0

    for i in range(1, n):
        if abs(arr[i]) > abs(arr[max_abs_index]):
            max_abs_index = i
        if abs(arr[i]) < abs(arr[min_abs_index]):
            min_abs_index = i

    # Определяем начальный и конечный индексы для произведения
    start_index = min(max_abs_index, min_abs_index)
    end_index = max(max_abs_index, min_abs_index)

    product = 1.0
    has_elements_between = False

    for i in range(start_index + 1, end_index):
        product *= arr[i]
        has_elements_between = True

    # Если между элементами нет других элементов, произведение = 0
    if not has_elements_between:
        product = 0.0

    # 3. Упорядочиваем массив по убыванию
    # Используем пузырьковую сортировку для упорядочивания по убыванию
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("\nРезультаты:")
    print(f"1. Сумма положительных элементов: {sum_positive:.3f}")
    print(f"2. Произведение элементов между максимальным по модулю и минимальным по модулю: {product:.3f}")

    print("3. Массив, упорядоченный по убыванию:")
    for i in range(n):
        print(f"{arr[i]:8.3f}", end=" ")
    print()

    # Дополнительная информация для проверки
    print(f"\nДополнительная информация:")
    print(
        f"Максимальный по модулю элемент: arr[{max_abs_index}] = {arr[max_abs_index]:.3f} (модуль = {abs(arr[max_abs_index]):.3f})")
    print(
        f"Минимальный по модулю элемент: arr[{min_abs_index}] = {arr[min_abs_index]:.3f} (модуль = {abs(arr[min_abs_index]):.3f})")
    print(f"Индексы для произведения: от {start_index + 1} до {end_index - 1}")


if __name__ == "__main__":
    main()