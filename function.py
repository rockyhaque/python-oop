""" 
def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)

c = 8
d = 74
isGreater(c, d)

e = int(input("Enter your e: "))
f = int(input("Enter your f: "))
isGreater(e, f) 

"""
#---------------------------------

""" 
# Function Arguments and return statement:

-> There are four types of arguments that we can provide in a function:

1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments 

"""


""" 
# 1. Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

Example:

"""

""" 
def name(fname, mname = "Haq", lname = "Roky"):
    print("Hello,", fname, mname, lname)

name("Rakibul") 

"""




""" 
# 2. Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

Example:

"""

""" 
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Haq", lname = "Roky", fname = "Rakibul") 

"""




""" 
# 3. Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

Example 1: when number of arguments passed does not match to the actual function definition.

-> Error will generate

"""

""" 
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Rakibul", "Roky") 
"""



""" 
Example 2: when number of arguments passed matches to the actual function definition.

"""

""" 
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Rakibul", "Haq", "Roky") 

"""


""" 
4. Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

-> There are two ways to achieve this:
1. Arbitrary Arguments
2. Keyword Arbitrary Arguments

"""

""" 
1. Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Example:

"""


""" 

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("Rakibul", "Muhammad", "Omar") 

"""





""" 
2. Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

Example:

"""



""" 
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Haq", lname = "Roky", fname = "Rakibul") 

"""



""" 
Return Statement:
The return statement is used to return the value of the expression back to the calling function.

Example:

"""

""" def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("Rakibul", "Muhammad", "Omar")) """