""" 

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

# print('Recheck') 

"""

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")