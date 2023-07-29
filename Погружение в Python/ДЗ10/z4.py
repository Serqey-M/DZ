# Напишите функцию для транспонирования матрицы

class Matrix():
    def __init__(self, matrix: list[list] | tuple[tuple]) -> None:
        self.matrix = matrix

    def matrix_transposition(self) -> list[list]:
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
    
    def print_matrix(self, matrix):
        for i in matrix: 
            print(i)


  
if __name__ == '__main__':
    matrix = ((10, 20, 30, 40),
               (40, 50, 60, 30),
               (70, 80, 90, 50))
    matr = Matrix(matrix)
    print('Начальная матрица')
    matr.print_matrix(matrix)
    matr_tr = matr.matrix_transposition()
    print('Транспонированная матрица')
    matr.print_matrix(matr_tr)



