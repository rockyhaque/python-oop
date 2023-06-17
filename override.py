# Operator overloading and method overriding

#eat() func has in child class and parent class that's why overwrite occure

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name 
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('biriyani ice-cream chips')


class Cricketer(Person):
    def __init__(self, name, age, height, weight ,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # ! override
    def eat(self):
        print('vegetables')

    def exercise(self):
        print('Gym is loss project 😂')

    def __add__(self, other):
        return self.age + other.age 

    def __mul__(self, other):
        return self.weight * other.weight

    def __len__(self):
        return self.height
    
    def __gt__(self, other):
        return self.age > other.age

"""
     __le__    -> Less Than
    __eq__    => Equal
    __ne__    => Not equal 

"""


sakib = Cricketer('sakib', 38, 68, 91, 'BD')
musfiq = Cricketer('Musfiq', 36, 65, 78, 'BD')
# sakib.eat()
# sakib.exercise()



# ! Plus sign oberload
print(50 + 60)
print('sakib' + 'takib')
print([12, 98] + [5, 6, 7, 1, 2])
print(sakib + musfiq)
print(sakib * musfiq)
print(len(sakib))
print(sakib > musfiq)