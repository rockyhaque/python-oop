""" 
->Lists:
1. Lists are ordered collection of data items.
2. They store multiple items in a single variable.
3. List items are separated by commas and enclosed within square brackets [].
4. Lists are changeable meaning we can alter them after creation.

"""

marks = [2, 4, 6, "Rocky", True]

# print(marks)
# print(type(marks))
# print(marks[4])

# print(marks[-2]) # Negative index
# print(marks[len(marks)-2]) # Positive index
# print(marks[5-2]) # Positive index
# print(marks[3]) # Positive index

# if "ocky" in "Rocky":
#     print("Yes")
# else:
#     print("No")

# colors = ["Red", "Yello", "Pink"]
# print(colors[1])


""" 
-> List Comprehension:

List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

"""



# li = [i*i for i in range(4)]
# print(li)

# li = [i for i in range(10) if i%2 == 0]
# print(li)





# -> Example 1: Accepts items with the small letter “o” in the new list

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)





# -> Example 2: Accepts items which have more than 4 letters

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if (len(item) > 4)]
# print(namesWith_O)