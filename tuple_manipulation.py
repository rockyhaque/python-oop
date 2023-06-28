""" 
-> Manipulating Tuples:

Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

"""



""" 

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries) 

"""

# Tuple Methods:

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = tuple1.index(3)
res = tuple1.index(3, 2, 6) # (key, start, end)

print('First occurrence of 3 is: ',res)

