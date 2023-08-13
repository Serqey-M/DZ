import unittest
import z2
import UserException

class TestCaseZ2 (unittest.TestCase):
    def setUp(self) -> None:
        self.matrix1 = ((1, 2, 3, 4),
                        (4, 5, 5, 7),
                        (7, 8, 9, 5),
                        (1, 2, 3, 8))
        self.matrix2 = ((1, 2, 3, 5), 
                        (4, 5, 6, 6), 
                        (7, 8, 9, 7), 
                        (1, 2, 3, 8))
        self.matrix3 = ((1, 2, 3, 4),
                        (4, 5, 5, 7),
                        (7, 8, 9, 5),
                        (1, 2, 3, 8))
        self.matrix4 = ((1, 2, 3, 4),
                        (4, 5, 5, 7),
                        (7, 8, 9), 
                        (1, 2, 3, 8))
        
    def test_matrix(self):
        matr1 = z2.Matrix(self.matrix1)
        matr_tr = z2.Matrix(matr1.matrix_transposition())
        result = '[1, 4, 7, 1]\n[2, 5, 8, 2]\n[3, 5, 9, 3]\n[4, 7, 5, 8]'
        self.assertEqual(matr_tr.print_matrix_class(), result)
        
    def test_error_init(self):
        self.assertRaisesRegex(UserException.MatrixError, 'Аргумент не является матрицей. В матрице все строки должны быть одного размера',
                               z2.Matrix, self.matrix4)
        
    def test_print(self):
        matr1 = z2.Matrix(self.matrix1)
        result= '(1, 2, 3, 4)\n(4, 5, 5, 7)\n(7, 8, 9, 5)\n(1, 2, 3, 8)'
        self.assertEqual(matr1.print_matrix_class(), result)

    def test_tr(self):
        matr1 = z2.Matrix(self.matrix1)
        result = [[1, 4, 7, 1], [2, 5, 8, 2], [3, 5, 9, 3], [4, 7, 5, 8]]
        self.assertEqual(matr1.matrix_transposition(), result)
    
    def test_eq(self):
        matr1 = z2.Matrix(self.matrix1)
        matr2 = z2.Matrix(self.matrix2)
        matr3 = z2.Matrix(self.matrix3)
        self.assertFalse(matr1 == matr2)
        self.assertTrue(matr1 == matr3)

    def test_add(self):
        matr1 = z2.Matrix(self.matrix1)
        matr2 = z2.Matrix(self.matrix2)
        result = [[2, 4, 6, 9], [8, 10, 11, 13], [14, 16, 18, 12], [2, 4, 6, 16]]
        self.assertEqual(matr1 + matr2, result)

    def test_mul(self):
        matr1 = z2.Matrix(self.matrix1)
        matr2 = z2.Matrix(self.matrix2)
        result = [[34, 44, 54, 70], [66, 87, 108, 141], [107, 136, 165, 186], [38, 52, 66, 102]]
        self.assertEqual(matr1 * matr2, result)

if __name__ == '__main__':
    unittest.main()