#Read only -> can not set the set the value. value can not be changed
#getter -> get a value of a property through a method. Most of the time, you will get the value of a private attribute
#setter -> set a value of a property through a method. Most of the time, you will set the value of a privater property

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self._money = money

    #getter without only setter is readonly attribute
    @property
    def age(self):
        return self._age
    
    #getter
    @property
    def salary(self):
        return self._money

    #setter
    @salary.setter
    def salary(self, value):
        if value < 0: 
            return 'Salary can not be negative'
        self._money += value

zarin = User('Tasnim', 24, 22000)

# print(zarin._money)
# print(zarin.age())

print(zarin.age)

""" print(zarin.salary()) # for adding @property, have to remove () """

print(zarin.salary)
zarin.salary = 30000
print(zarin.salary)
