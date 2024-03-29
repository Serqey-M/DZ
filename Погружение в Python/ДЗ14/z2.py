# Создайте класс Матрица. Добавьте методы для:
# а. вывода на печать,
# б. сравнения,
# в. сложения,
# г. *умножения матриц

from UserException import MatrixError, SizeMatrixError, СompatibilityMatrixError, ElementsMatrixError

class Matrix():
    '''Операции с матрицами: печать, транспонирование, сравнение, сложение, умножение
    >>> print(Matrix(Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))).matrix_transposition()).print_matrix_class())
    [1, 4, 7, 1]
    [2, 5, 8, 2]
    [3, 5, 9, 3]
    [4, 7, 5, 8]
    '''

    def __init__(self, matrix: list[list] | tuple[tuple]) -> None:
        '''
    >>> Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 9, 5), (1, 2, 3, 8)))
    Traceback (most recent call last):
    ...
    UserException.MatrixError: Аргумент не является матрицей. В матрице все строки должны быть одного размера
      '''
        len_ = len(matrix[0])
        check = True
        for i in matrix:
            if len(i) != len_:
                check = False
        if check == True:
            self.matrix = matrix
        else:
            raise MatrixError()


    def print_matrix_class(self):
        '''Печать экземпляра класса Matrix
    >>> print(Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))).print_matrix_class())
    (1, 2, 3, 4)
    (4, 5, 5, 7)
    (7, 8, 9, 5)
    (1, 2, 3, 8)
        '''
        result = ''
        for i in self.matrix:
            result += str(i) + '\n'
        return result[:-1]
    

    def matrix_transposition(self) -> list[list]:
        '''Транспонирование матрицы
    >>> print(Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))).matrix_transposition())
    [[1, 4, 7, 1], [2, 5, 8, 2], [3, 5, 9, 3], [4, 7, 5, 8]]
        '''
        lines = len(self.matrix)
        columns = len(self.matrix[0])
        result = []
        for i in range(columns):
            result.append([])
            for _ in range(lines):
                result[i].append(0)
        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[0])): 
                result[j][i] = self.matrix[i][j] 
        return result
    

    def __eq__(self, other):
        '''Сравнение матриц
        >>> Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))) == Matrix(((1, 2, 3, 5), (4, 5, 6, 6), (7, 8, 9, 7), (1, 2, 3, 8)))
        False
        >>> Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))) == Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8)))
        True
        '''
        result = True
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            result = False
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        result = False 
        return result
    

    def __add__(self, other):
        '''Сложение матриц: матрицы должны быть одного размера
        >>> Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))) + Matrix(((1, 2, 3, 5), (4, 5, 6, 6), (7, 8, 9, 7), (1, 2, 3, 8)))
        [[2, 4, 6, 9], [8, 10, 11, 13], [14, 16, 18, 12], [2, 4, 6, 16]]
        '''
        lines = len(self.matrix)
        columns = len(self.matrix[0])
        if lines != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise SizeMatrixError()
        else:
            result = []
            for i in range(lines):
                result.append([])
                for _ in range(columns):
                    result[i].append(0)
            for i in range(lines):
                for j in range(len(self.matrix[i])):
                    try:
                        result[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    except:
                        raise ElementsMatrixError()
        return result
    

    def __mul__(self, other):
        '''Умножение матриц: матрицы должны быть совместимы(число столбцов первой матрицы длжно быть равно числу строк второй матрицы)
        >>> Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))) * Matrix(((1, 2, 3, 5), (4, 5, 6, 6), (7, 8, 9, 7), (1, 2, 3, 8)))
        [[34, 44, 54, 70], [66, 87, 108, 141], [107, 136, 165, 186], [38, 52, 66, 102]]
        '''
        lines1 = len(self.matrix)
        columns1 = len(self.matrix[0])
        lines2 = len(other.matrix)
        columns2 = len(other.matrix[0]) 
        if columns1 != lines2:
            raise СompatibilityMatrixError() 
        else:      
            result = []
            for i in range(lines1):
                    result.append([])
                    for _ in range(columns2):
                        result[i].append(0)        
            for i in range(lines1):
                for j in range(columns2):
                    sum = 0
                    for n in range(columns1):
                        try:
                            sum += self.matrix[i][n]*other.matrix[n][j]
                        except:
                            raise ElementsMatrixError()
                    result[i][j] = sum
        return result
    

    def __str__(self):
        '''
        >>> print(Matrix(((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))))
        ((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))
        '''
        return f'{self.matrix}'
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)