from lexer import Lexer
from parser import Parser
from codegen import CodeGen

# Тестовая программа
js_code = """
let x = 10;
let y = 20;
console.log(x + y);
console.log(x * y);
"""

# Создаем CodeGen
codegen = CodeGen()

# Создаем лексер и парсер
lexer = Lexer().get_lexer()
parser = Parser(codegen)
parser.parse()
pg = parser.get_parser()

# Разбираем и выполняем
tokens = lexer.lex(js_code)
ast = pg.parse(tokens)
ast.eval()

# Компилируем и запускаем
codegen.create_ir()
codegen.save_ir("output.ll")
codegen.run()

test_cases = [
    "console.log(2 + 3);",
    "console.log((2 + 3) * 4);",
    "let a = 5; let b = 3; console.log(a * b);"
]

for test in test_cases:
    print(f"\n {test}")

    # Новый codegen для каждого теста
    cg = CodeGen()
    p = Parser(cg)
    p.parse()
    pg_test = p.get_parser()

    tokens_test = lexer.lex(test)
    ast_test = pg_test.parse(tokens_test)
    ast_test.eval()

    cg.create_ir()
    cg.run()

# Сохраняем исходный код
with open("input.js", "w", encoding="utf-8") as f:
    f.write(js_code)