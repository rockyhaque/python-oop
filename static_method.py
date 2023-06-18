class Shopping:
    cart = [] # class attribute # static attribute
    origin = 'China'

    def __init__(self, name, location) -> None:
        self.name = 'Jamuna city' #instance attribute
        self.location = 'khilket er pore'

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply(a, b):
        result = a*b
        print(result)

    @classmethod
    def extra(self, item):
        print('Not useful', item)

    

basundara = Shopping('Best place', 'But high price')

basundara.extra('Nothing')
# basundara.purchase('pen', 500, 1200)
# Shopping.purchase('oil', 2 ,30,  30)   
Shopping.extra('Shirt')
Shopping.multiply(4, 5)
