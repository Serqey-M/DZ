import os
import unittest
import z1
import UserException

class TestCaseZ1 (unittest.TestCase):
    def setUp(self) -> None:
        self.student_1 = z1.Student(1,'Иванов', 'Иван', 'Иванович')
        self.student_2 = z1.Student(2,'Петров', 'Петр', 'Петрович')

    def tearDown(self) -> None:
        if os.path.exists(f'{z1.directory}/_2.json'):
            os.remove(f'{z1.directory}/_2.json')

    def test_name(self):
        self.assertEqual(self.student_1.name, 'Иван')

    def test_surname(self):
        self.assertEqual(self.student_1.surname, 'Иванов')

    def test_error_init1(self):
        self.assertRaisesRegex(UserException.NameError, 'Значение Иванович! не соответствует требованиям. Значение должно содержать только буквы.',
                               z1.Student, 1,'Иванов', 'Иван', 'Иванович!')
        
    def test_error_init2(self):
        self.assertRaisesRegex(UserException.NameError, 'Значение иван! не соответствует требованиям. Значение должно содержать только буквы и начинаться с заглавной буквы.',
                               z1.Student, 1,'Иванов', 'иван!', 'Иванович!')
        
    def test_error_init3(self):
        self.assertRaisesRegex(UserException.NameError, 'Значение иван не соответствует требованиям. Значение длжно начинаться с заглавной буквы.',
                               z1.Student, 1,'Иванов', 'иван', 'Иванович!')
        
    def test_reading_information(self):
        self.assertEqual(self.student_1.reading_information(), {'Математика': {'оценки': [2, 3, 4, 5, 4, 3, 2], 'тесты': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}, 'Физика': {'оценки': [], 'тесты': [1, 1]}, 'Химия': {'оценки': [], 'тесты': [100, 100]}, 'История': {'оценки': [2, 2], 'тесты': []}, 'Литература': {'оценки': [5, 5], 'тесты': []}})

    def test_adding_assessment(self):
        self.student_2.adding_assessment('Математика', 5, 1)   
        self.assertEqual(self.student_2.reading_information(), {'Математика': {'оценки': [5], 'тесты': []}, 'Физика': {'оценки': [], 'тесты': []}, 'Химия': {'оценки': [], 'тесты': []}, 'История': {'оценки': [], 'тесты': []}, 'Литература': {'оценки': [], 'тесты': []}})

    def test_average_test_score(self):
        self.assertEqual(self.student_1.average_test_score('Математика'), 50.0)

    def test_overall_average_assessment(self):
        self.assertEqual(self.student_1.overall_average_assessment(), 3.36)
       
if __name__ == '__main__':
    unittest.main()