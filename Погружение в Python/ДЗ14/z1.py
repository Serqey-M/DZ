# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
import json
from pathlib import Path
from UserException import NameError, AssessmentError, TypeError

MIN_assessment = 2
MAX_assessment = 5
MIN_test = 0
MAX_test = 100
directory = 'D:\GB\ДЗ\Погружение в Python\ДЗ14'


class Descriptor_name:
    '''
    >>> student_1 = Student(1,'Иванов', 'Иван', 'Иванович')
    '''
    def __set_name__(self, owner, name):
        '''
        >>> Student(1,'Иванов', 'Иван', 'Иванович').name
        'Иван'
        '''
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        '''
        >>> print(Student(1,'Иванов', 'Иван', 'Иванович').surname)
        Иванов
        '''
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        '''
        >>> Student(1,'Иванов', 'Иван', 'Иванович!')
        Traceback (most recent call last):
        ...
        UserException.NameError: Значение Иванович! не соответствует требованиям. Значение должно содержать только буквы.
        '''        
        if value.isalpha() and value.istitle():
            setattr(instance, self.param_name, value)
        else:
            raise NameError(value)


class Student:
    '''
    >>> Student(1,'Иванов', 'иван!', 'Иванович')
    Traceback (most recent call last):
    ...
    UserException.NameError: Значение иван! не соответствует требованиям. Значение должно содержать только буквы и начинаться с заглавной буквы.
    '''    
    surname = Descriptor_name()
    name = Descriptor_name()
    patronymic = Descriptor_name()


    def __init__(self, id: int, surname: str, name: str, patronymic: str) -> None:
        '''
        >>> Student(1,'Иванов', 'иван', 'Иванович')
        Traceback (most recent call last):
        ...
        UserException.NameError: Значение иван не соответствует требованиям. Значение длжно начинаться с заглавной буквы.
        '''
        self.id = id
        self.surname = surname 
        self.name = name 
        self.patronymic = patronymic 
        self.__list_of_disciplines = {}
        with open(f'{directory}\discipline.csv', 'r', newline='', encoding='utf-8') as f:
            disciplines = list(csv.reader(f))
        for i in disciplines:
            self.__list_of_disciplines[i[0]] = {'оценки': [], 'тесты': []}
        if not Path(f'{directory}\_{self.id}.json').exists():
            with open(f'{directory}\_{self.id}.json', 'w', encoding='utf-8') as f:
                json.dump(self.__list_of_disciplines, f, ensure_ascii=False, indent=2)


    def reading_information(self) -> dict[dict]:
        '''
        >>> Student(1,'Иванов', 'Иван', 'Иванович').reading_information()
        {'Математика': {'оценки': [2, 3, 4, 5, 4, 3, 2], 'тесты': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}, 'Физика': {'оценки': [], 'тесты': [1, 1]}, 'Химия': {'оценки': [], 'тесты': [100, 100]}, 'История': {'оценки': [2, 2], 'тесты': []}, 'Литература': {'оценки': [5, 5], 'тесты': []}}
        '''
        with open(f'{directory}\_{self.id}.json', 'r', encoding='utf-8') as f:
            self.__list_of_disciplines = json.load(f)
        return self.__list_of_disciplines


    def adding_assessment(self, discipline: str, assessment: int, type_: int = 1) -> None:
        '''type_ 1 - Оценка, type_ 0 - Тест
        >>> Student(2,'Петров', 'Петр', 'Петрович').adding_assessment('Математика', 5, 1)
        '''
        self.reading_information()
        match type_:
            case 1:
                if MIN_assessment <= assessment <= MAX_assessment:
                    temp = self.__list_of_disciplines[discipline]['оценки']
                    temp.append(assessment)
                    self.__list_of_disciplines[discipline]['оценки'] = temp
                else:
                    raise AssessmentError(assessment, MIN_assessment, MAX_assessment)
            case 0:
                if MIN_test <= assessment <= MAX_test:
                    temp = self.__list_of_disciplines[discipline]['тесты']
                    temp.append(assessment)
                    self.__list_of_disciplines[discipline]['тесты'] = temp
                else:
                    raise AssessmentError(assessment, MIN_test, MAX_test)
            case _:
                raise TypeError()
        with open(f'{directory}\_{self.id}.json', 'w', encoding='utf-8') as f:
            json.dump(self.__list_of_disciplines, f, ensure_ascii=False, indent=2)


    def average_test_score(self, discipline: str) -> float:
        '''
        >>> Student(1,'Иванов', 'Иван', 'Иванович').average_test_score('Математика')
        50.0
        '''
        self.reading_information()
        data = self.__list_of_disciplines[discipline]['тесты']
        sum = 0 
        for i in data:
            sum += i
        return round(sum/len(data), 2)


    def overall_average_assessment(self) -> float:
        '''
        >>> Student(1,'Иванов', 'Иван', 'Иванович').overall_average_assessment()
        3.36
        '''        
        self.reading_information()
        sum = 0
        count = 0
        for i in self.__list_of_disciplines:
            for j in self.__list_of_disciplines[i]['оценки']:
                sum += j
                count += 1
        return round(sum/count, 2)
                

    def __str__(self) -> str:
        '''
        >>> print(Student(1,'Иванов', 'Иван', 'Иванович'))
        Иванов Иван Иванович, Оценки: {'Математика': {'оценки': [2, 3, 4, 5, 4, 3, 2], 'тесты': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}, 'Физика': {'оценки': [], 'тесты': [1, 1]}, 'Химия': {'оценки': [], 'тесты': [100, 100]}, 'История': {'оценки': [2, 2], 'тесты': []}, 'Литература': {'оценки': [5, 5], 'тесты': []}}
        '''   
        return f'{self.surname} {self.name} {self.patronymic}, Оценки: {self.reading_information()}'
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)