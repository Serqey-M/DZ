# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

from UserException import BackpackError

class Backpack():
    backpack_weight = 0
    contents_backpack = []

    def __init__(self, things: dict, backpack_capacity: float | int) -> None:
        self.things = things
        if isinstance(backpack_capacity, (float,int)) and backpack_capacity > 0:
            self.backpack_capacity = backpack_capacity
        else:
            raise BackpackError(backpack_capacity)

    def filling_backpack(self) -> str:
        for i, j in self.things.items():
            if self.backpack_weight + j <= self.backpack_capacity:
                self.backpack_weight += j
                self.contents_backpack.append(i)
        return f'Наполнение рюкзака: {self.contents_backpack}, вес: {self.backpack_weight}'


    def possible_backpack_fillings(self):

        sorted_things = sorted(self.things.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(sorted_things)):
            for items, weight  in dict(sorted_things).items():
                if self.backpack_weight + weight <= self.backpack_capacity:
                    self.backpack_weight += weight
                    self.contents_backpack.append(items)
            print(f'{i+1}. Наполнение рюкзака: {self.contents_backpack}, вес: {self.backpack_weight}')
            sorted_things.append(sorted_things[0])
            sorted_things.pop(0)
            self.backpack_weight = 0
            self.contents_backpack = []

if __name__ == '__main__':
    list_of_things = {'палатка':3, 'фонарь':1.5, 'аптечка':1, 'зажигалка':0.015, 'термос':0.7, 'котелок':0.8, 'топор': 0.6, 'нож':0.1, 'Столовые приборы':0.25, 'еда':1.2}
    backpack = Backpack(list_of_things, 0)

