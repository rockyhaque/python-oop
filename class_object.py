# A class is a blueprint or template for creating objects

class Person:
    name = "Rocky"
    age = 22
    ocuupation = "Software Engineer"
    marital_status = 'Single'

    # *Methods are functions that are defined inside a class. 

    # *name, age, occupation thoes are attribute and Rocky, 22, Software Engineer are values


    def basic_info(self):
        print(f'{self.name} is a {self.ocuupation}\n')

        # * The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.



    def family_info(self):
        print(f'{newPerson.name} is a {newPerson.marital_status} person')

# *newPerson object has the name attribute and the basic_info method.

newPerson = Person()
newPerson2 = Person()


# Could be change
newPerson.name = 'Mr. Rocky'
newPerson.age = 22.5
# print(newPerson.name, newPerson.age)

newPerson2.name = 'Abdul Ali'
newPerson2.age = 33

newPerson.basic_info()
newPerson.family_info()

newPerson2.basic_info()
newPerson2.family_info()


print('-------New Program-------')

class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
