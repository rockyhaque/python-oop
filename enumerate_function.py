# Enumerate function in python

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)