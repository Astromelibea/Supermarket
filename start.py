from register import Register
from product import Product


# Create list of products

washingpowder=Product('Washing powder', 8.00)
chocolate=Product('Chocolate', 2.00)
chinese_vegs=Product('Chinese vegetables', 3.00)
yoghurt=Product('Yoghurt', 1.50)
butter=Product('Butter', 2.25)

products=[washingpowder,chocolate,chinese_vegs,yoghurt,butter]

register = Register(products)
register.create_sale()
register.get_total()
register.get_receipt()



