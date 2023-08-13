# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

from UserException import BackpackError

def filling_backpack(things, backpack_capacity) -> str:
    ''' 
    >>> filling_backpack({'палатка':3, 'фонарь':1.5, 'аптечка':1, 'зажигалка':0.015, 'термос':0.7, 'котелок':0.8, 'топор': 0.6, 'нож':0.1, 'Столовые приборы':0.25, 'еда':1.2}, 0)
    Traceback (most recent call last):
    ...
    UserException.BackpackError: Не коректное значение аргумета backpack_capacity. Аргумент должен быть больше 0
    >>> filling_backpack({'палатка':3, 'фонарь':1.5, 'аптечка':1, 'зажигалка':0.015, 'термос':0.7, 'котелок':0.8, 'топор': 0.6, 'нож':0.1, 'Столовые приборы':0.25, 'еда':1.2}, 9)
    "Наполнение рюкзака: ['палатка', 'фонарь', 'аптечка', 'зажигалка', 'термос', 'котелок', 'топор', 'нож', 'Столовые приборы'], вес: 7.964999999999999"
    >>> filling_backpack({'палатка':3, 'фонарь':1.5, 'аптечка':1, 'зажигалка':0.015, 'термос':0.7, 'котелок':0.8, 'топор': 0.6, 'нож':0.1, 'Столовые приборы':0.25, 'еда':1.2}, 5)
    "Наполнение рюкзака: ['палатка', 'фонарь', 'зажигалка', 'нож', 'Столовые приборы'], вес: 4.864999999999999"
    '''
    if isinstance(backpack_capacity, (float,int)) and backpack_capacity > 0:
        backpack_weight = 0
        contents_backpack = []
        for i, j in things.items():
            if backpack_weight + j <= backpack_capacity:
                backpack_weight += j
                contents_backpack.append(i)
        return f'Наполнение рюкзака: {contents_backpack}, вес: {backpack_weight}'
    else:
        raise BackpackError(backpack_capacity)


if __name__ == '__main__':
    # list_of_things = {'палатка':3, 'фонарь':1.5, 'аптечка':1, 'зажигалка':0.015, 'термос':0.7, 'котелок':0.8, 'топор': 0.6, 'нож':0.1, 'Столовые приборы':0.25, 'еда':1.2}
    # print(filling_backpack(list_of_things, 5))
    import doctest
    doctest.testmod(verbose=True)

