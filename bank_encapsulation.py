# Encapsulation and Access Modifiers (Public, Private, Protected)

# ! Encapsulation -> Hide Details
# ! Access Modifer -> Public, Protected, Private

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = 'banani 11' # protected
        self.__balance = initial_deposit # prive

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount

        else:
            return f'OPPS! You have no money.'
    
rafsun = Bank('Choooto Bro', 10000)


print(rafsun.holder_name)
rafsun.holder_name = 'Boro Bhai'
rafsun.deposit(5000)
print(rafsun.get_balance())
print(rafsun.holder_name)
# print(rafsun._branch)
# print(dir(rafsun))
print(rafsun._Bank__balance)





# Single underscore vs Double underscore

""" class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self._balance = initial_deposit

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
    
rafsun = Bank('Choooto Bro', 10000)
aziz = Bank('Boro Bro', 20000)

print(rafsun.holder_name)
rafsun.deposit(5000)
print(rafsun.get_balance())

print(aziz.holder_name)
aziz.deposit(10000)
print(aziz.get_balance())
 """