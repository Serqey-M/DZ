# Напишите функцию для транспонирования матрицы

MATRIX = ((10, 20, 30, 40),
          (40, 50, 60, 30),
          (70, 80, 90, 50))


def matrix_transposition (matrix: list[list] | tuple[tuple]) -> list[list]:
    lines = len(matrix)
    columns = len(matrix[0])
    result = []
    for i in range(columns):
        result.append([])
        for _ in range(lines):
            result[i].append(0)
    for i in range(len(matrix)): 
       for j in range(len(matrix[0])): 
           result[j][i] = matrix[i][j] 
    return result

  
if __name__ == '__main__':
    print('Начальная матрица')
    for i in MATRIX: 
       print(i)
    print('Итоговая матрица')
    for i in matrix_transposition(MATRIX): 
       print(i)