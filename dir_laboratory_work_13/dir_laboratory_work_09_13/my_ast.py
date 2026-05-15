from llvmlite import ir


class Number:
    def __init__(self, codegen, value):
        self.codegen = codegen
        self.value = value

    def eval(self):
        if self.codegen:
            return ir.Constant(ir.IntType(32), int(self.value))
        return int(self.value)


class BinaryOp:
    def __init__(self, codegen, left, right):
        self.codegen = codegen
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        if self.codegen:
            return self.codegen.builder.add(self.left.eval(), self.right.eval())
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        if self.codegen:
            return self.codegen.builder.sub(self.left.eval(), self.right.eval())
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        if self.codegen:
            return self.codegen.builder.mul(self.left.eval(), self.right.eval())
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        if self.codegen:
            right_val = self.right.eval()
            return self.codegen.builder.sdiv(self.left.eval(), right_val)
        return self.left.eval() / self.right.eval()


class Print:
    def __init__(self, codegen, value):
        self.codegen = codegen
        self.value = value

    def eval(self):
        value = self.value.eval()
        if self.codegen:
            return self.codegen.create_print(value)
        print(value)
        return value


class Assignment:
    def __init__(self, codegen, name, value):
        self.codegen = codegen
        self.name = name
        self.value = value

    def eval(self):
        value = self.value.eval()
        if self.codegen:
            self.codegen.create_variable(self.name, value)
        return value


class Variable:
    def __init__(self, codegen, name):
        self.codegen = codegen
        self.name = name

    def eval(self):
        if self.codegen:
            return self.codegen.get_variable(self.name)
        return None


class Program:
    def __init__(self, codegen, statements):
        self.codegen = codegen
        self.statements = statements

    def eval(self):
        result = None
        for stmt in self.statements:
            result = stmt.eval()
        return result