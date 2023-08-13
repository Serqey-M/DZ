import os
import pytest
import z1
import UserException

@pytest.fixture
def student_1():
    return z1.Student(1,'Иванов', 'Иван', 'Иванович')

@pytest.fixture
def student_2():
    return z1.Student(2,'Петров', 'Петр', 'Петрович')

@pytest.fixture
def delet():
    if os.path.exists(f'{z1.directory}/_2.json'):
        os.remove(f'{z1.directory}/_2.json')

def test_name(student_1):
    assert student_1.name == 'Иван'

def test_print_surname(capfd, student_1):
    print(student_1.surname)
    captured = capfd.readouterr()
    assert captured.out == 'Иванов\n'

def test_error_init1():
    with pytest.raises(UserException.NameError, match = r'Значение Иванович! не соответствует требованиям. Значение должно содержать только буквы.'):
        z1.Student(1,'Иванов', 'Иван', 'Иванович!')

def test_error_init2():
    with pytest.raises(UserException.NameError, match = r'Значение иван! не соответствует требованиям. Значение должно содержать только буквы и начинаться с заглавной буквы.'):
        z1.Student(1,'Иванов', 'иван!', 'Иванович!')

def test_error_init3():
    with pytest.raises(UserException.NameError, match = r'Значение иван не соответствует требованиям. Значение длжно начинаться с заглавной буквы.'):
        z1.Student(1,'Иванов', 'иван', 'Иванович!')

def test_reading_information(student_1):
    assert student_1.reading_information() == {'Математика': {'оценки': [2, 3, 4, 5, 4, 3, 2], 'тесты': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}, 'Физика': {'оценки': [], 'тесты': [1, 1]}, 'Химия': {'оценки': [], 'тесты': [100, 100]}, 'История': {'оценки': [2, 2], 'тесты': []}, 'Литература': {'оценки': [5, 5], 'тесты': []}}

def test_adding_assessment(delet, student_2):
    student_2.adding_assessment('Математика', 5, 1)   
    assert student_2.reading_information() == {'Математика': {'оценки': [5], 'тесты': []}, 'Физика': {'оценки': [], 'тесты': []}, 'Химия': {'оценки': [], 'тесты': []}, 'История': {'оценки': [], 'тесты': []}, 'Литература': {'оценки': [], 'тесты': []}}

def test_average_test_score(student_1):
    assert student_1.average_test_score('Математика') == 50.0

def test_overall_average_assessment(student_1):
    assert student_1.overall_average_assessment() == 3.36

def test_print(capfd, student_1):
    print(student_1)
    captured = capfd.readouterr()
    assert captured.out == "Иванов Иван Иванович, Оценки: {'Математика': {'оценки': [2, 3, 4, 5, 4, 3, 2], 'тесты': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}, 'Физика': {'оценки': [], 'тесты': [1, 1]}, 'Химия': {'оценки': [], 'тесты': [100, 100]}, 'История': {'оценки': [2, 2], 'тесты': []}, 'Литература': {'оценки': [5, 5], 'тесты': []}}\n"


if __name__ == '__main__':
    pytest.main(['-v'])