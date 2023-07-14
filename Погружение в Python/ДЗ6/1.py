# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

MIN_DATE = 1
MAX_DAY = 31
MAX_MONTH = 12
MAX_YEAR = 9999


def is_real_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if not(MIN_DATE <= year <= MAX_YEAR and MIN_DATE <= month <= MAX_MONTH and MIN_DATE <=day <= MAX_DAY):
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and _is_leap_year(year) and day > 29:
        return False
    if month == 2 and not _is_leap_year(year) and day > 28:
        return False
    return True


def _is_leap_year(year: int) -> bool:
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


if __name__ == '__main__':
    print(is_real_date(str(argv[1])))