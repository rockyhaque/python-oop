class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_item(self, item):
        pass
    
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity'] 
        print('Total Price',total)
        if amount < total:
            print(f'Please Provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your items & extra money:  {extra}')

rocky = shopping('Rocky Haque')
rocky.add_to_cart('Potato', 50, 6)
rocky.add_to_cart('Egg', 12, 24)
rocky.add_to_cart('Rice', 50, 5)

print(rocky.cart)
rocky.checkout(1600)