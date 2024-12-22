class MyClass:

    def method_1(self) -> None:
        print('method 1')
        self.__method_2()

    def __method_2(self) -> None:
        print('method 2')


obj = MyClass()
obj.method_1()
# obj.__method_2()  # método privado não pode ser acessado diretamente por um objeto da classe
