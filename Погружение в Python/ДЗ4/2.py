# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def function (**kwargs):
    dictionary = {}
    for i, j in kwargs.items():
        if isinstance(j, (list, dict, bytearray, frozenset)):
            j = str(j)
        dictionary[j] = i
    return dictionary


if __name__ == '__main__':
    print(function (z=1, x=2, c='три', v=[1,2,3], b=(1,2,3), n=True, m={1:'z', 2:'x', 3:'c'}, a='1',s=1))