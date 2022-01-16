# Kalkulator z zadania_1

class Calculator:
    def __init__(self):
        self.error = None

    def __valid_number(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return True
        else:
            self.error = f"{type(a)} a={a} | {type(b)} b={b} \n Both should be <class 'int'>"

    def addition(self, a, b):
        return a + b if self.__valid_number(a, b) else self.error

    def subtraction(self, a, b):
        return a - b if self.__valid_number(a, b) else self.error
