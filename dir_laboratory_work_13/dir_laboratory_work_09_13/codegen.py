from llvmlite import ir, binding


class CodeGen:
    def __init__(self):
        self.binding = binding
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._config_llvm()
        self._create_execution_engine()
        self._declare_print_function()

        # Словарь для переменных
        self.variables = {}
        self.counter = 0  # Счетчик для уникальных имен

    def _config_llvm(self):
        """Настройка LLVM"""
        self.module = ir.Module(name="js_compiler")
        self.module.triple = self.binding.get_default_triple()

        # Создаем функцию main
        func_type = ir.FunctionType(ir.IntType(32), [], False)
        self.main_func = ir.Function(self.module, func_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def _create_execution_engine(self):
        """Создание ExecutionEngine"""
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        backing_mod = self.binding.parse_assembly("")
        self.engine = self.binding.create_mcjit_compiler(backing_mod, target_machine)

    def _declare_print_function(self):
        """Объявление функции printf"""
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

    def create_print(self, value):
        """Создание вывода с уникальным именем"""
        self.counter += 1
        fmt_name = f"fstr_{self.counter}"

        # Создаем форматную строку
        fmt = "%d\n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))

        # Глобальная переменная с уникальным именем
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=fmt_name)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt

        # Преобразуем указатель
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Вызываем printf
        self.builder.call(self.printf, [fmt_arg, value])
        return value

    def create_variable(self, name, value):
        """Создание переменной"""
        self.variables[name] = value
        return value

    def get_variable(self, name):
        """Получение переменной"""
        return self.variables.get(name, ir.Constant(ir.IntType(32), 0))

    def create_ir(self):
        """Создание IR"""
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

        # Валидация и добавление в движок
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()

        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod

    def save_ir(self, filename):
        """Сохранение IR в файл"""
        with open(filename, 'w') as f:
            f.write(str(self.module))
        print(f"LLVM IR сохранен в {filename}")

    def run(self):
        """Запуск скомпилированного кода"""
        func_ptr = self.engine.get_function_address("main")

        import ctypes
        cfunc = ctypes.CFUNCTYPE(ctypes.c_int)(func_ptr)
        result = cfunc()
        print(f"Код завершился с результатом: {result}")
        return result