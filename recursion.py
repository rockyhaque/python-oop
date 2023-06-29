""" 
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1
factorial(0) = 1

factorial(n) = n * factorial(n-1)

-> How works:

4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1) 
4 * 3 * 2 * 1   -->> (n==0 or 1 ) return 1

"""

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(3))
n = int(input("Enter your number: "))
print(factorial(n))