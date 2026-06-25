"""
Модуль для работы со словами в тексте.
"""
def longest_word(s):
    """
    Возвращает самое длинное слово из строки.

    Args:
        s (str): Входная строка

    Returns:
        str: Самое длинное слово или пустая строка
    """
    words = s.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

if __name__ == "__main__":
    print("Тестирование longest_word:")
    print(longest_word("Я люблю программирование"))  # "программирование"
    print(longest_word("Python мой второй язык"))  # "Python"
    print(longest_word(""))  # ""