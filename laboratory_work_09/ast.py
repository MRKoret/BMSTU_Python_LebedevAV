"""
Абстрактное синтаксическое дерево
"""

from enum import Enum
from typing import List

class ASTNodeType(Enum):
    """Типы узлов AST"""
    NUMBER = 'NUMBER'
    BINARY_OP = 'BINARY_OP'
    UNARY_OP = 'UNARY_OP'
    FUNCTION_CALL = 'FUNCTION_CALL'

class ASTNode:
    """Базовый класс для узлов AST"""

    def __init__(self, node_type: ASTNodeType):
        self.node_type = node_type

    def __repr__(self):
        return f"{self.node_type.value}()"

    def accept(self, visitor):
        """Для паттерна Visitor"""
        method_name = f'visit_{self.__class__.__name__}'
        visitor_method = getattr(visitor, method_name, visitor.generic_visit)
        return visitor_method(self)

class NumberNode(ASTNode):
    """Узел для чисел"""

    def __init__(self, value: float):
        super().__init__(ASTNodeType.NUMBER)
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

class BinaryOpNode(ASTNode):
    """Узел для бинарных операций"""

    def __init__(self, left: ASTNode, operator: str, right: ASTNode):
        super().__init__(ASTNodeType.BINARY_OP)
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOp('{self.operator}', {self.left}, {self.right})"

class UnaryOpNode(ASTNode):
    """Узел для унарных операций"""

    def __init__(self, operator: str, operand: ASTNode):
        super().__init__(ASTNodeType.UNARY_OP)
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return f"UnaryOp('{self.operator}', {self.operand})"

class FunctionCallNode(ASTNode):
    """Узел для вызова функций"""

    def __init__(self, function_name: str, argument: ASTNode):
        super().__init__(ASTNodeType.FUNCTION_CALL)
        self.function_name = function_name
        self.argument = argument

    def __repr__(self):
        return f"FunctionCall('{self.function_name}', {self.argument})"

class ASTVisualizer:
    """Визуализирует AST"""

    def visualize(self, node: ASTNode, level: int = 0, prefix: str = "") -> str:
        """Рекурсивно визуализирует AST"""
        result = []
        indent = "  " * level

        # Текущий узел
        node_info = f"{indent}{prefix}{node.__class__.__name__}"

        if isinstance(node, NumberNode):
            node_info += f"({node.value})"
        elif isinstance(node, BinaryOpNode):
            node_info += f"('{node.operator}')"
        elif isinstance(node, UnaryOpNode):
            node_info += f"('{node.operator}')"
        elif isinstance(node, FunctionCallNode):
            node_info += f"('{node.function_name}')"

        result.append(node_info)

        # Дети узла
        if isinstance(node, BinaryOpNode):
            result.append(self.visualize(node.left, level + 1, "left: "))
            result.append(self.visualize(node.right, level + 1, "right: "))
        elif isinstance(node, UnaryOpNode):
            result.append(self.visualize(node.operand, level + 1, "operand: "))
        elif isinstance(node, FunctionCallNode):
            result.append(self.visualize(node.argument, level + 1, "arg: "))

        return "\n".join(result)

    def print_ast(self, node: ASTNode, title: str = "AST"):
        """Печатает AST"""
        print(f"\n🌳 {title}:")
        print("=" * 50)
        print(self.visualize(node))
        print("=" * 50)