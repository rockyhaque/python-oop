# Poly -> many(multiple)
# morpy -> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal making sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Meow Meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Ghew Gheu')  

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Beh Beh Beh')

don = Cat('Real Don')
don.make_sound()

shepard = Dog('Local Shepard')
shepard.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('Gora Gori')

animals = [don, shepard, mess]
for animal in animals:
    animal.make_sound()