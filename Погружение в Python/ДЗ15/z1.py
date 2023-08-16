# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import argparse
import csv
import json
import logging
from datetime import datetime
from pathlib import Path
from UserException import NameError, AssessmentError, TypeError

MIN_assessment = 2
MAX_assessment = 5
MIN_test = 0
MAX_test = 100
directory = 'D:\GB\ДЗ\Погружение в Python\ДЗ15'

logging.basicConfig(level=0, filename=f'{directory}/log_z1.log', encoding='utf-8', style='{')
logger = logging.getLogger(__name__)


class Descriptor_name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value.isalpha() and value.istitle():
            setattr(instance, self.param_name, value)
        else:
            logger.error(f'{datetime.now()}: {NameError(value)}')
            raise NameError(value)


class Student:
    surname = Descriptor_name()
    name = Descriptor_name()
    patronymic = Descriptor_name()


    def __init__(self, id: int, surname: str, name: str, patronymic: str) -> None:
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
        logger.info(f'{datetime.now()}: Создание нового объекта: {self.id} {self.surname} {self.name} {self.patronymic}')
        

    def reading_information(self) -> dict[dict]:
        with open(f'{directory}\_{self.id}.json', 'r', encoding='utf-8') as f:
            self.__list_of_disciplines = json.load(f)
        logger.info(f'{datetime.now()}: Чтение информации о студенте {self.id} {self.surname} {self.name} {self.patronymic}: {self.__list_of_disciplines}')
        return self.__list_of_disciplines


    def adding_assessment(self, discipline: str, assessment: int, type_: int = 1) -> None:
        '''type_ 1 - Оценка, type_ 0 - Тест'''
        self.reading_information()
        match type_:
            case 1:
                if MIN_assessment <= assessment <= MAX_assessment:
                    temp = self.__list_of_disciplines[discipline]['оценки']
                    temp.append(assessment)
                    self.__list_of_disciplines[discipline]['оценки'] = temp
                    logger.info(f'{datetime.now()}: Добавление оценки студенту {self.id} {self.surname} {self.name} {self.patronymic}: предмет - {discipline}, оценка - {assessment}')
                else:
                    logger.error(f'{datetime.now()}: {AssessmentError(assessment, MIN_assessment, MAX_assessment)}')
                    raise AssessmentError(assessment, MIN_assessment, MAX_assessment)
            case 0:
                if MIN_test <= assessment <= MAX_test:
                    temp = self.__list_of_disciplines[discipline]['тесты']
                    temp.append(assessment)
                    self.__list_of_disciplines[discipline]['тесты'] = temp
                    logger.info(f'{datetime.now()}: Добавление результата теста студенту {self.id} {self.surname} {self.name} {self.patronymic}: предмет - {discipline}, оценка - {assessment}')
                else:
                    logger.error(f'{datetime.now()}: {AssessmentError(assessment, MIN_test, MAX_test)}')                    
                    raise AssessmentError(assessment, MIN_test, MAX_test)
            case _:
                logger.error(f'{datetime.now()}: {TypeError()}')
                raise TypeError()
        with open(f'{directory}\_{self.id}.json', 'w', encoding='utf-8') as f:
            json.dump(self.__list_of_disciplines, f, ensure_ascii=False, indent=2)


    def average_test_score(self, discipline: str) -> float:
        self.reading_information()
        data = self.__list_of_disciplines[discipline]['тесты']
        sum = 0 
        for i in data:
            sum += i
        if len(data) < 1:
            result = 0
        else:
            result = round(sum/len(data), 2)
        logger.info(f'{datetime.now()}: Средний бал по тесту у студента {self.id} {self.surname} {self.name} {self.patronymic} по предмету {discipline} - {result}')
        return result


    def overall_average_assessment(self) -> float:
        self.reading_information()
        sum = 0
        count = 0
        for i in self.__list_of_disciplines:
            for j in self.__list_of_disciplines[i]['оценки']:
                sum += j
                count += 1
        if count < 1:
            result = 0
        else:
            result = round(sum/count, 2)
        logger.info(f'{datetime.now()}: Средняя оценка у студента {self.id} {self.surname} {self.name} {self.patronymic} - {result}')
        return result
                

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}, Оценки: {self.reading_information()}'
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='class Student', description='Работа класса студент: Создание объекта класса, \
                                     вывод средней оценки, вывод среднего балла, Вывод информации об объкте, добавление оценки',\
                                          epilog='Работа с class Student')
    parser.add_argument('-id', metavar ='id', type = int, help ='id объекта класса', default = -1)
    parser.add_argument('-s', metavar ='s', type = str, help ='Фамилия', default = 'User')
    parser.add_argument('-m', metavar ='m', type = str, help ='Имя', default = 'User')
    parser.add_argument('-p', metavar ='p', type = str, help ='Отчество', default = 'User')
    parser.add_argument('-dt', metavar ='dt', type = str, help ='Предмет для вывода средней оценки', default = 'Математика')
    parser.add_argument('-da', metavar ='da', type = str, help ='Предмет для добавления оценки', default = 'Математика')
    parser.add_argument('-a', metavar ='a', type = int, help ='Оценка', default = -1)
    parser.add_argument('-t', metavar ='t', type = int, help ='Выбор типа добавляемой оценки(1 - оценка, 0 - тест)', default = -1)
    args = parser.parse_args()

    stud1 = Student(args.id, args.s, args.m, args.p)
    print(stud1.overall_average_assessment())
    print(stud1.average_test_score(args.dt))
    print(stud1.reading_information())
    stud1.adding_assessment(args.da, args.a, args.t)
    print(stud1)
  


