#inheritance vs composition

#inheritance
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f'The {self.name} is driving.')

class Car(Vehicle):
    def __init__(self, name, make):
        super().__init__(name)
        self.make = make

    def honk(self):
        print('Beep! Beep!')

car = Car('Tesla Model 3', 'Tesla')
car.drive()
car.honk()
# !output: The Tesla Model 3 is driving. Beep! Beep!

# As you can see, the Car class inherits from the Vehicle class. This means that the Car class has all of the properties and methods of the Vehicle class, plus its own additional properties and methods.


#composition
class Engine:
    def __init__(self, size):
        self.size = size

    def start(self):
        print(f'The engine is {self.size} liters and is starting.')

class Car:
    def __init__(self, name, make, engine):
        self.name = name
        self.make = make
        self.engine = engine

    def drive(self):
        print(f'The {self.name} is driving with a {self.engine.size} liter engine.')

car = Car('Tesla Model 3', 'Tesla', Engine(2.0))
car.drive()
# !output: The Tesla Model 3 is driving with a 2.0 liter engine.

# As you can see, the Car class contains an instance of the Engine class. This means that the Car class has access to the Engine class's properties and methods.
