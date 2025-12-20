"""
Лексический анализатор - две версии:
1. Для текста (слов)
2. Для математических выражений (символов)
"""

import re
from enum import Enum
from typing import List, Tuple

class TokenType(Enum):
    """Типы токенов"""
    NUMBER = 'NUMBER'      # Числа
    PLUS = 'PLUS'          # +
    MINUS = 'MINUS'        # -
    MULTIPLY = 'MULTIPLY'  # *
    DIVIDE = 'DIVIDE'      # /
    POWER = 'POWER'        # ^
    SQRT = 'SQRT'          # sqrt
    LPAREN = 'LPAREN'      # (
    RPAREN = 'RPAREN'      # )
    WORD = 'WORD'          # Слова (только в текстовом режиме)
    EOF = 'EOF'            # Конец

class Token:
    """Токен"""

    def __init__(self, type: TokenType, value: str = None, position: Tuple[int, int] = (0, 0)):
        self.type = type
        self.value = value
        self.start, self.end = position

    def __repr__(self):
        if self.value:
            return f"{self.type.name}('{self.value}')"
        return f"{self.type.name}"

# ============================================
# 1. ЛЕКСЕР ДЛЯ ТЕКСТА (СЛОВА)
# ============================================

class TextLexer:
    """Лексический анализатор для текста (слов)"""

    def __init__(self, text: str):
        from dictionary import MathDictionary
        self.dict = MathDictionary
        self.text = self.dict.normalize_text(text)
        self.pos = 0
        self.current_char = self.text[0] if self.text else None

    def advance(self):
        """Переходит к следующему символу"""
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Пропускает пробелы"""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_word(self) -> str:
        """Получает целое слово"""
        start_pos = self.pos
        result = ''

        while self.current_char is not None and not self.current_char.isspace():
            result += self.current_char
            self.advance()

        return result

    def get_next_token(self) -> Token:
        """Получает следующий токен"""

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Получаем слово
            word = self.get_word()

            # Преобразуем слово в символ
            symbol = self.dict.word_to_symbol(word)

            # Определяем тип токена
            if symbol.isdigit() or (symbol[0] == '-' and symbol[1:].isdigit()):
                return Token(TokenType.NUMBER, float(symbol), (self.pos-len(word), self.pos))
            elif symbol == '+':
                return Token(TokenType.PLUS, '+', (self.pos-len(word), self.pos))
            elif symbol == '-':
                return Token(TokenType.MINUS, '-', (self.pos-len(word), self.pos))
            elif symbol == '*':
                return Token(TokenType.MULTIPLY, '*', (self.pos-len(word), self.pos))
            elif symbol == '/':
                return Token(TokenType.DIVIDE, '/', (self.pos-len(word), self.pos))
            elif symbol == '^   ':
                return Token(TokenType.POWER, '^', (self.pos-len(word), self.pos))
            elif symbol == 'sqrt':
                return Token(TokenType.SQRT, 'sqrt', (self.pos-len(word), self.pos))
            else:
                # Если не преобразовалось, оставляем как слово
                return Token(TokenType.WORD, word, (self.pos-len(word), self.pos))

        return Token(TokenType.EOF)

    def tokenize(self) -> List[Token]:
        """Разбивает текст на токены"""
        tokens = []

        # Сбрасываем позицию
        self.pos = 0
        self.current_char = self.text[0] if self.text else None

        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        return tokens

    def pretty_print(self, tokens: List[Token]):
        """Красиво выводит токены"""
        print("\nТОКЕНЫ ИЗ ТЕКСТА:")
        print("-" * 40)
        for token in tokens[:-1]:  # Не выводим EOF
            if token.type == TokenType.WORD:
                print(f"  {token.type.name:10} → '{token.value}' (не распознано)")
            else:
                print(f"  {token.type.name:10} → {token.value}")
        print("-" * 40)

# ============================================
# 2. ЛЕКСЕР ДЛЯ МАТЕМАТИКИ (СИМВОЛЫ)
# ============================================

class MathLexer:
    """Лексический анализатор для математических выражений"""

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None

    def error(self, message: str):
        """Генерирует ошибку"""
        raise Exception(f'Ошибка лексера: {message} на позиции {self.pos}')

    def advance(self):
        """Переходит к следующему символу"""
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Пропускает пробелы"""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self) -> Token:
        """Считывает число"""
        start_pos = self.pos
        result = ''

        # Считываем целую часть
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        # Дробная часть
        if self.current_char == '.':
            result += '.'
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

        try:
            value = float(result)
            return Token(TokenType.NUMBER, value, (start_pos, self.pos))
        except:
            self.error(f"Неверное число: {result}")

    def get_next_token(self) -> Token:
        """Получает следующий токен"""

        while self.current_char is not None:

            # Пропускаем пробелы
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Числа
            if self.current_char.isdigit():
                return self.number()

            # Операторы
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+', (self.pos - 1, self.pos))

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-', (self.pos - 1, self.pos))

            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY, '*', (self.pos - 1, self.pos))

            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE, '/', (self.pos - 1, self.pos))

            if self.current_char == '^':
                self.advance()
                return Token(TokenType.POWER, '^', (self.pos - 1, self.pos))

            # Скобки
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(', (self.pos - 1, self.pos))

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')', (self.pos - 1, self.pos))

            # Точка в начале числа (например, .5)
            if self.current_char == '.':
                # Это начало дробного числа без целой части
                return self.number()

            # Функция sqrt
            if self.current_char == 's':
                # Проверяем, не "sqrt" ли это
                if self.pos + 4 <= len(self.text) and self.text[self.pos:self.pos + 4] == 'sqrt':
                    start_pos = self.pos
                    for _ in range(4):
                        self.advance()
                    return Token(TokenType.SQRT, 'sqrt', (start_pos, self.pos))
                else:
                    self.error(f"Неизвестный символ: {self.current_char}")

            self.error(f"Неизвестный символ: '{self.current_char}'")

        return Token(TokenType.EOF)

    def tokenize(self) -> List[Token]:
        """Разбивает текст на токены"""
        tokens = []

        self.pos = 0
        self.current_char = self.text[0] if self.text else None

        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        return tokens

    def pretty_print(self, tokens: List[Token]):
        """Красиво выводит токены"""
        print("\nТОКЕНЫ ИЗ МАТЕМАТИКИ:")
        print("-" * 40)
        for token in tokens[:-1]:  # Не выводим EOF
            print(f"  {token.type.name:10} → {token.value}")
        print("-" * 40)