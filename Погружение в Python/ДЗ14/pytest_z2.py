import pytest
import z2
import UserException


@pytest.fixture
def matrix1():
    return ((1, 2, 3, 4),
            (4, 5, 5, 7),
            (7, 8, 9, 5),
            (1, 2, 3, 8))

@pytest.fixture
def matrix2():
    return ((1, 2, 3, 5), 
            (4, 5, 6, 6), 
            (7, 8, 9, 7), 
            (1, 2, 3, 8))

@pytest.fixture
def matrix3():
    return ((1, 2, 3, 4),
            (4, 5, 5, 7),
            (7, 8, 9, 5),
            (1, 2, 3, 8))

@pytest.fixture
def matrix4():
    return ((1, 2, 3, 4),
            (4, 5, 5, 7),
            (7, 8, 9), 
            (1, 2, 3, 8))

def test_matrix(matrix1):
    matr1 = z2.Matrix(matrix1)
    matr_tr = z2.Matrix(matr1.matrix_transposition())
    result = '[1, 4, 7, 1]\n[2, 5, 8, 2]\n[3, 5, 9, 3]\n[4, 7, 5, 8]'
    assert matr_tr.print_matrix_class() == result

def test_error_init(matrix4):
    with pytest.raises(UserException.MatrixError, match = r'Аргумент не является матрицей. В матрице все строки должны быть одного размера'):
        z2.Matrix(matrix4)

def test_print(matrix1):
    matr1 = z2.Matrix(matrix1)
    result= '(1, 2, 3, 4)\n(4, 5, 5, 7)\n(7, 8, 9, 5)\n(1, 2, 3, 8)'
    assert matr1.print_matrix_class(), result

def test_tr(matrix1):
    matr1 = z2.Matrix(matrix1)
    result = [[1, 4, 7, 1], [2, 5, 8, 2], [3, 5, 9, 3], [4, 7, 5, 8]]
    assert matr1.matrix_transposition(), result

def test_eq1(matrix1, matrix2):
    matr1 = z2.Matrix(matrix1)
    matr2 = z2.Matrix(matrix2)
    assert not matr1 == matr2

def test_eq(matrix1, matrix3):
    matr1 = z2.Matrix(matrix1)
    matr3 = z2.Matrix(matrix3)
    assert matr1 == matr3

def test_add(matrix1, matrix2):
    matr1 = z2.Matrix(matrix1)
    matr2 = z2.Matrix(matrix2)
    result = [[2, 4, 6, 9], [8, 10, 11, 13], [14, 16, 18, 12], [2, 4, 6, 16]]
    assert matr1 + matr2, result

def test_mul(matrix1, matrix2):
    matr1 = z2.Matrix(matrix1)
    matr2 = z2.Matrix(matrix2)
    result = [[34, 44, 54, 70], [66, 87, 108, 141], [107, 136, 165, 186], [38, 52, 66, 102]]
    assert matr1 * matr2, result

def test_print(capfd, matrix1 ):
    matr1 = z2.Matrix(matrix1)
    print(matr1)
    captured = capfd.readouterr()
    assert captured.out == '((1, 2, 3, 4), (4, 5, 5, 7), (7, 8, 9, 5), (1, 2, 3, 8))\n'

if __name__ == '__main__':
    pytest.main(['-v'])