class UserException(Exception):
    pass


class NameError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not self.value.isalpha() and not self.value.istitle():
            text = 'Значение должно содержать только буквы и начинаться с заглавной буквы.'
        elif not self.value.isalpha():
            text = 'Значение должно содержать только буквы.'
        elif not self.value.istitle():
            text = 'Значение длжно начинаться с заглавной буквы.'
        return f'Значение {self.value} не соответствует требованиям. {text}'
    

class AssessmentError(UserException):
    def __init__(self, value, min_value, max_value):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        if self.value < self.min_value:
            text = 'меньше минимального значения'
        elif self.value > self.max_value:
            text = 'больше максимального значения'
        return f'Оценка {self.value} {text}. Оценка должна от {self.min_value} до {self.max_value}'

class TypeError(UserException):
        def __str__(self) -> str:
            return 'Некоректное значение аргумента type_. type_ может принимать значение 1 (ввод оценки) или 0 (ввод результата теста)'
        
class MatrixError(UserException):
    def __str__(self) -> str:
        return 'Аргумент не является матрицей. В матрице все строки должны быть одного размера'
    
class SizeMatrixError(UserException):
    def __str__(self) -> str:
        return 'Матрицы разного размера, сложение не возможно'
    
class СompatibilityMatrixError(UserException):
    def __str__(self) -> str:
        return 'Матрицы не совместимы, перемножение не возможно(число столбцов первой матрицы длжно быть равно числу строк второй матрицы)'
    
class ElementsMatrixError(UserException):
    def __str__(self) -> str:
        return 'Матрица содержит не числовые элементы'
    
class BackpackError(UserException):
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        if not isinstance(self.value, (float, int)):
            text = 'иметь тип float'
        elif self.value <= 0:
            text = 'быть больше 0'
        return f'Не коректное значение аргумета backpack_capacity. Аргумент должен {text}'