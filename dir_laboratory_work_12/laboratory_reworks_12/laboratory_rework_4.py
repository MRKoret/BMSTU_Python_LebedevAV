from random import uniform

__all__ = [
    'create_random_array',
    'sum_positive_elements',
    'sort_by_absolute_value',
    'product_between_min_max_abs',
    'sort_descending',
    'get_valid_array_size'
]

def get_valid_array_size(min_size: int = 5, max_size: int = 30):
    while True:
        try:
            print("Запуск лабораторной работы №4...")
            n = int(input(f"Введите кол-во элементов в массиве (от {min_size} до {max_size}): "))

            if n < min_size:
                print(f"Значение меньше {min_size}, установлено значение {min_size}")
                return min_size
            elif n > max_size:
                print(f"Значение больше {max_size}, установлено значение {max_size}")
                return max_size
            return n
        except ValueError:
            print("Ошибка! Введите целое число.")

def create_random_array(size: int, min_val: float = -5, max_val: float = 5):
    return [uniform(min_val, max_val) for _ in range(size)]

def sum_positive_elements(arr: list):
    return sum(x for x in arr if x > 0)

def sort_by_absolute_value(arr: list, reverse: bool = True):
    return sorted(arr, key=lambda x: abs(x), reverse=reverse)

def product_between_min_max_abs(arr: list):
    if len(arr) < 2:
        return 0.0

    # Находим индексы элементов с минимальным и максимальным модулем
    abs_values = [abs(x) for x in arr]

    min_abs_index = abs_values.index(min(abs_values))
    max_abs_index = abs_values.index(max(abs_values))

    # Определяем границы
    left = min(min_abs_index, max_abs_index)
    right = max(min_abs_index, max_abs_index)

    # Если элементы рядом или это один элемент
    if right - left <= 1:
        return 0.0

    # Произведение элементов между ними
    product = 1
    for i in range(left + 1, right):
        product *= arr[i]

    return product

def sort_descending(arr: list):
    return sorted(arr, reverse=True)

def get_positive_elements(arr: list):
    return [x for x in arr if x > 0]

def main():
    # Ввод размера и создание массива
    size = get_valid_array_size()
    original_array = create_random_array(size)

    # Положительные элементы
    positive_elements = get_positive_elements(original_array)
    positive_sum = sum_positive_elements(original_array)

    # Сортировка по модулю
    sorted_by_abs = sort_by_absolute_value(original_array)

    # Произведение между min и max по модулю
    product = product_between_min_max_abs(original_array)

    # Сортировка по убыванию
    sorted_desc = sort_descending(original_array)

    # Вывод результатов
    print("=" * 200)
    print(f"Изначальный список: {original_array}")
    print(f"Положительные элементы: {positive_elements}")
    print(f"Сумма положительных элементов: {positive_sum:.2f}")
    print(f"Список, отсортированный по модулю (убывание): {sorted_by_abs}")
    print(f"Произведение элементов между min и max по модулю: {product:.4f}")
    print(f"Список, отсортированный по убыванию: {sorted_desc}")
    print("Конец вывода")
    print("-------------------------------------------")

if __name__ == "__main__":
    main()
else:
    print("Модуль лабораторной работы №4 импортирован")
    print("-------------------------------------------")
    main()