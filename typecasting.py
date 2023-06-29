# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

#Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.



""" 
Two Types of Typecasting:

1. Explicit Conversion (Explicit type casting in python)

2. Implicit Conversion (Implicit type casting in python).

"""







# Explicit Conversion
""" a = 2
b = 3
print(a + b) """

""" a = "10"
b = "20"
print(int(a) + int(b)) """


#Implicit Conversion
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))