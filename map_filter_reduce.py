# Map

def cube(x):
    return x*x*x

print(cube(2))

l = [1, 2, 3, 4, 5]

# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube, l))
print(newl)



# Filter

def filter_func(a):
    return a>2

newnewl = list(filter(filter_func, l))
print(newnewl)



# Reduce

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)