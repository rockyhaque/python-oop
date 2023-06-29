# -> list.sort()

# This method sorts the list in ascending order. The original list is updated

# Example 1:

# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# print(num)


"""  

What if you want to print the list in descending order?
We must give reverse=True as a parameter in the sort method.
"""

# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort(reverse=True)
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort(reverse=True)
# print(num)

# The reverse parameter is set to False by default.

# ! Note: Do not mistake the reverse parameter with the reverse method.





# * reverse()

# This method reverses the order of the list.

# colors = ["voilet", "indigo", "blue", "green"]
# colors.reverse()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.reverse()
# print(num)



# * index()

# This method returns the index of the first occurrence of the list item.


# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.index("green"))

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.index(3))



# * count()

# Returns the count of the number of items with the given value.


# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.count("green"))

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.count(4))




# * copy()

# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.


# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)



# * append()

# This method appends items to the end of the existing list.

# colors = ["voilet", "indigo", "blue"]
# colors.append("green")
# print(colors)




# * insert():

# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.


""" 

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

"""





# * extend():

# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

#add a list to a list

# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)




# -> Concatenating two lists:

# You can simply concatenate two lists to join two lists.


# colors = ["voilet", "indigo", "blue", "green"]
# colors2 = ["yellow", "orange", "red"]
# print(colors + colors2)