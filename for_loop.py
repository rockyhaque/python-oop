""" 
name = 'Rocky'
for i in name:
    # print(i, end=" ")
    print(i)
    if(i == "c"):
        print("I love C keyword") 
        
"""


#  iterating over a list:
""" 
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for char in color:
        print(char) 
        
"""


#Range
for k in range(5): # o to 4
    # print(k)
    print(k + 1)

for k in range(1, 9):
    print(k)

for k in range(1, 9, 2): # 2 is step here
    print(k)