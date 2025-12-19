"""
Парсер для двух режимов
"""

from typing import List
from lexer import Token, TokenType, TextLexer, MathLexer
from ast import (
    ASTNode, NumberNode, BinaryOpNode, UnaryOpNode, FunctionCallNode
)

class BaseParser:
    """Базовый парсер"""

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0] if self.tokens else None

    def error(self, message: str):
        """Генерирует ошибку"""
        token_info = f" токен {self.current_token}" if self.current_token else ""
        raise Exception(f'Ошибка парсера: {message}{token_info}')

    def eat(self, token_type: TokenType):
        """Проверяет текущий токен и переходит к следующему"""
        if self.current_token.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current_token = self.tokens[self.pos]
            else:
                self.current_token = None
        else:
            self.error(f'Ожидался {token_type}, получен {self.current_token.type}')

    def parse(self) -> ASTNode:
        """Основной метод парсинга - должен быть переопределен"""
        raise NotImplementedError

class TextParser(BaseParser):
    """Парсер для текста (слов)"""

    def parse(self) -> ASTNode:
        """Парсит выражения из слов"""
        node = self.expr()

        if self.current_token and self.current_token.type != TokenType.EOF:
            self.error(f'Неожиданный токен')

        return node

    def expr(self) -> ASTNode:
        """Сложение и вычитание"""
        node = self.term()

        while self.current_token and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinaryOpNode(node, token.value, self.term())

        return node

    def term(self) -> ASTNode:
        """Умножение и деление"""
        node = self.factor()

        while self.current_token and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token.type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
            elif token.type == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)

            node = BinaryOpNode(node, token.value, self.factor())

        return node

    def factor(self) -> ASTNode:
        """Степени и атомарные выражения"""
        node = self.atom()

        while self.current_token and self.current_token.type == TokenType.POWER:
            token = self.current_token
            self.eat(TokenType.POWER)
            node = BinaryOpNode(node, token.value, self.atom())

        return node

    def atom(self) -> ASTNode:
        """Атомарные выражения"""
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return NumberNode(token.value)

        elif token.type == TokenType.SQRT:
            self.eat(TokenType.SQRT)
            # Для текста: sqrt следующий аргумент
            arg = self.atom()
            return FunctionCallNode('sqrt', arg)

        elif token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            return self.atom()

        elif token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            return UnaryOpNode('-', self.atom())

        else:
            self.error(f'Неожиданный токен в тексте')

class MathParser(BaseParser):
    """Парсер для математических выражений"""

    def parse(self) -> ASTNode:
        """Парсит математические выражения"""
        node = self.expr()

        if self.current_token and self.current_token.type != TokenType.EOF:
            self.error(f'Неожиданный токен')

        return node

    def expr(self) -> ASTNode:
        """Сложение и вычитание"""
        node = self.term()

        while self.current_token and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinaryOpNode(node, token.value, self.term())

        return node

    def term(self) -> ASTNode:
        """Умножение и деление"""
        node = self.factor()

        while self.current_token and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token.type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
            elif token.type == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)

            node = BinaryOpNode(node, token.value, self.factor())

        return node

    def factor(self) -> ASTNode:
        """Степени"""
        node = self.atom()

        while self.current_token and self.current_token.type == TokenType.POWER:
            token = self.current_token
            self.eat(TokenType.POWER)
            node = BinaryOpNode(node, token.value, self.atom())

        return node

    def atom(self) -> ASTNode:
        """Атомарные выражения"""
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return NumberNode(token.value)

        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

        elif token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            return self.atom()

        elif token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            return UnaryOpNode('-', self.atom())

        elif token.type == TokenType.SQRT:
            self.eat(TokenType.SQRT)

            # Ожидаем скобки
            if self.current_token and self.current_token.type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                node = self.expr()
                self.eat(TokenType.RPAREN)
            else:
                # Без скобок (простой вариант)
                node = self.atom()

            return FunctionCallNode('sqrt', node)

        else:
            self.error(f'Неожиданный токен в математике')