# -> Python Tuples

# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

# tp = (1, 3, 6)
# print(type(tp), tp)



# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)




# details = ("Abhijeet", 18, "FYBScIT", 9.8)
# print(details)





# -> Tuple Indexes

# Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.


# * Range of Index:

# You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

# Tuple[start : end : jumpIndex]

""" 
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes 

"""

# Example: printing every 3rd consecutive withing given range

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])

# output: ('dog', 'pig', 'goat')