# GfG

"""

 # Parent class
class Parent :        
           # Constructor
           # Variables of Parent class

           # Methods
           ...

           ...


# Child class inheriting Parent class 
class Child(Parent) :  
           # constructor of child class
           # variables of child class
           # methods of child class

           ...

           ... 

 """


 # parent class
class Parent:

	# parent class method
	def m1(self):
		print('Parent Class Method called...')

# child class inheriting parent class
class Child(Parent):

	# child class constructor
	def __init__(self):
		print('Child Class object created...')

	# child class method
	def m2(self):
		print('Child Class Method called...')


# creating object of child class
obj = Child()

# calling parent class m1() method
obj.m1()

# calling child class m2() method
obj.m2()

print('-----------------Inheritance End-----------------------')

# Composite
""" 
class A :

      # variables of class A
      # methods of class A
      ...
      ...

class B : 
      # by using "obj" we can access member's of class A.
      obj = A()

      # variables of class B
      # methods of class B
      
      ...
      ...

 """


class Component:

# composite class constructor
	def __init__(self):
		print('Component class object created...')

	# composite class instance method
	def m1(self):
		print('Component class m1() method executed...')


class Composite:

	# composite class constructor
	def __init__(self):

		# creating object of component class
		self.obj1 = Component()
		
		print('Composite class object also created...')

	# composite class instance method
	def m2(self):
		
		print('Composite class m2() method executed...')

		# calling m1() method of component class
		self.obj1.m1()


# creating object of composite class
obj2 = Composite()

# calling m2() method of composite class
obj2.m2()




