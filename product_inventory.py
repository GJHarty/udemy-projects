
# Define a Product class. Objects should have 3 variables for price, code, and quantity
class Product:
    
    def __init__(self, price=0.00, code='aaaa', quantity=0):
        self.price = price
        self.code = code
        self.quantity = quantity
    
    def __repr__(self):
        return f'Product({self.price!r}, {self.code!r}, {self.quantity!r})'
    
    def __str__(self):
        return f'The product code is: {self.code}'

# Define an inventory class and a function for calculating the total value of the inventory. 
class Inventory:    
    
    def __init__(self):
        self.products_list = []
    
    def add_product(self, product):
        self.products_list.append(product)
        return self.products_list
        
    def total_value(self):
        return sum(product.price * product.quantity for product in self.products_list)
