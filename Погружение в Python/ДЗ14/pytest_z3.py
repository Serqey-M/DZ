import pytest
import z3
import UserException

@pytest.fixture
def things():
    return {'палатка':3, 'фонарь':1.5, 'аптечка':1, 'зажигалка':0.015, 'термос':0.7, 'котелок':0.8, 'топор': 0.6, 'нож':0.1, 'Столовые приборы':0.25, 'еда':1.2}

def test_error(things):
    with pytest.raises(UserException.BackpackError, match = r'Не коректное значение аргумета backpack_capacity. Аргумент должен быть больше 0'):
        z3.filling_backpack(things, 0)

def test_1(things):
    assert z3.filling_backpack(things, 9) == "Наполнение рюкзака: ['палатка', 'фонарь', 'аптечка', 'зажигалка', 'термос', 'котелок', 'топор', 'нож', 'Столовые приборы'], вес: 7.964999999999999"

def test_2(things):
    assert z3.filling_backpack(things, 5) == "Наполнение рюкзака: ['палатка', 'фонарь', 'зажигалка', 'нож', 'Столовые приборы'], вес: 4.864999999999999"    