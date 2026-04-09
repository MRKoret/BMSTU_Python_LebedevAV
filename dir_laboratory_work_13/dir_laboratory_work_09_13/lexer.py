from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Ключевые слова
        self.lexer.add('PRINT', r'console\.log|alert')
        self.lexer.add('LET', r'let|var')
        self.lexer.add('CONST', r'const')

        # Скобки
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Точка с запятой
        self.lexer.add('SEMI_COLON', r'\;')

        # Операторы
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('ASSIGN', r'\=')

        # Числа
        self.lexer.add('NUMBER', r'\d+')

        # Идентификаторы
        self.lexer.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # Игнорируем пробелы
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()