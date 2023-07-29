# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name:str) -> None:
        self.name = name

    def show_spec(self):
        pass

class Fish(Animal):
    LITTLE = 10
    HIGHT = 100
    def __init__(self, name:str, long:int) -> None:
        super().__init__(name)
        self.long = long
    
    def show_spec(self):
        if self.long < self.LITTLE:
            return 'Мелководная рыба'
        elif self.long > self.HIGHT:
            return 'Глубоководная рыба'
        else:
            return f'Средне-глубоководная рыба'
        
class Bird(Animal):
    def __init__(self, name: str, length:int) -> None:
        super().__init__(name)
        self.length = length

    def show_spec(self):
        return self.length*2
    
class Factory(Animal):
    def __init__(self, type_:str, name: str, args: int) -> None:
        self.type_ = type_
        self.args = args
        super().__init__(name)

    def creature (self) -> None:
        if self.type_ == Fish:
            return Fish(self.name, self.args)
        elif self.type_ == Bird:
            return Bird(self.name, self.args)
        
    
if __name__ == '__main__':
    animal1 = Factory(Fish, 'окунь', 15).creature()
    print(animal1.show_spec())
    animal2 = Factory(Bird, 'сокол', 30).creature()
    print(animal2.show_spec())