# Создайте класс Матрица. Добавьте методы для:
# а. вывода на печать,
# б. сравнения,
# в. сложения,
# г. *умножения матриц

import argparse
from datetime import datetime
import logging
from UserException import MatrixError, SizeMatrixError, СompatibilityMatrixError, ElementsMatrixError

logging.basicConfig(level=0, filename='D:\GB\ДЗ\Погружение в Python\ДЗ15\log_z2.log', encoding='utf-8', style='{')
logger = logging.getLogger(__name__)

class Matrix():
    '''Операции с матрицами: печать, транспонирование, сравнение, сложение, умножение'''

    def __init__(self, matrix: list[list] | tuple[tuple]) -> None:
        len_ = len(matrix[0])
        check = True
        for i in matrix:
            if len(i) != len_:
                check = False
        if check == True:
            self.matrix = matrix
            logger.info(f'{datetime.now()}: Инициализация матрицы {matrix}')
        else:
            logger.error(f'{datetime.now()}: {NameError(MatrixError())}')
            raise MatrixError()
        

    def print_matrix_class(self):
        '''Печать экземпляра класса Matrix'''
        result = ''
        for i in self.matrix:
            result += str(i) + '\n'
        logger.info(f'{datetime.now()}: Печать матрицы \n{result}')
        return result[:-1]
    

    def matrix_transposition(self) -> list[list]:
        '''Транспонирование матрицы'''
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
        logger.info(f'{datetime.now()}: Транспонирование матрицы')
        return result
    

    def __eq__(self, other):
        '''Сравнение матриц'''
        result = True
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            result = False
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        result = False 
        logger.info(f'{datetime.now()}: Сравнение матриц, результат {result}')
        return result
    

    def __add__(self, other):
        '''Сложение матриц: матрицы должны быть одного размера'''
        lines = len(self.matrix)
        columns = len(self.matrix[0])
        if lines != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            logger.error(f'{datetime.now()}: {SizeMatrixError()}')
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
                        logger.error(f'{datetime.now()}: {ElementsMatrixError()}')
                        raise ElementsMatrixError()
        logger.info(f'{datetime.now()}: Сложение матриц')
        return result
    

    def __mul__(self, other):
        '''Умножение матриц: матрицы должны быть совместимы(число столбцов первой матрицы длжно быть равно числу строк второй матрицы)'''
        lines1 = len(self.matrix)
        columns1 = len(self.matrix[0])
        lines2 = len(other.matrix)
        columns2 = len(other.matrix[0]) 
        if columns1 != lines2:
            logger.error(f'{datetime.now()}: {СompatibilityMatrixError()}')
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
                            logger.error(f'{datetime.now()}: {ElementsMatrixError()}')
                            raise ElementsMatrixError()
                    result[i][j] = sum
        logger.info(f'{datetime.now()}: Умножение матриц')
        return result
    

    def __str__(self):
        logger.info(f'{datetime.now()}: Печать матрицы в строку')
        return f'{self.matrix}'
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='class Matrix', description='Операции с матрицами (транспонирование, сравнение, сложение, умножение, печать', \
                                                                               epilog='class Matrix')
    parser.add_argument('-m1', metavar ='m1', type = lambda s: [int(item) for item in s.split(',')], nargs = '+', \
                        help = 'Матрица1(пример ввода: 1,2,3 4,5,6 7,8,9)')
    parser.add_argument('-m2', metavar ='m2', type = lambda s: [int(item) for item in s.split(',')], nargs = '+', \
                    help = 'Матрица1(пример ввода: 1,2,3 4,5,6 7,8,9)', default = ((0,0,0),(0,0,0)))
    parser.add_argument('-o', metavar ='0', type = int, help = '1 - печать матрицы, 2 - транспонирование матрицы, 3 - сравнение матриц, \
                        4 - сложение матриц, 5 - умножение матриц', default = 1)    
    args = parser.parse_args()
    matr1 = Matrix(args.m1)
    matr2 = Matrix(args.m2)
    match args.o:
        case 1:
            print(matr1.print_matrix_class())
        case 2:
            print(Matrix(matr1.matrix_transposition()).print_matrix_class())
        case 3:
            print(matr1 == matr2)
        case 4:
            print(Matrix(matr1 + matr2).print_matrix_class())
        case 5:
            print(Matrix(matr1 * matr2).print_matrix_class())
        case _:
            raise ValueError('Недопустимый параметр -o')

