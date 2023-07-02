""" 

class Bike:
    name = ""
...
# create object
bike1 = Bike() 

"""

# we can also initialize values using the constructors. For example,

class Bike:

    # constructor function    
    def __init__(self, name = ""):
        self.name = name
    
    # method to print the name of the bike
    def print_name(self):
        print(self.name)

# create object
bike1 = Bike("Mountain Bike")

# print the name of the bike
bike1.print_name()




# Another Example
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")