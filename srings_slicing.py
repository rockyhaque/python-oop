names = "Rocky"
print(len(names))

print('Full Strings: ',names)
print(names[:])

print(names[0:4]) # including 0 but not 4
print(names[:4])

print(names[1:4])
print(names[0:-3])

print(names[:len(names)-3])
print(names[-1:len(names)-3])

print(names[-3:-1])



#index =   0   1   2   3   4   5   6   7   8   9
numbers = [12, 23, 34, 21, 43, 65, 74, 89, 76, 10]
#index =  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1


#list (start : end)
print(numbers[1:7])
print(numbers[1:7:2]) #skip 2
print(numbers[2:7:-1]) # index is not exist 2, 1, 0, -1, -2.....
print(numbers[7:2:-1])
print(numbers[4:])
print(numbers[:5])
print(numbers[::-1]) #shortcut to reverse a list