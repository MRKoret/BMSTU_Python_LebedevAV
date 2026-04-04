from rply import ParserGenerator
from ast import Number, Sum, Sub, Mul, Div, Print, Assignment, Variable, Program


class Parser:
    def __init__(self, codegen):
        self.codegen = codegen
        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV',
             'ASSIGN', 'LET', 'CONST', 'ID'],
            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV']),
            ]
        )

    def parse(self):
        @self.pg.production('program : statements')
        def program(p):
            return Program(self.codegen, p[0])

        @self.pg.production('statements : statements statement')
        def statements_multiple(p):
            return p[0] + [p[1]]

        @self.pg.production('statements : statement')
        def statements_single(p):
            return [p[0]]

        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def statement_print(p):
            return Print(self.codegen, p[2])

        @self.pg.production('statement : LET ID ASSIGN expression SEMI_COLON')
        def statement_let(p):
            return Assignment(self.codegen, p[1].getstr(), p[3])

        @self.pg.production('statement : CONST ID ASSIGN expression SEMI_COLON')
        def statement_const(p):
            return Assignment(self.codegen, p[1].getstr(), p[3])

        @self.pg.production('statement : ID ASSIGN expression SEMI_COLON')
        def statement_assign(p):
            return Assignment(self.codegen, p[0].getstr(), p[2])

        @self.pg.production('statement : expression SEMI_COLON')
        def statement_expr(p):
            return Print(self.codegen, p[0])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if operator.gettokentype() == 'SUM':
                return Sum(self.codegen, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.codegen, left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(self.codegen, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.codegen, left, right)

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_paren(p):
            return p[1]

        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return Number(self.codegen, p[0].getstr())

        @self.pg.production('expression : ID')
        def expression_variable(p):
            return Variable(self.codegen, p[0].getstr())

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Синтаксическая ошибка: {token}")

    def get_parser(self):
        return self.pg.build()