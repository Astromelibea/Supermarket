from product import Product

class Register:

    def __init__(self, products):
        self.products = products


    def create_sale(self):
        self.shopping_cart=[(self.products[0], 2), (self.products[2], 1), (self.products[4],4)]


    def get_total(self):
         total = 0
         for item in self.shopping_cart:
            total += item[0].price * item[1]
         return total

    def get_receipt(self):
        for item in self.shopping_cart:
            print([(item[0].name, item[0].price)])














